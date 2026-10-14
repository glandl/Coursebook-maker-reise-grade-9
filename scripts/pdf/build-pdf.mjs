// Renders the built site into one PDF scriptum per language.
//
// Hugo cannot write PDFs itself. Relearn's print output format already puts the
// whole book on one page (`index.print.html` of the home page), so a headless
// Chromium loads that page from ./public, lets the theme render the Mermaid
// diagrams, adapts a few interactive elements for paper and prints it.
//
// Usage (after `hugo`):  node build-pdf.mjs [--public ../../public] [--base-url https://…/]
// --base-url must be the baseURL the site was built with; it defaults to the one in hugo.toml.

import { chromium } from 'playwright';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '../..');

// One PDF per language. `dir` is the language's path below baseURL.
// `exclude` lists top-level sections that stay out of the student scriptum.
const BOOKS = [
  { lang: 'de', dir: '', file: 'kursbuch-informatik.pdf', title: 'Kursbuch Informatik', stand: 'Stand', online: 'Online-Version', video: 'Video', exclude: ['lehrkraefte'] },
  { lang: 'en', dir: 'en/', file: 'coursebook-informatics.pdf', title: 'Coursebook Informatics', stand: 'As of', online: 'Online version', video: 'Video', exclude: ['lehrkraefte'] },
];

const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.mjs': 'text/javascript',
  '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.gif': 'image/gif', '.webp': 'image/webp', '.ico': 'image/x-icon', '.woff': 'font/woff', '.woff2': 'font/woff2',
  '.ttf': 'font/ttf', '.xml': 'application/xml', '.txt': 'text/plain',
};

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i > -1 ? process.argv[i + 1] : fallback;
}

async function defaultBaseURL() {
  const toml = await readFile(path.join(root, 'hugo.toml'), 'utf8');
  return toml.match(/^baseURL\s*=\s*['"]([^'"]+)['"]/m)[1];
}

const publicDir = path.resolve(root, arg('public', 'public'));
let baseURL = arg('base-url', process.env.BASE_URL) || (await defaultBaseURL());
if (!baseURL.endsWith('/')) baseURL += '/';

// Answers requests for baseURL from ./public, so the page loads exactly as deployed
// without a web server. Everything else (YouTube, Wokwi, …) is blocked; those
// embeds are replaced by links anyway.
async function serveFromPublic(route) {
  const url = new URL(route.request().url());
  if (!url.href.startsWith(baseURL)) return route.abort();
  let file = path.join(publicDir, decodeURIComponent(url.pathname.slice(new URL(baseURL).pathname.length)));
  try {
    if ((await stat(file)).isDirectory()) file = path.join(file, 'index.html');
    const body = await readFile(file);
    return route.fulfill({ body, contentType: MIME[path.extname(file).toLowerCase()] ?? 'application/octet-stream' });
  } catch {
    return route.fulfill({ status: 404, body: 'not found' });
  }
}

// Runs inside the page: turns the interactive print view into something that works on paper.
async function prepareForPaper({ book, homeURL, today }) {
  // Leave out excluded sections: their article plus the nested section of subpages.
  for (const slug of book.exclude) {
    const html = await (await fetch(`${homeURL}${slug}/index.print.html`)).text();
    const id = new DOMParser().parseFromString(html, 'text/html').querySelector('article h1')?.id;
    const article = id && document.getElementById(id)?.closest('article');
    if (!article) throw new Error(`excluded section "${slug}" not found in print view`);
    const next = article.nextElementSibling;
    if (next?.tagName === 'SECTION') next.remove();
    article.remove();
  }

  // Tabs: show every tab (e.g. all four boards), each headed by its tab title.
  for (const panel of document.querySelectorAll('.tab-panel')) {
    for (const content of panel.querySelectorAll('.tab-content')) {
      const label = panel.querySelector(`.tab-nav-button[data-tab-item="${content.dataset.tabItem}"] .tab-nav-text`);
      const heading = document.createElement('p');
      heading.className = 'pdf-tab-title';
      heading.textContent = label?.textContent.trim() ?? '';
      content.prepend(heading);
      content.classList.add('active');
    }
    panel.querySelector('.tab-nav')?.remove();
  }

  // Collapsible boxes open; quiz solutions stay hidden so the quiz still works as a self-check.
  for (const details of document.querySelectorAll('details:not(.quiz-solution)')) details.open = true;

  // Embedded videos become a link.
  for (const iframe of document.querySelectorAll('iframe')) {
    const src = new URL(iframe.src);
    const yt = src.hostname.includes('youtube') && src.pathname.match(/\/embed\/([^/?]+)/);
    const href = yt ? `https://www.youtube.com/watch?v=${yt[1]}` : src.href;
    const p = document.createElement('p');
    p.className = 'pdf-embed';
    p.innerHTML = `▶ ${yt ? book.video : (iframe.title || 'Link')}: <a href="${href}">${href}</a>`;
    // the theme wraps iframes in a fixed-ratio box; replace that box, not just the iframe
    const wrapper = iframe.parentElement.style.paddingBottom ? iframe.parentElement : iframe;
    wrapper.replaceWith(p);
  }

  // Title page.
  const cover = document.createElement('div');
  cover.className = 'pdf-cover';
  cover.innerHTML = `<h1>${book.title}</h1><p>${book.stand}: ${today}</p><p>${book.online}: <a href="${homeURL}">${homeURL}</a></p>`;
  const first = document.querySelector('article');
  first.parentElement.insertBefore(cover, first);

  const style = document.createElement('style');
  style.textContent = `
    .pdf-cover { break-after: page; padding-top: 30vh; text-align: center; }
    .pdf-cover h1 { font-size: 2.6rem; margin-bottom: 2rem; }
    .pdf-tab-title { font-weight: bold; margin: .75rem 0 .25rem; padding: 0 .5rem; }
    .tab-content { display: block !important; }
    .pdf-embed { font-style: italic; }
    #R-topbar, .actionbar, .inline-copy-to-clipboard-button, .block-copy-to-clipboard-button { display: none !important; }
    code.copy-to-clipboard-code::after { display: none !important; }
    .quiz-solution, .quiz-score { display: none !important; }
    .mermaid, figure, img, tr { break-inside: avoid; }
    h1, h2, h3, h4 { break-after: avoid; }
  `;
  document.head.append(style);
}

const browser = await chromium.launch();
try {
  for (const book of BOOKS) {
    const homeURL = baseURL + book.dir;
    const page = await browser.newPage({ colorScheme: 'light' });
    await page.route('**/*', serveFromPublic);
    page.on('pageerror', (err) => console.warn(`[${book.lang}] page error: ${err.message}`));

    await page.goto(`${homeURL}index.print.html`, { waitUntil: 'load' });
    // Mermaid renders client-side; wait until every diagram has become an SVG.
    await page.waitForFunction(
      () => [...document.querySelectorAll('.mermaid')].every((el) => el.querySelector('svg')),
      null, { timeout: 60_000 },
    );

    const today = new Date().toLocaleDateString(book.lang === 'de' ? 'de-AT' : 'en-GB', { year: 'numeric', month: 'long', day: 'numeric' });
    await page.evaluate(prepareForPaper, { book, homeURL, today });
    await page.evaluate(() => document.fonts.ready);

    const out = path.join(publicDir, book.dir, book.file);
    await page.pdf({
      path: out,
      format: 'A4',
      margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
      printBackground: true,
      outline: true, // PDF bookmarks from the headings, the table of contents in any PDF viewer
      tagged: true,
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-size:8px;width:100%;padding:0 16mm;display:flex;justify-content:space-between;color:#666">
        <span>${book.title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
    });
    console.log(`[${book.lang}] ${path.relative(root, out)} (${((await stat(out)).size / 1024 / 1024).toFixed(1)} MB)`);
    await page.close();
  }
} finally {
  await browser.close();
}

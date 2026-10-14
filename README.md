Run coursbook via https://glandl.github.io/Coursebook-maker-reise-grade-9/

## PDF scriptum

On every deploy the workflow also renders the book into a PDF per language
(`kursbuch-informatik.pdf`, `en/coursebook-informatics.pdf`), linked in the menu.
The teacher section is left out. To build it locally:

```bash
hugo --gc
cd scripts/pdf
npm ci
npx playwright install --with-deps chromium   # once
node build-pdf.mjs                            # writes the PDFs into public/
```

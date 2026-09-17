# Progress log

Companion to `PLAN.md`. `PLAN.md` holds the settled design; this file tracks what has been built and what is open. Newest entry first.

---

## 2026-09-17 · P1 „Code & Gadget" weeks 2–7 written (issue #5)

**Goal:** finish the P1 exemplar: phase pages, board scaffolds, journal tasks, quiz, videos, DE + EN, and run the cost stress test.

### Content written (DE + EN mirror each, `content/projekte/p1-code-gadget/`)

| Week | Page | Phase | Content |
|------|------|-------|---------|
| 2 | `woche-02-anforderungen` | Kickoff → Sprint 1 | Python: types/`int()`/`float()`, `if`/`elif`/`else`, `while`/`for` (`thermostat.py`, `countdown.py`, `wuerfel.py`) · team + board choice table (with P2 Wi-Fi hint) · team repo `p1-gadget-<team>` · user stories + acceptance criteria + Muss/Soll/Kann → `ANFORDERUNGEN.md` · inputs→gadget→outputs Mermaid sketch · Kanban board, WIP limit, stand-up |
| 3 | `woche-03-board` | Sprint 1 | functions (`schalter_funktionen.py`), lists + modulo (`ampel_liste.py`, `messwerte.py`) · connect board in Thonny · blink + button toggles LED with edge detection (4 platform tabs) · `main.py` autostart |
| 4 | `woche-04-sensoren-review` | Sprint 1 → Review | **hardware layer `hardware.py`** per board (the only tabbed code from here on) · sensor + Thonny plotter, threshold · `nachtlicht_einfach.py` shows why states are needed · state diagram + flowchart (Mermaid, TB09 state-based *and* process-oriented) · **Sprint-Review 1** format |
| 5 | `woche-05-zustandsautomat` | Sprint 2 | **state machine recipe** (`naechster_zustand` = arrows only) on PC then board · hysteresis · dict transition table (pro) · reaction game with time as event · **TB06 experiment**: vary LED/tone/fixed wait, measure, explain, accessibility question |
| 6 | `woche-06-testen-doku` | Sprint 2 | `hardware.py` / `logik.py` / `main.py` split · `test_logik.py` on PC (one test per arrow) · `TESTS.md` device test report · code review checklist (teams swap, GitHub issues) · README template · 3-min presentation plan + Plan-B video |
| 7 | `woche-07-review-retro` | Review & Retro | presentations with feedback cards · Start/Stop/Continue retrospective · Journalauftrag 7 with self-assessment per P1 competency · submission checklist · 8-question final quiz · outlook P2 |

Each week has: goals box, minute-timed sections (100 min), Journalauftrag N, quiz, „Bis nächste Woche".

### New: quiz shortcode

`layouts/shortcodes/quiz.html` + `question.html`: multiple choice with instant feedback and score. Inner format: question / options (one per line) / explanation, separated by `---`; `correct="N"`. Without JavaScript and in the print view each question falls back to a collapsible solution. Build errors on a malformed question. **This is the quiz format for all later projects and Lernpfade.**

### Verification

- `hugo --gc` clean (DE 113 / EN 115 pages), all `relref`s resolve, no raw shortcodes in output.
- All YouTube IDs checked via oEmbed: `Kc-JmsKLPjs`, `cSkP6rYQ3U0`, `vYnprnrTWwU`, `P513uNckJF0`, `B1mMAieycPY`, `R7lZTvC9UUU`, `DaZF-3jM69U`, `HTlIg6IqNzA`, `59S53NSHR0M`, `nwmIg0ZYnF8`, `rqTMaD4FnFA`, `3NroZHXFihE`, `rWz9VsHSpAE`. All German; EN pages label them as such.
- Every Python snippet (DE and EN) syntax-checked. PC programs run with sample input. Board programs run against **mock** `machine`/`microbit`/`music` modules for micro:bit, Pico and ESP32 (all `hardware.py` × `sensor_test`/`nachtlicht`/`main`/`reaktion` combinations, including real reaction-game hits). **Not tested on physical boards**: pin choices (Pico GP14/15/16/26, ESP32 GPIO 4/18/19/34), PWM buzzer volume, micro:bit light-level reading while the display is lit.
- Kompetenzmatrix: TB02 (9), TB06 (10), TB09 (9) → 🟢. TB04 stays 🟡 (network part in P2).
- P1 brief end-product list updated (flowchart, file structure, tests).

### Stress test (PLAN.md §8)

- Platform tabs ≈ **10 %** of P1 DE words (1,120 of 11,384). Only weeks 1, 3, 4 have tabs. The `hardware.py` pattern keeps weeks 5–7 platform-free.
- EN mirror = **+100 %** words (23.7k total). Every correction made during this session had to be applied twice.
- Real cost of 4 platforms: hardware verification and teacher support, not writing.
- Recommendation recorded in PLAN.md §8, **decision pending**.

### Deliberately not done (other issues)

- `werkzeuge/micropython-boards` and `wokwi-simulator` are still stubs, but weeks 3–4 link to them for drivers, pinouts, Arduino R4/Nano pin mapping (**issue #4, needed before week 3**).
- Kanban/Sprint method page (issue #3). Week 2 explains Kanban inline for now; move it to the method page later and link back.
- Teacher Verlaufspläne weeks 2–7 (issue #7) and rubric templates (#8), which week 7 links to.
- Leftover empty stub `content/projekte/p1-code-und-gadget/` still exists (see previous entry).

Committed and pushed to `master` at the end of this session (triggers the Pages deploy); **issue #5 closed**. The stress-test question (EN full mirror vs. partial) stays **open for decision** in PLAN.md §8.

### Next steps (in order)

1. Decide the stress-test question (EN full vs. partial) before P2 is written.
2. Issue #4: MicroPython boards + Wokwi guides (week 3 depends on them).
3. Issue #3: Kanban/Sprint method page; replace the inline Kanban section in week 2 with a link.
4. Issue #7: Verlaufspläne weeks 2–7.
5. Build hardware test: run weeks 3–5 code once on a real micro:bit, Pico and ESP32.
6. Check the Mermaid diagrams in a browser on the deployed site (state diagrams and flowcharts were only verified as rendered blocks, not visually).

---

## 2026-09-17 · Kompetenzmatrix published (issue #2)

**Goal:** verify the v0.1 draft matrix against the full Excel wording and publish `lehrkraefte/kompetenzmatrix` (DE + EN).

- Local `master` was 2 commits behind `origin/master` (the Pages deploy workflow had been fixed and pushed directly on GitHub on 2026-09-16, switching to a `gh-pages`-branch build; site is live and green at https://glandl.github.io/Coursebook-maker-reise-grade-9/). Fast-forwarded to sync. Issue #1 is functionally done but still open on GitHub — not closed yet, pending confirmation.
- Extracted all cell text from `planning/LP-Informatik-Sek2-v1.3-nachBegutachtung.xlsx`, sheet `PF-NachBegutachtung-V1` (sheet 2), by parsing the OOXML directly (no `openpyxl` available locally). Full extraction confirms **27 competencies** (9 per grade 9/10/11 by actual row count; the sheet's own header claims 9/9/8).
- Corrections found versus the v0.1 draft: **TB04** grade was 9–11 → actually **10 only**; **TB06** was 9/10 → actually **10/11**; **TB07** was 9–11 → actually **10 only**; **TB09** was 9–11 → actually **9 only**; **TB05** 2nd competency was 10/11 → actually **11 only**; **TB02** "Laufzeitabschätzungen" was listed as grade 10 → actually **11** (same column as "Programmcode verbessern/korrigieren", both grade 11). **TB11** previously merged two different competencies (grade-9 "Berufsfelder der Informatik" and grade-11 "ethisch/inklusive Systemgestaltung") into a single grade-11 row — split into two correct rows.
- Also found: **Themenbereich 04 has no title** in the source document (row is blank), only its competency text is filled in.
- Published `content/lehrkraefte/kompetenzmatrix.de.md` and `.en.md`: curriculum wording (footnote reference numbers like ".6, 7, 9, 13" stripped for public readability — see notes file), grade/semester, covered-by (P1–P5 / Selbstlernen link), status icon (🟡/🔴) per row, plus a coverage-count summary table (P1: 4, P2: 3, P3: 5, P4: 4, P5: 5, Selbstlernen: 6 = 27). TB04 (no title in the source) is published under the working title **"Computersysteme" / "Computer Systems"**. The source is referred to on public pages as **"Lehrplan für Informatik und KI"**, never by the xlsx filename.
- Source-verification detail (row-count discrepancy, grade corrections, TB02/TB11 merge fix, footnote-number handling, full raw extraction) moved to a new **`planning/KOMPETENZMATRIX-NOTES.md`** — internal only, not published on the site.
- Backfilled the corrected mapping into `planning/PLAN.md` §4 (bumped to v1.0), and marked roadmap steps 1–2 done in §7.
- `hugo --gc` build is clean (95 DE / 97 EN pages), all `relref` links in the new page resolve.
- **Not yet done:** committing/pushing this change, and closing issue #2 on GitHub — both need explicit confirmation first.

### Next steps (in order)

1. Commit + push the Kompetenzmatrix + PLAN.md v1.0 changes; close issue #2 once the user confirms.
2. Decide fate of the leftover empty stub `content/projekte/p1-code-und-gadget/` (duplicate of `p1-code-gadget`, unused, never linked) — looks like dead content from an early naming decision.
3. Week 2 student page + Verlaufsplan: team & board choice, requirements, Kanban page (issue #3).
4. Continue P1 weeks 2–7 (issue #5) to finish the exemplar project format.
5. One-page briefs P2–P5 (issue #6).

---

## 2026-09-15 · Session 1 materials (P1 Kickoff) built

**Goal of the day:** everything needed to teach the first double lesson (100 min net) of P1 „Code & Gadget".

### Decisions taken today (also recorded in PLAN.md §3 and §6)

| Topic | Decision | Reason |
|-------|----------|--------|
| IDE | **Thonny for P1–P2, VS Code from P3** | Thonny: bundled Python, portable/no-admin install, built-in MicroPython flashing + REPL for Pico/ESP32, beginner debugger, no AI autocomplete. VS Code wins for notebooks/SQL (P3–P4) and web + Git (P5). |
| Lernjournal format | **Markdown files in a private GitHub repo per student**, one file per project week, plus `selbstlernen/` and `images/` | Progress visible continuously through commits; nothing „handed in" at the end; feeds P5. |
| Journal distribution | **Classroom 50** (Fifty Foundation, classroom50.org) with a template repo `lernjournal-vorlage`. **GitHub Classroom is retired (2026-08-28), do not use.** | Private repo per student in the school org, submissions page shows latest push per student. Plan B: self-created private repo + teacher as collaborator. |
| Week 1 content | Includes a short **Markdown + GitHub-in-the-browser** block; local Git deferred until teams share code | Journal starts on day one. |
| Methods placement | Lernjournal page lives as intro page under *Projekte* (issue 3, journal half). Kanban page still open. | |

### Content written (DE + EN mirror each)

| Page | Path | Status |
|------|------|--------|
| P1 project brief | `content/projekte/p1-code-gadget/_index` | done: goal, end product, competencies with exact Excel wording, 7-week phase table, tools |
| P1 Week 1 student page | `content/projekte/p1-code-gadget/woche-01-kickoff` | done: Maker-Reise intro, Thonny check, `hallo.py` + `schalter.py` (state idea), `ampel.py` for fast/at home, board tabs (micro:bit/Pico/ESP32/Arduino) as preview, GitHub + Markdown block, Journalauftrag 1, self-check, homework, 2 verified YouTube embeds |
| Lernjournal method page | `content/projekte/lernjournal` | done: repo structure, entry template, rules, when it is looked at |
| Thonny setup | `content/werkzeuge/python-thonny` | done: OS tabs + browser fallback, first start, buttons, 2 verified videos, note on VS Code from P3 |
| Git & GitHub | `content/werkzeuge/git-github` | done for week 1 (browser only): account, repo via Classroom 50 or self-created (tabs), edit/preview/commit, new file with folder, image upload. Local Git section is a placeholder. |
| Markdown cheat sheet | `content/werkzeuge/markdown` | done (new page, weight 5) |
| Teacher lesson plan week 1 | `content/lehrkraefte/verlaufsplaene/woche-01` | done: goals, two-stage prep list (Education/Team plan, Classroom 50 setup, template repo content), minute table, differentiation, pitfalls, homework, evidence + weekly commit-check routine |
| Verlaufspläne section index | `content/lehrkraefte/verlaufsplaene/_index` | done (new section for future weeks) |

Verified externals: YouTube IDs `oxXAb8IikHM` (Python erstes Programm), `k7CLrRkzC5o` (Thonny), `93J6Sxk55mg` (Thonny UI), `SF_Ym8fWTPU` (micro:bit) checked via oembed. Classroom 50 workflow taken from its wiki (Web Student Guide, Web Teacher Guide, Prerequisites, Known Limitations).

Hugo build: clean. **Nothing committed yet** (working tree only).

### Session 1 timing (100 min)

| Min | Phase |
|-----|-------|
| 0–10 | Maker-Reise intro, boards passed around |
| 10–25 | Thonny tool check |
| 25–55 | `hallo.py`, `schalter.py`, screenshot; fast: `ampel.py` |
| 55–60 | Break |
| 60–75 | GitHub account, usernames → roster, Classroom 50 accept |
| 75–85 | Markdown in 5 min, first commit (README) |
| 85–98 | Journalauftrag 1 as `p1/woche-01.md`, commit |
| 98–100 | Outlook, homework |

### Teacher prep before lesson 1 (from the Verlaufsplan)

- [ ] **Now:** apply for GitHub Education teacher verification (takes up to 2 weeks).
- [ ] Create school/class GitHub organisation, upgrade to **Team plan** with the Education benefit.
- [ ] Classroom 50: set up organisation (service token), create classroom (short slug), create `lernjournal-vorlage` template repo, create individual private assignment `lernjournal` (not graded, no due date).
- [ ] Decide username convention with the class (no real-name requirement; GitHub minimum age 13).
- [ ] Check that GitHub confirmation mails pass the school mail filter; Plan B: allow private addresses.
- [ ] Thonny on all school PCs, `input()` works in the shell.
- [ ] Hardware showcase set (micro:bit, Pico, ESP32, Arduino, 2–3 finished mini gadgets).

### Findings for open issues

- **Issue 2 (Kompetenzmatrix):** in Excel sheet 2 the TB 04, TB 06 and TB 07 competencies sit in the **10th-grade** column, not 9th as the PLAN.md v0.1 matrix assumes. P1 brief uses the Excel grades; the matrix page still needs the correction.
- **Issue 3 (Methoden):** Lernjournal half done. Kanban/Sprints page and optional methods (pair programming, Jigsaw) still open; needed by week 2.
- **Issue 4 (Werkzeuge):** Thonny and Git (week-1 scope) done, Markdown added. MicroPython boards and Wokwi still stubs; needed by week 3.
- **Issue 5 (P1):** brief + week 1 done. Weeks 2–7, scaffolds for boards, quiz beyond self-check, cost stress test still open.
- **Issue 1 (Pages):** workflow exists; first push will trigger deploy.

### Next steps (in order)

1. Commit + push the session 1 set (closes issue 1 on first deploy).
2. Week 2 student page + Verlaufsplan: team & board choice, requirements, Kanban page (issue 3).
3. `werkzeuge/micropython-boards` and `wokwi-simulator` before week 3 (issue 4).
4. Kompetenzmatrix page with corrected grade columns (issue 2).
5. One-page briefs P2–P5 (issue 6).

# Progress log

Companion to `PLAN.md`. `PLAN.md` holds the settled design; this file tracks what has been built and what is open. Newest entry first.

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

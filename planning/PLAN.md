# Coursebook Informatik — Master Plan

**Status:** agreed 2026-09-15 (grilling session) · **Owner:** Gerald Landl
**Scope:** One regular 9. Schulstufe class covers the full 3-year Informatik curriculum (9.–11. Schulstufe) in **one school year at 2 h/week** (~32–34 double lessons), project-driven, backed by a Hugo course book.

---

## 1. Source of truth

- **Only** sheet `PF-NachBegutachtung-V1` (sheet 2) of `planning/LP-Informatik-Sek2-v1.3-nachBegutachtung.xlsx` is authoritative: **11 Themenbereiche, 27 competencies** (9 per grade 9/10/11; the sheet's own header says 9/9/8, the actual row count is 9/9/9 — verified 2026-09-17, see issue #2).
- Sheet 1 is marked outdated — never use it (background reference at most).
- Coverage must be **formally defensible**: every competency is traceably mapped to a project or a self-study path in a **Kompetenzmatrix** (published in the Lehrkräfte section).

## 2. Compression strategy

3 year-hours are compressed into 2 year-hours (⅓ time deficit). Strategy: **projects + self-study**.

- **Core competencies** are taught inside 5 medium projects (6–8 weeks each).
- **Remaining competencies** become **Selbstlern-Lernpfade**: curated links and videos + one journal task + one self-check quiz per chapter. The book does **not** rewrite textbook theory — theory is link-based.
- The book's own written material is limited to: project briefs and phase instructions, **code scaffolds**, tool setup guides, learning-path curation, and teacher pages.
- Self-study evidence: **journal task per chapter** (checked in the Lernjournal during projects) + **quizzes embedded in the book**.

## 3. The year: „Maker-Reise" (5 projects)

| # | Project | Duration | Themenbereiche (primary) | Idea |
| --- | --------- | ---------- | -------------------------- | ------ |
| P1 | **Code & Gadget** | ~7 weeks | TB 02, 04, 06, 09 | Python-Grundlagen; ein interaktives Gerät am Einplatinenrechner bauen (Zustandsautomat, Sensoren/Aktoren, Peripherie) |
| P2 | **Wetterstation / IoT** | ~7 weeks | TB 04, 05, 01, 11 | Sensoren vernetzen, Daten erfassen → speichern → analysieren; Netzwerkgrundlagen; Energie & Nachhaltigkeit |
| P3 | **KI-Labor** | ~7 weeks | TB 03, 01, 11 | Entscheidungsbäume, Perzeptron/ML-Verfahren, neuronale Netze, generative KI; EU AI Act, gesellschaftliche Teilhabe |
| P4 | **Datendetektive** | ~6 weeks | TB 01, 10 | SQL & Datenmodellierung; Verschlüsselung, DSGVO-Sphären, OSINT & Datenfußabdruck |
| P5 | **Web-Portfolio** | ~7 weeks | TB 08, 07, 05 | Agil entwickelte Website als Showcase aller Projekte; Anforderungen; client-/serverseitig; netzbasierte Dienste |

Rhythm per project: **Kickoff/Anforderungen → Sprints (Bauen) → Review/Präsentation → Retrospektive + Journal-Abgabe.**

### Methods (recurring rituals, explained once in the book)

- **Mandatory:** Agile-lite (Team-Kanban, Sprints, Sprint-Review = Zwischenpräsentation — also covers the „agile Methoden" competency of TB 08) and **Portfolio/Lernjournal** (feeds P5 and evidence of self-study).
- **Lernjournal format (decided 2026-09-15):** Markdown files in a **private GitHub repository per student** (via **Classroom 50** by the Fifty Foundation, since GitHub Classroom was retired 2026-08-28; needs the org on the Team plan via GitHub Education; template repo `lernjournal-vorlage`; Plan B: self-created private repo + teacher as collaborator), one file per project week plus `selbstlernen/` and `images/`. Progress is visible continuously through commits, nothing is "handed in" at the end. Week 1 of P1 therefore contains a short Markdown + GitHub-in-the-browser introduction; local Git follows when teams share code.
- **Optional per project:** Pair-Programming-Rotationen (Driver/Navigator), Gruppenpuzzle/Jigsaw (z. B. ein Sensortyp pro Expert:innengruppe).

## 4. Kompetenzmatrix v1.0 (verified against full Excel wording 2026-09-15/17, issue #2; full text published at `lehrkraefte/kompetenzmatrix`)

27 competencies (9 per grade 9/10/11 by row count — the sheet's own header says 9/9/8, see issue #2 finding). Corrected vs. the earlier v0.1 draft: **TB04** (was 9–11, is **10**), **TB06** (was 9/10, is **10/11**), **TB07** (was 9–11, is **10**), **TB09** (was 9–11, is **9**), **TB05** 2nd row (was 10/11, is **11**), **TB02** "Laufzeitabschätzungen" (was 10, is **11**), **TB11** split into two 9th-grade rows (Nachhaltigkeit and Berufsfelder, previously merged into one row).

| TB | Competency (short) | Grade col. | Covered by |
| ---- | -------------------- | ------------ | ----------- |
| 01 | Weg der Daten: Erfassung → Analyse untersuchen | 9 | **P2** |
| 01 | Datenmodellierung, Abfragen, Daten aus Beständen gewinnen (SQL) | 10 | **P4** (Daten für ML auch in P3) |
| 02 | Algorithmen in textbasierter Sprache umsetzen | 9 | **P1** |
| 02 | Algorithmen mit geeigneten Datenstrukturen implementieren | 10 | **Selbstlernen** + Praxis in P3/P4 |
| 02 | Programmcode analysieren, verbessern/korrigieren | 11 | **Selbstlernen** + Code-Reviews in allen Projekten |
| 02 | Laufzeitabschätzungen, rekursiv/iterativ vergleichen | 11 | **Selbstlernen** |
| 03 | Einfache KI-Modelle (Entscheidungsbäume, Klassifikation) erstellen/bewerten | 9 | **P3** |
| 03 | ML-Verfahren (Perzeptron, unüberwacht) schrittweise nachvollziehen | 10 | **P3** |
| 03 | Neuronale Netze & generative KI erklären, Auswirkungen | 11 | **P3** |
| 03 | KI-Anwendungsbereiche vergleichen, Verfahren begründen | 11 | **P3** |
| 04 | Rechnersysteme mit Peripherie, Sensoren/Aktoren, Netzwerkkonfiguration in Betrieb nehmen | 10 | **P1** (Gerät) + **P2** (Netzwerk) |
| 05 | Lokale Netzwerke, einfache Protokolle, Gerät einbinden | 9 | **P2** |
| 05 | Stufenmodell, netzbasierte Dienste, zustandslos/verbindungsorientiert | 11 | **P5** (Vertiefung: Selbstlernen) |
| 06 | Einfache interaktive Systeme bauen, Systemverhalten variieren | 10 | **P1** |
| 06 | Interaktionsformen beschreiben und vergleichen | 11 | **Selbstlernen** |
| 07 | Anforderungen in natürlicher Sprache und einfachen grafischen Notationen nachvollziehen | 10 | **P5** (geübt ab P1-Kickoff) |
| 08 | Digitale Artefakte: Form/Inhalt-Trennung, geistiges Eigentum, CC | 9 | **P5** (Journal ab P1) |
| 08 | Multimediale Artefakte, Inklusion, Prinzipien begründen | 10 | **P5** |
| 08 | Webbasierte Anwendungen, client-/serverseitig, agile Methoden | 11 | **P5** |
| 09 | Zustandsbasiert und ablauforientiert abstrahieren/modellieren | 9 | **P1** |
| 10 | Sphären der Privatheit, DSGVO, eigenes Verhalten begründen | 9 | **P4** |
| 10 | Symmetrische/asymmetrische Verschlüsselung, Authentifizierung | 10 | **P4** |
| 10 | OSINT, Datenfußabdruck | 11 | **P4** |
| 11 | Energie-/Ressourcenverbrauch, nachhaltige Gestaltung | 9 | **P2** |
| 11 | Berufsfelder der Informatik | 9 | **Selbstlernen** |
| 11 | Digitale Infrastrukturen, Teilhabe, EU-Gesetzgebung zu KI | 10 | **P3** |
| 11 | Ethisch/inklusive Systemgestaltung | 11 | **Selbstlernen** + Reflexion in P3/P5 |

**Selbstlern-Lernpfade (initial set):** Datenstrukturen · Laufzeit & Algorithmenanalyse · Code-Qualität/Refactoring · Interaktionsformen (MMI) · Stufenmodell-Vertiefung · Berufsfelder & Ethik.

## 5. Assessment

**Deferred by decision.** The book ships **rubric templates only** (project product/process/presentation, Lernjournal). The concrete grading scheme is defined later by the teacher.

## 6. Technology & book format

| Decision | Choice |
| ---------- | -------- |
| Framework | Hugo + **Relearn** theme |
| Hosting | **GitHub Pages** via GitHub Actions |
| Languages | Bilingual, **German leads, English full mirror** (Hugo multilingual, language switcher) |
| German style | Doppelpunkt: **Schüler:innen**; students addressed as „du" in instructions |
| Breaks | **Never planned in the book** (decided 2026-09-23). Student pages and Verlaufspläne contain no break section or row; when a break happens and how long it lasts is the teacher's decision. A double lesson is therefore planned as **95 min of content**, the rest is slack. |
| Must-have content features | Syntax-highlighted code snippets, YouTube embeds (built-in shortcode), resource links, **tabbed code blocks per platform**, callouts, search, print/offline view |
| Programming spine | **Python everywhere** (PC: Python; Boards: MicroPython) |
| IDE | **Thonny for P1–P2** (bundled Python, portable/no-admin install, built-in MicroPython flashing/REPL for Pico & ESP32, beginner debugger, no AI autocomplete). **VS Code from P3** (notebooks/pandas/SQL in P3–P4, HTML/CSS/JS + Git in P5). Decided 2026-09-15. |
| Hardware | micro:bit, Raspberry Pi/Pico, Arduino, ESP32 — **all equal, student choice**; per-platform instructions as tabs. Arduino-UNO fallback: Wokwi simulator / ESP32, C++ appendix if needed |
| Student devices | School PCs (install rights) + BYOD; browser tools (Wokwi, micro:bit editor, …) as universal fallback |

### Site structure (projects-first)

```
Start          — Jahresüberblick, Maker-Reise-Landkarte
Projekte       — P1 … P5: Phasen, Code-Scaffolds, Links, Videos
Selbstlernen   — Lernpfade: Links/Videos + Journalauftrag + Quiz
Werkzeuge      — Setup-Guides: Thonny, MicroPython, Wokwi, Boards, Git …
Lehrkräfte    — Kompetenzmatrix, Wochenraster/Timing, Rubrik-Vorlagen
```

Teacher section is **public** (deliberate decision), just a separate menu branch.

## 7. Build roadmap

1. **Skeleton:** Hugo + Relearn, DE/EN multilingual config, GitHub Actions → GitHub Pages, full navigation with stub pages. ✅ done, site live at [https://glandl.github.io/Coursebook-maker-reise-grade-9/](https://glandl.github.io/Coursebook-maker-reise-grade-9/)
2. **Kompetenzmatrix** page (from §4, verified against the full Excel texts). ✅ done 2026-09-17, see `lehrkraefte/kompetenzmatrix`
3. **P1 „Code & Gadget" fully written** — the exemplar that defines the format (phases, scaffolds, platform tabs, journal tasks, quiz). 🟢 student pages done 2026-09-17 (weeks 1–7, DE + EN, issue #5). Still open outside #5: board setup guide (#4), Kanban method page (#3), teacher lesson plans (#7: week 2 done 2026-09-23, weeks 3–7 open), classroom test on real hardware
4. **One-page briefs for P2–P5** so the whole year is visible from day one.
5. Then project by project: P2 → P3 → P4 → P5 + matching Selbstlern-Lernpfade, validated in class as the year progresses.

## 8. Known risks

- **Cost multiplier:** „all 4 platforms equal" × „EN full mirror" multiplies writing effort. P1 is the stress test — if too heavy, downgrade to *one primary platform + extension tabs* and/or *EN partial* (both cheap to change after the exemplar).
  - **Stress test result (P1, 2026-09-17):** platform tabs are only **~10 %** of P1's words (weeks 1, 3, 4; weeks 5–7 have none), because from week 4 all board-specific code lives in one `hardware.py` per board and the gadget code is shared. The Arduino tab has already become a pointer (UNO R4/Nano ESP32 → ESP32 code, UNO R3 → Wokwi). The **EN mirror is the real multiplier: +100 %** of words (DE 11.4k → DE+EN 23.7k), and every later correction has to be made twice. The hidden cost of 4 platforms is not text but **verification and classroom support**: the board code was only tested against mock modules, not on real hardware, and the teacher has to support 3–4 wiring setups.
  - **Recommendation (decision pending):** keep all 4 platforms, with the rule "tabs only for `hardware.py` and first contact; Arduino = pointer tab". For EN, decide between keeping the full mirror and *EN partial* (briefs, tool guides and Kompetenzmatrix in EN, week pages DE only).
- **Defensibility depends on the matrix:** resolved — the full-text matrix (§4 v1.0, published at `lehrkraefte/kompetenzmatrix`) is verified against the Excel wording.
- **Sequential compression trap:** resist drifting back into teaching 9./10./11. content in sequence; the projects must genuinely merge the spiral.

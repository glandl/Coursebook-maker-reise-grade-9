# Baupläne · P1 Code & Gadget

Individual build instructions for each P1 team, derived from its User Stories. Terms are defined in [`../CONTEXT.md`](../CONTEXT.md). Decided in the grilling session of 2026-11-09.

## Folder layout

```
bauplaene/
  README.md              ← this file: process, demand table, review checklist
  schaltplan.py          ← draws every team's schaltung.svg (python3 schaltplan.py, no dependencies)
  4a-t1/
    ANFORDERUNGEN.md     ← anonymised copy of the team's original stories (input)
    BAUPLAN.md           ← drafted here, reviewed by the teacher, copied into the team repo
    schaltung.svg        ← wiring picture, embedded in K1; generated, copied along with BAUPLAN.md
  4a-t2/ …
```

## Anonymisation (before anything is committed, this repo is public)

- Folder and file content use the **Team-Kürzel** (`4a-t3`), never the team's own name.
- No student names, GitHub handles, repo URLs or photos.
- Identifying details in stories are generalised ("for my brother Jonas" → "for a younger sibling").
- Every file is checked again for names and handles before it is committed.

## Process

1. Teacher adds all `ANFORDERUNGEN.md` (anonymised) and the parts list (stock).
2. Demand table below: Bausteine needed per team, weak stories, unrealistic Muss stories. **Stop:** the teacher decides cuts and simplifications once, for all teams.
3. Write the Bausteine (Werkzeuge → Bausteine, DE first, Pico 2 W only, see [ADR 0001](../adr/0001-bausteine-pico-2-w-only.md)), most in-demand first.
4. Write the Baupläne, one class at a time.
5. Teacher reviews each Bauplan with the checklist below and copies it, together with `schaltung.svg`, into the team repository.

## Structure of a Bauplan

1. **Unsere User Stories (überarbeitet):** Muss stories only (at most 3), corrected story sentence, checkable acceptance criteria, and a *Was wir geändert haben* note per story. Step 1 for the team: copy them into their `ANFORDERUNGEN.md`.
2. **Karten für euer Kanban-Board:** table with Karte · Story · braucht vorher · fertig, wenn … (each "fertig, wenn" points to an acceptance criterion). Includes the standard week 6 cards (`TESTS.md`, README, presentation). No names, no dates: the team decides who and when; everything is due by the end of week 6.
3. **Anleitungen pro Karte:** steps, link to the Baustein, and for team-specific code a Gerüst with `# TODO` gaps and Tipp-Stufen (`<details>`: Tipp 1 → Tipp 2 → Lösung).
4. **Wenn ihr schneller seid:** Soll/Kann stories, optional.

## Demand table

*(filled in once the stories and the parts list are in)*

| Team | Gadget | Muss stories | Bausteine needed | Story problems | Cut / simplification (teacher decision) |
|------|--------|--------------|------------------|----------------|------------------------------------------|

## Review checklist (teacher, per Bauplan)

- [ ] No names, handles or repo URLs.
- [ ] At most 3 Muss stories; Soll/Kann only under "Wenn ihr schneller seid".
- [ ] Every acceptance criterion can be checked by an outsider (numbers instead of "fast", "loud").
- [ ] Every Karte's "fertig, wenn" matches an acceptance criterion.
- [ ] "braucht vorher" has no cycles and at least one Karte can start immediately.
- [ ] Every Baustein link resolves; all pins follow the Kurs-Verkabelung.
- [ ] `schaltung.svg` matches the wiring tables in K1/K2 (pins are physical Beinchen numbers in `schaltplan.py`, not GP numbers).
- [ ] All required parts are in stock.
- [ ] Realistic for two double lessons plus homework.

+++
title = "Week 2 · Team, Requirements, Kanban"
weight = 2
+++

**Student page:** [P1 Week 2 · Team, Requirements, Kanban]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}) · **Duration:** double lesson · 95 min planned, the remaining time stays free

This lesson has two halves: a **Python workshop** (variables, conditionals, loops) and the **project start** (team, board, requirements, Kanban). **Sprint 1** begins with this lesson (weeks 2–4) and ends with the sprint review in week 4.

## Lesson goals

- Everyone can convert input with `int()`/`float()`, branch with `if`/`elif`/`else` and repeat with `while` and `for` (TB 02, grade 9).
- Everyone is in a team of 2–3, every team has chosen a board and created a private team repository.
- Every team has a `REQUIREMENTS.md` with 3–5 **user stories** including acceptance criteria and an inputs → gadget → outputs sketch (preview of TB 07, grade 10: requirements in natural language and simple graphical notations).
- Every team has a Kanban board with a filled "sprint 1" column and knows the WIP limit and the stand-up (preview of the agile methods in TB 08).
- Journal task 2 is begun and committed.

## Before the lesson: commit check

This is routine from now on (see [week 1]({{% relref "lehrkraefte/verlaufsplaene/woche-01" %}})): open the assignment's submissions page in Classroom 50 (reload the page!) and check who has pushed `p1/woche-01.md`.

- [ ] Note who has **no commit**. This week the most common reason is not unwillingness but an **unfinished account** (confirmation email, username, roster entry).
- [ ] Plan catch-up for those people: add them to the roster and re-upload, send the assignment link again. During the lesson an advanced student can take this over in the Python phase (see differentiation).
- [ ] Skim the gadget ideas in the journal entries. Note two or three workable ones — you will need them in phase 3 for a team without an idea of its own.

## Preparation

### Technology
- [ ] Book page week 2 open on the projector, plus an empty Thonny with the shell visible.
- [ ] Run `thermostat.py` and `countdown.py` yourself once, including the deliberate error (entering `warm` → `ValueError`). You want to be able to read the message out loud.
- [ ] GitHub reachable from the school network (as in week 1). The browser is enough for the team repositories, **no local Git**.
- [ ] Optional: a finished example `REQUIREMENTS.md` (night light, as on the student page) in a repo of your own, to show Mermaid rendering live on GitHub.

### Hardware stock
- [ ] **Count beforehand** and write on the board how many micro:bit, Pico/Pico W, ESP32 and Arduino are actually available, including cables and breadboards. Without that number every team picks the board with the coolest name.
- [ ] Decide and announce the allocation rule in advance, e.g. "one board per team, first come first served, ESP32 only for teams whose gadget is meant to go online later".
- [ ] Without enough hardware: point teams to [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) or the micro:bit simulator. This is not a second-class fallback — from week 3 the whole sprint works with it.

### Kanban material
- [ ] Sticky notes (two colours: story and task), thick markers, one poster or a section of the wall board with four columns per team.
- [ ] Settle storage: posters stay in the room (cupboard, back wall). Otherwise the board is gone next week.
- [ ] Announce: **photo of the board into the team repository at the end of the lesson.** That is the evidence, whether the board is paper or a GitHub Project.

### Organisation
- [ ] Prepare a **team list** (table on the projector or on paper) that you fill in during the lesson:

  | Team | Members | Gadget (one sentence) | Board | Repo URL |
  |------|---------|-----------------------|-------|----------|

  You need the repo URLs for the weekly check and for the review in week 4.
- [ ] Decide whether you want to be a **collaborator** in every team repository. Recommendation: yes, otherwise you will not see the teams' work until week 4.
- [ ] Be ready to announce the sprint 1 deadline: **review in week 4**. Everything that lands in the "sprint 1" column has to be demonstrable there.

## Flow

| Time | Phase | Teacher | Students | Material |
|------|-------|---------|----------|----------|
| 0–5 | **Look back** | Sprint logic in two sentences: sprint 1 starts today, review in week 4. Set up the pair work: show gadget ideas, question "which idea has the clearest inputs, outputs and states?" | Show week 1 journal entries in pairs | Projector, book page |
| 5–20 | **Python A: variables & conditionals** | Type `thermostat.py` on the projector, do not paste it. Explain `float(input(...))`. Then deliberately enter `warm` and read the traceback together: **last line first**, then the line number. Individual/pair work on the two modification tasks. | Type the program, try it, tasks 1 and 2 | PCs, Thonny |
| 20–35 | **Python B: loops** | Short stop: contrast `while` (condition) with `for` (count) on the board, stress `range(3)` → 0, 1, 2 explicitly. Run `countdown.py`, repeat the stop button. Circulate, send fast students to `dice.py`. | `countdown.py`, modification tasks; fast ones: `dice.py` | PCs, book page section 2 |
| 35–50 | **Team & board** | Show the hardware stock on the board, walk through the board table in 3 min (strengths, not pinouts), mention P2/WLAN. Let teams form, **timer set to 8 min**. Then fill in the team list on the projector. Assign anyone left over yourself, do not let it be discussed. One person per team creates the private repo `p1-gadget-<teamname>` and invites the team plus the teacher as collaborators. | Form team, choose board, create repo, accept invitations | Board (stock), Git guide part 2, team list |
| 50–75 | **Requirements** | User story template on the board: **As … I want … so that …**. Formulate **one** story for an example gadget together plus two acceptance criteria, replacing "fast" with "within 1 s". Explain must/should/could. Show a Mermaid block live on GitHub once. Then team work: circulate and **look at every team once**, checking that the stories describe behaviour, not components. | `REQUIREMENTS.md` in the team repo: gadget sentence, sketch, 3–5 stories with priority and criteria | Book page section 4, example repo |
| 75–85 | **Kanban** | Four columns on the board, break one must-story from a team into three cards together ("connect LED", "print sensor value", "find threshold"). Announce the WIP limit and the stand-up — the stand-up opens every lesson from week 3. Let them write cards and fill the sprint 1 column. At the end: photo into the repo. | Build the board, write cards, select sprint 1, upload photo | Sticky notes, markers, posters |
| 85–95 | **Journal task 2 & outlook** | Show the template on the projector, have `p1/woche-02.md` created, dictate the commit message. Last 2 min: outlook on week 3 (functions, lists, putting the board into operation), name the homework. | Write the entry, commit | Journal task 2 |

## Differentiation

- **Fast:** `dice.py` counting the sixes; Kanban digitally as a GitHub Project instead of paper; sharpen acceptance criteria with measurable numbers; use them as helpers for the week 1 stragglers (account, roster, first commit).
- **Slow:** modification task 1 is enough for `countdown.py`. In the requirements phase **two** must-stories with one criterion each are enough; the sketch may be drawn by hand and photographed instead of written as Mermaid.
- **Team without an idea:** offer your two or three prepared ideas (reaction game, dice, night light). These teams start with a ready-made story from the book example and only write the remaining ones themselves.
- **Prior knowledge:** require these teams to slice their stories so that each one can be finished in a single lesson — that is the genuinely hard exercise and costs them more thinking than the Python part.

## Typical pitfalls

- **Team formation eats the lesson.** Hard limit: 8 min with a visible timer. Anyone without a team when it runs out gets assigned. Announce that assignment will happen *before* the timer starts.
- **Everyone wants the ESP32.** Stock numbers and the allocation rule go on the board before the choice, not after.
- **Team repo accidentally public.** Point explicitly at **Private** while creating it. Changeable afterwards under *Settings → General → Danger Zone*.
- **Collaborator invitation not accepted.** Those invited must confirm the link in the email or the notification on GitHub, otherwise they cannot write. Ask once during the lesson: "can everyone in your team create a file in your repo?"
- **Stories that are really tasks** ("connect the buzzer to pin 15"). Counter-question: *who* wants this, and *what for*? If there is no answer, it is a Kanban card, not a story.
- **Acceptance criteria without measurability** ("reacts fast", "works well"). Leave the rule on the board: a stranger must be able to check the criterion without asking you.
- **Mermaid does not render:** the block needs the line ```` ```mermaid ````, and it is only rendered on GitHub, not in Thonny or a local editor.
- `input()` returns text — `TypeError` when calculating. This will happen; use it to practise reading tracebacks (it is also a quiz question on the student page).
- **`=` instead of `==`** in a condition. Produces a `SyntaxError`; clear it up for everyone on the board the first time it appears.
- **Off-by-one with `range`:** `range(3)` stops **before** 3, `range(start, 0, -1)` stops at 1. Count it out on the board once explicitly.
- **`while` loop without an exit** blocks Thonny. Show the stop button again, as in week 1.

## Homework

- Finish `REQUIREMENTS.md` as a team, fill the Kanban board with cards for sprint 1.
- Commit journal task 2 (`p1/woche-02.md`) if it was not finished in the lesson.
- If you have hardware at home: read [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}}) and connect the board to Thonny. Without hardware: open [Wokwi]({{% relref "werkzeuge/wokwi-simulator" %}}) or [python.microbit.org](https://python.microbit.org/).

## Evidence and progress check

There are **two** pieces of evidence this week:

1. **Individual:** the commit to `p1/woche-02.md` in the learning journal — checkable on the submissions page as usual.
2. **Team:** `REQUIREMENTS.md` and the board photo in the team repository. Put the repo URLs into your team list and look into each repo once before week 3.

If a team has no `REQUIREMENTS.md`, that team starts week 3 with it instead of with the board. Without requirements there is nothing in week 4 for the review to measure "finished" against.

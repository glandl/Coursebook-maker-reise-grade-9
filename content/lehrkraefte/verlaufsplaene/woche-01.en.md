+++
title = "Week 1 · P1 Kickoff"
weight = 1
+++

**Student page:** [P1 Week 1 · Kickoff]({{% relref "projekte/p1-code-gadget/woche-01-kickoff" %}}) · **Duration:** double lesson · 95 min planned, the remaining time stays free

## Lesson goals

- The year structure (5 projects, rhythm, learning journal) is known and located in the book.
- Everyone has started Thonny and run and modified two programs (TB 02, grade 9).
- The term **state** is introduced via the switch (preview of TB 09).
- Everyone has a GitHub account, a private learning journal repository and at least one commit.
- Markdown basics (heading, list, image) have been applied once.
- Journal task 1 is begun, including gadget ideas.

## Preparation

### Technology

- [ ] Thonny working on all school PCs, test run with `input()` (some sandbox configurations block the shell).
- [ ] github.com reachable from the school network, including email delivery for the confirmation code (check the school mail filter!).
- [ ] Projector, book (start page, P1 brief, week 1, Git guide) open in the browser.
- [ ] Fallback in case of PC failure: [python.microbit.org](https://python.microbit.org/) in the browser.

### Classroom 50 (recommended)

GitHub Classroom was retired on 28 August 2026. The free successor is **[Classroom 50](https://classroom50.org/)** by the Fifty Foundation (CS50), documented in its [wiki](https://github.com/foundation50/classroom50/wiki). Every student gets a **private repository in your organisation**, you have access to all of them, and the submissions page shows the latest push per person with a timestamp. Exactly the progress view we want.

**At least two weeks before the first lesson:**

- [ ] Get verified as a teacher with [GitHub Education](https://docs.github.com/en/education/about-github-education/github-education-for-teachers/apply-to-github-education-as-a-teacher) (faculty ID or employment letter). Approval takes days to two weeks.
- [ ] Create a GitHub **organisation** for the school/class and upgrade it to the **Team plan** using the education benefit. Classroom 50 requires the Team plan (GitHub Pages from a private repo); the Free plan is not enough. The benefit on your account does **not** upgrade the organisation by itself.

**The week before:**

- [ ] On classroom50.org **Sign in with GitHub** → **Set up new organization** → **Run setup** (creates a `classroom50` repo and workflows) → **Next: service token** (fine-grained PAT scoped to this organisation only) → **Done**.
- [ ] **Create classroom**: name e.g. `Informatik 5A`, keep the slug short (it becomes part of the repo names, e.g. `inf5a`).
- [ ] Create the **template repository** `lernjournal-vorlage` in the organisation (settings: *Template repository*), content see below. Never put solutions in it: students can read the template including its history.
- [ ] Create the assignment: **Assignment type: Individual** · **Start with a template: Template repository** · **Advanced settings → Repository visibility: Private** · **Submission type: Every push to the default branch** · **Grading: Not graded** · leave the due date empty (the journal runs all year). **Feedback pull request** can stay on, then you can comment directly on journal lines.
- [ ] Have both links from **Share** ready: the **Classroom onboarding link** and the assignment link.

**In the lesson (roster):** Classroom 50 cannot find students by email and there is no self-service join. Usernames must be in the roster **before** accepting. In practice: collect usernames during the lesson (form or list on the projector), upload them as a plain list under **Roster → Upload roster**, then share the links. Re-uploading is safe, existing entries are kept. Repos must never be renamed (`<slug>-lernjournal-<username>`), otherwise they disappear from the submissions view.

- [ ] Privacy: usernames are public, repos are private. Agree on a naming convention with the class (e.g. first name plus initials), do not enforce real names. GitHub's minimum age is 13.

**Plan B without Classroom 50** (education approval not in time): tab "Create it yourself" in the Git guide. Everyone creates a private repo `lernjournal` and adds you as a collaborator. You then see progress via your GitHub home feed or a bookmark list of the repos. Moving to Classroom 50 later is possible but costs a lesson of migration.

### Other

- [ ] Hardware showcase: one micro:bit, Pico, ESP32, Arduino each, plus 2–3 finished mini gadgets to touch (e.g. micro:bit dice, Pico with button + LED). Passed around during the intro.
- [ ] Your own GitHub username on the board (for the "create it yourself" case).

## Flow

| Time | Phase | Teacher | Students | Material |
| ------ | ------- | --------- | ---------- | ---------- |
| 0–10 | **Intro** | Present the Maker Journey: 5 projects, rhythm kickoff→sprints→review→retro, role of the book. Demo two finished gadgets, pass the boards around. Announce the journal: "lives on GitHub, you create it today". | Listen, look at hardware | Projector, start page, showcase |
| 10–25 | **Tool check** | Start Thonny together, show shell vs. editor, `print` in the shell. Show the stop button now already. Browser fallback on problems. | Start Thonny, first command in the shell | PCs, Thonny guide |
| 25–55 | **Two programs** | Show program 1 (2 min), then individual/pair work. Circulate. After ~15 min a short stop: draw `switch.py` on the board as two circles with arrows, introduce the word **state**. 5 min before the end: announce "take a screenshot". | Run and modify `hello.py`, `switch.py`, screenshot; fast ones: `trafficlight.py` | Book page week 1 |
| 55–70 | **GitHub account & repo** | Walk through account creation step by step on the projector. Collect usernames (form/list), upload them as roster, then show the onboarding and assignment links. Those who finish help their neighbour. Catch confirmation code problems immediately (spam folder, second address). | Create account, report username, sign in at classroom50.org, accept assignment, bookmark repo link | Git guide parts 1+2, roster |
| 70–75 | **Markdown intro** | On the projector: open README in the web editor, show `#`, `-`, `**bold**`, image syntax, Preview tab. No more than these four things. | Watch, open the cheat sheet | Markdown cheat sheet |
| 75–80 | **First commit** | Have README filled in with name and class, dictate the commit message. Show on the Classroom 50 submissions page (after reload) that pushes arrive. | Edit README, preview, commit | Git guide part 3 |
| 80–93 | **Journal task 1** | Open `p1/woche-01.md` (from the template) or create it. Let them write; gadget ideas are part of the entry. Screenshot upload as a bonus, otherwise homework. | Write entry, commit | Journal task 1 |
| 93–95 | **Outlook** | Next week: team and board choice, requirements for the gadget, Kanban. Name the homework. | | |

## Differentiation

- **Fast:** `trafficlight.py` with fourth state; upload and embed the screenshot; extend README with an "About me" section; rebuild `switch.py` in the micro:bit simulator on python.microbit.org.
- **Slow:** only run program 2, skip the counting task. For the journal, a heading plus two sentences on expectations is enough today. Priority is that account and repo exist.
- **Prior knowledge (know Git or have programmed):** use as helpers for account creation.

## Typical pitfalls

- **Confirmation email does not arrive** (school mail filter). Plan B: allow a private address, or move account creation to homework before the first lesson if the class can be reached beforehand.
- **Username taken.** Suggest a convention with initials and a number.
- **"Accept assignment" fails or the assignment is not visible:** username missing from the roster or misspelled. Add it, re-upload, student reloads the page.
- **Assignment page shows stale data:** Classroom 50 publishes via GitHub Pages, changes take 20 seconds to a few minutes. Wait briefly, reload.
- **Slash in the file name** is the trick for folders; show it explicitly.
- `while True` without `break` blocks; show the stop button explicitly before program 2.
- `input()` not supported in some online editors; use Thonny.

## Homework

Finish journal task 1 and commit it (screenshot in `images/`). Try `trafficlight.py`. Install Thonny on your own device (if BYOD). Watch the video "Your first program" (German).

## Evidence and progress check

The commit to `p1/woche-01.md` is the evidence for this week. On the assignment's submissions page in Classroom 50 (or in the organisation under *Repositories*) you can see in two minutes before the next lesson who has pushed and who has not. The page only refreshes on reload. From now on this is the weekly routine: **skim the commit list once before every lesson.**

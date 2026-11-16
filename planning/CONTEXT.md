# Coursebook Informatik · Maker-Reise

Shared language for planning and writing the course book: a one-year, project-driven Informatik course for a 9th-grade class, published as a bilingual Hugo site.

## Language

### Projects and teams

**Team**:
2–3 students who build one gadget together in a project and share one private team repository.
_Avoid_: group

**Gadget**:
The interactive device a team builds in P1. It reacts to inputs, has states and responds through outputs.
_Avoid_: device, project (the project is P1, the gadget is what a team builds in it)

**User Story**:
A requirement written from a user's point of view ("Als … möchte ich …, damit …"), with a priority (Muss/Soll/Kann) and checkable acceptance criteria. A team's stories live in its `ANFORDERUNGEN.md`.
_Avoid_: requirement, feature, task (a task is a Kanban card, not a story)

**Karte** (card):
One task on a team's Kanban board, small enough for about one lesson hour. A User Story is broken down into several Karten; the team itself decides who takes a Karte and when.
_Avoid_: ticket, issue, step

### Individual instructions

**Baustein** (building block):
A generic, reusable instruction page in the public book that teaches one capability a gadget may need (e.g. reading a light sensor, playing a tone). It contains no team-specific content.
_Avoid_: recipe, module, snippet

**Kurs-Verkabelung** (course wiring):
The fixed pin assignment that every example in the book uses (e.g. button on GP14, LED on GP15), plus the reserved pins for additional components. Bausteine and Baupläne never deviate from it, so code from different pages fits together.
_Avoid_: pinout, wiring diagram

**Bauplan** (build plan):
Step-by-step build instructions for one team's Gadget, derived from its User Stories. It opens with the team's Muss stories in corrected form (clear story sentence, checkable acceptance criteria, a change note), then lists the Karten with their dependencies, then gives step-by-step instructions per Karte. It does not say who does what or when; that is the team's decision. Soll/Kann stories appear only as optional extras. It links to Bausteine for reusable how-to and adds the team-specific steps between them. Drafted by AI, reviewed by the teacher, copied into the team repository.
_Avoid_: individual instructions, team guide, personal tutorial

**Gerüst** (scaffold):
Team-specific starter code in a Bauplan: the team's own states and transitions are already laid out, the logic is left as marked gaps for the team to fill.
_Avoid_: template, starter kit, solution

**Tipp-Stufen** (hint levels):
The graded help attached to each gap in a Gerüst, opened one at a time: Tipp 1 (the idea), Tipp 2 (nearly the code), Lösung (the solution).
_Avoid_: hints, answers

**Team-Kürzel** (team code):
The anonymous identifier of a Team in planning material, formed from class and number (e.g. `4a-t3`). Never a student-chosen team name.
_Avoid_: team name (in planning material)

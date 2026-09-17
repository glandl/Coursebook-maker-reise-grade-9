+++
title = "Week 7 · Review and Retrospective"
weight = 7
+++

**Today:** the grand finale of P1. You present your gadgets, look at how you worked together in the **retrospective**, and complete your learning journal for this project.

{{% notice style="info" title="What you will have at the end of the lesson" %}}
- Your team has presented its gadget and received feedback.
- You have given written feedback to at least one other team.
- Your team has 1–2 concrete resolutions for P2.
- Your journal for P1 is complete, with project review and self-assessment, and committed.
{{% /notice %}}

## 1. Set up and tech check (10 min)

- Set up the gadget, connect it to power (power bank or USB), **play through it once completely**.
- Have the state diagram and code excerpt ready for projection (team repository open in the browser).
- Keep the plan B video at hand.
- The order of teams is on the board. Each person **draws a team** to give written feedback to.

## 2. Presentations (45 min)

Each team: **3 minutes of presentation + 2 minutes of questions**, as planned in [week 6]({{% relref "projekte/p1-code-gadget/woche-06-testen-doku" %}}). The teacher keeps time.

**Feedback card** (for the team you drew, on paper or as an issue in their team repository):

```markdown
Team: …

I like: …
I wonder: …
What if: …

The demo showed that … (which user story?)
```

What your teacher looks at (product, process, presentation, journal) is in the [rubric templates]({{% relref "lehrkraefte/rubriken" %}}).

## Break (5 min)

## 3. Retrospective (20 min)

The review looks at the **product**. The **retrospective** looks at the **collaboration**: how did we work, and what will we do differently in the next project? It is not about blame, it is about improvement.

Format **Start · Stop · Continue**, as a team:

| Step | Time | What happens |
|------|------|--------------|
| Write silently | 5 min | Each person writes sticky notes in three columns: **Start** (what should we begin doing?), **Stop** (what should we stop doing?), **Continue** (what worked well?). One idea per note. |
| Present and group | 8 min | Read out in turn and stick them up, move similar notes together. |
| Decide | 5 min | Each person has 2 dots to give. The 1–2 notes with the most dots become **resolutions for P2**, phrased as a concrete action: "We do a stand-up every lesson with a photo of the board" instead of "communicate better". |
| Record | 2 min | Photo of the wall, resolutions into the team repository's `README.md` under **Retrospective**. |

Prompts if you are stuck: did you keep the Kanban board up to date? Were tasks shared fairly? When did you get the most done, when the least, and why? How did merging the code go?

German video on the Start, Stop, Continue format:

{{< youtube rWz9VsHSpAE >}}

## 4. Journal submission (15 min)

Submission means: **the last commit is in**. Nothing is collected (see [Learning Journal]({{% relref "projekte/lernjournal" %}})).

{{% notice style="primary" title="Journal task 7 · Project review P1" icon="book" %}}
File `p1/woche-07.md`:

```markdown
# P1 · Week 7 · Project review · <date>

## Our gadget
One sentence, one photo, link to the team repository.

## My best code
A code excerpt you wrote yourself, and what is good about it.

## Self-assessment
| I can … | 1 | 2 | 3 | 4 | Evidence (link) |
|---------|---|---|---|---|-----------------|
| implement simple algorithms in Python (branching, loop, function, list) | | | | | |
| bring a board with sensor and actuator into operation | | | | | |
| investigate and explain the behaviour of an interactive system by varying inputs and feedback | | | | | |
| model a device with a state diagram and a flowchart | | | | | |

1 = not yet · 2 = with help · 3 = on my own · 4 = I can explain it to others

## Retrospective
Your team's resolutions for P2, and one personal resolution.

## Feedback
The feedback you got at the presentation in one sentence,
and what you think of it.
```
{{% /notice %}}

**Checklist before the last commit:**

- [ ] `p1/woche-01.md` to `p1/woche-07.md` exist.
- [ ] Journal tasks 1–7 are answered (headings from the templates).
- [ ] Images are in `images/` and are displayed (check the preview).
- [ ] `README.md` links all P1 entries.
- [ ] No passwords, no photos of people without their consent.

Commit message: `P1 week 7: project review, P1 submitted`.

## 5. Final quiz P1 (5 min)

{{< quiz title="Final quiz · P1 Code & Gadget" >}}
{{< question correct="2" >}}
What does this program print?

```python
values = [4, 8, 6]
total = 0
for v in values:
    if v > 5:
        total = total + v
print(total)
```
---
18
14
8
3
---
Only 8 and 6 are greater than 5, so 8 + 6 = 14.
{{< /question >}}
{{< question correct="1" >}}
`number = input("Number: ")`. How do you calculate with the input?
---
`number = int(input("Number: "))`
`number = input(int("Number: "))`
`number = number(input("Number: "))`
You don't need to, `input` already returns a number.
---
`input` returns text, `int(...)` converts it into a whole number.
{{< /question >}}
{{< question correct="3" >}}
A roller blind has the states UP, DOWN and MOVING. Which of these is an **event** that triggers a transition?
---
MOTOR
MOVING
limit switch reached
blind
---
States describe situations, events trigger the changes. "Limit switch reached" ends the MOVING state.
{{< /question >}}
{{< question correct="4" >}}
A button on a pin with pull-up should toggle the LED **exactly once per press**. What do you need?
---
A longer `time.sleep`.
A second pin.
`button.value() == 1` instead of `== 0`.
Edge detection: only react to the change from not pressed to pressed.
---
While the button is down, the pin reports 0 for many loop passes. Only the change 1 → 0 is the actual press.
{{< /question >}}
{{< question correct="2" >}}
How did we split up the code in P1?
---
Everything in `main.py`, so you never have to search.
`hardware.py` (board-specific), `logic.py` (testable on the PC), `main.py` (main loop)
One file per state.
`input.py`, `output.py`, `test.py`
---
The hardware layer makes the code board-independent, the logic file makes it testable.
{{< /question >}}
{{< question correct="1" >}}
You replace the sound of an alarm clock with a short flash of the LED. What are you investigating in terms of human-computer interaction?
---
How different feedback affects the behaviour of the users (e.g. whether they wake up).
How fast the processor is.
Whether the code gets shorter.
How much power the LED needs.
---
Varying the feedback and observing how people react to it is exactly the experiment from week 5.
{{< /question >}}
{{< question correct="3" >}}
What is the purpose of a **retrospective**?
---
To decide the grades for the project.
To demonstrate the product.
To improve the team's collaboration, with concrete resolutions for the next project.
To check the code for bugs.
---
The product is shown at the review, the code is checked in the code review. The retrospective looks at **how** the team worked.
{{< /question >}}
{{< question correct="4" >}}
Where on the Kanban board does a card belong whose acceptance criteria are only partly met?
---
Done
Backlog, it gets deleted.
Anywhere, as long as it is visible.
In progress
---
"Done" means: all acceptance criteria are met. Until then the card stays in progress.
{{< /question >}}
{{< /quiz >}}

## Outlook: P2 Weather Station

Your board can now measure and react. In [P2]({{% relref "projekte/p2-wetterstation" %}}) it learns to **transmit**: sending measurements over Wi-Fi, storing and analysing them. If you built with an ESP32 or Pico W, you keep using the board, and `hardware.py` simply grows new functions. You take the resolutions from today's retrospective with you.

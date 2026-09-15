+++
title = "P1 · Code & Gadget"
weight = 10
+++

**Duration:** ~7 weeks (weeks 1–7) · **Team:** 2–3 people · **Language:** Python (PC) and MicroPython (board)

## What is it about?

You learn Python from scratch and end up building an **interactive gadget** on a single-board computer: a device that reacts to inputs (buttons, sensors), moves between different **states**, and answers through outputs (LEDs, display, sound, motor).

Examples of gadgets teams have built or could build:

- Reaction game with two buttons and a high score
- Step counter or dice using the accelerometer
- Night light reacting to brightness and motion
- Timer/Pomodoro clock with display and buzzer
- Alarm system with distance sensor and code entry

## The end product

1. A **working gadget** on micro:bit, Raspberry Pi Pico, ESP32 or Arduino (your choice, see [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}})).
2. A **state diagram** of your gadget (which states exist, what triggers transitions).
3. The **source code** with comments, in the team repository.
4. A **3-minute presentation** at the review in week 7.
5. Your **learning journal entries** (at least one per week).

## Learning goals (curriculum)

At the end of P1 you can …

| TB | Competency (curriculum wording, translated) | Grade |
|----|---------------------------------------------|-------|
| 02 Algorithms & Programming | Implement algorithms in a text-based programming language using simple applications. | 9 |
| 04 Systems | Configure computer systems with peripherals, sensors or actuators and basic network functionality and use them for real-life tasks. *(Network part follows in P2)* | 10 |
| 06 Human-Computer Interaction | Build simple interactive systems and investigate and explain their behaviour by varying inputs and feedback. | 10 |
| 09 Modelling & Simulation | Abstract and model real objects or situations in a state-based and process-oriented way. | 9 |

## Schedule

| Week | Phase | Content |
|------|-------|---------|
| 1 | **Kickoff** | Maker Journey, first Python programs, create the learning journal on GitHub (Markdown, first commit), gadget ideas |
| 2 | Kickoff → Sprint 1 | Python: variables, branching, loops · choose team & board · requirements for the gadget · set up Kanban board |
| 3 | Sprint 1 | Functions and lists · bring the board to life: LED, button |
| 4 | Sprint 1 → Review | Connect sensors/actuators · draw the state diagram · **Sprint review 1** |
| 5 | Sprint 2 | Implement the state machine in code · vary behaviour through inputs |
| 6 | Sprint 2 | Polish, test, document · prepare presentation |
| 7 | **Review & Retro** | Presentations · retrospective · journal submission |

## Tools

- [Python & Thonny]({{% relref "werkzeuge/python-thonny" %}}) — from week 1
- [MicroPython Boards]({{% relref "werkzeuge/micropython-boards" %}}) — from week 3
- [Wokwi & Browser Simulators]({{% relref "werkzeuge/wokwi-simulator" %}}) — fallback without hardware
- [Git & GitHub]({{% relref "werkzeuge/git-github" %}}) and [Markdown]({{% relref "werkzeuge/markdown" %}}) — from week 1 for the learning journal
- [Learning Journal]({{% relref "projekte/lernjournal" %}}) — from day one

## Weeks

{{% children sort="weight" %}}

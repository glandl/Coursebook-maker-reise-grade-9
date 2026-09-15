+++
title = "Learning Journal"
weight = 1
+++

The learning journal accompanies you through the whole year. It is your memory, your evidence and later the material for your web portfolio in P5. It lives as **Markdown files in your own GitHub repository**. Every entry is a commit, so your teacher sees progress continuously, not only at the end of a project.

## Repository structure

```
lernjournal/
├── README.md              ← name, class, links to your entries
├── p1/
│   ├── woche-01.md        ← one entry per week
│   ├── woche-02.md
│   └── …
├── p2/ … p5/
├── selbstlernen/
│   └── datenstrukturen.md ← journal tasks from the learning paths
└── images/                ← screenshots and photos
```

How to create the repository and edit files in the browser is explained under [Git & GitHub]({{% relref "werkzeuge/git-github" %}}). The syntax is on the [Markdown cheat sheet]({{% relref "werkzeuge/markdown" %}}).

## What goes in

- **One entry per week** (mandatory): what did I do, what worked, where did I get stuck, what do I plan next?
- **Journal tasks** from the project weeks and the [self-study learning paths]({{% relref "selbstlernen" %}}), each headed with number and title.
- **Evidence:** screenshots, photos of your setup, code snippets, sketches, state diagrams.
- **Sources:** links that helped you, with one sentence on what you took from them.

## Template for a weekly entry

File `p1/woche-02.md`:

```markdown
# P1 · Week 2 · 2026-09-21

## Done
- …

## Worked
- …

## Stuck on
- …

## Next step
- …

## Evidence
![Screenshot switch.py](../images/p1-w02-switch.png)

## Sources
- [Thonny guide](…) – helped me find the stop button
```

## Rules

1. **Commit by the end of every school week at the latest.** The commit message says what you changed, e.g. `P1 week 2: entry and screenshot`.
2. **Short and honest beats long and pretty.** Three sentences per section are enough.
3. **Evidence goes into the `images/` folder**, not linked from external services.
4. **No other people's data:** no photos of classmates without consent, no passwords, no private addresses. The repository is private, but still.

## When is it looked at?

- **Continuously** via the commit history. Your teacher sees when you wrote what.
- Briefly at every **sprint review** (interim presentation) in the team.
- Completely at the **journal submission** at the end of each project. Submission means: the last commit is in, nothing is collected.
- The journal tasks from the self-study learning paths count as evidence that you have worked through the path.

{{% notice style="tip" title="Why this is useful, not annoying" %}}
If you keep the journal honestly, you find last time's solution in 30 seconds, you can say concretely in the retrospective what should change, and you already have all the content for the web portfolio in P5. And the commit history shows you yourself how much you got done in a year.
{{% /notice %}}

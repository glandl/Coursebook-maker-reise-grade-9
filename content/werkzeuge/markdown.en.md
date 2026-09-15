+++
title = "Markdown Cheat Sheet"
weight = 5
+++

**Markdown** is text with a few special characters for formatting. Your [learning journal]({{% relref "projekte/lernjournal" %}}) is written in Markdown, so is this book, and README files on GitHub anyway. You only need this handful of rules.

## The essentials

| You write | You get |
|-----------|---------|
| `# Heading` | large heading (one hash = level 1, `##` = level 2, `###` = level 3) |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `- item` | bullet list (start every line with `-`) |
| `1. step` | numbered list |
| `` `code` `` | `code` inside text |
| `[text](https://…)` | [link](https://thonny.org) |
| `![description](../images/picture.png)` | embedded image |
| `---` | horizontal rule |

Separate paragraphs with a **blank line**. A single line break is not enough.

## Code blocks

Multi-line code goes between three backticks, followed by the language for colours:

````markdown
```python
state = "OFF"
print(state)
```
````

becomes

```python
state = "OFF"
print(state)
```

## A complete example

```markdown
# P1 · Week 1 · 2026-09-14

## Done
- Started Thonny, wrote `hello.py` and `switch.py`
- Created GitHub account and learning journal

## Worked
- The switch toggles between **OFF** and **ON**

## Stuck on
- `while True` ran forever until I found the stop button

## Evidence
![My switch](../images/p1-w01-switch.png)
```

{{% notice style="tip" title="Preview" %}}
The GitHub editor has a **Preview** tab. There you see immediately how your text looks. In VS Code it is **Ctrl+Shift+V** later on.
{{% /notice %}}

## More

- [Basic writing and formatting syntax on GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [CommonMark reference](https://commonmark.org/help/) with an interactive 10-minute tutorial

+++
title = "Markdown-Spickzettel"
weight = 5
+++

**Markdown** ist Text mit ein paar Sonderzeichen für die Formatierung. Dein [Lernjournal]({{% relref "projekte/lernjournal" %}}) ist in Markdown geschrieben, dieses Buch auch, README-Dateien auf GitHub sowieso. Du brauchst nur diese Handvoll Regeln.

## Das Wichtigste

| Du schreibst | Es erscheint |
|--------------|--------------|
| `# Überschrift` | große Überschrift (eine Raute = Ebene 1, `##` = Ebene 2, `###` = Ebene 3) |
| `**fett**` | **fett** |
| `*kursiv*` | *kursiv* |
| `- Punkt` | Aufzählung (jede Zeile mit `-` beginnen) |
| `1. Schritt` | nummerierte Liste |
| `` `code` `` | `code` im Text |
| `[Text](https://…)` | [Link](https://thonny.org) |
| `![Beschreibung](../images/bild.png)` | eingebettetes Bild |
| `---` | Trennlinie |

Absätze trennst du mit einer **Leerzeile**. Ein einzelner Zeilenumbruch reicht nicht.

## Code-Blöcke

Mehrzeiliger Code kommt zwischen drei Backticks, dahinter die Sprache für die Farben:

````markdown
```python
zustand = "AUS"
print(zustand)
```
````

wird zu

```python
zustand = "AUS"
print(zustand)
```

## Ein vollständiges Beispiel

```markdown
# P1 · Woche 1 · 2026-09-14

## Gemacht
- Thonny gestartet, `hallo.py` und `schalter.py` geschrieben
- GitHub-Konto und Lernjournal angelegt

## Geklappt
- Der Schalter wechselt zwischen **AUS** und **AN**

## Hängen geblieben
- `while True` lief endlos, bis ich den Stopp-Button gefunden habe

## Belege
![Mein Schalter](../images/p1-w01-schalter.png)
```

{{% notice style="tip" title="Vorschau" %}}
Auf GitHub gibt es im Editor den Reiter **Preview**. Dort siehst du sofort, wie dein Text aussieht. In VS Code ist es später **Strg+Shift+V**.
{{% /notice %}}

## Mehr

- [Markdown-Grundlagen auf GitHub Docs](https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) (deutsch)
- [CommonMark-Referenz](https://commonmark.org/help/) mit interaktivem 10-Minuten-Tutorial (englisch)

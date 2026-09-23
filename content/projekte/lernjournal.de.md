+++
title = "Lernjournal"
weight = 5
+++

Das Lernjournal begleitet dich durch das ganze Jahr. Es ist dein Gedächtnis, dein Nachweis und später das Material für dein Web-Portfolio in P5. Es lebt als **Markdown-Dateien in deinem eigenen GitHub-Repository**. Jeder Eintrag ist ein Commit, deine Lehrkraft sieht den Fortschritt laufend, nicht erst am Projektende.

## Aufbau des Repositorys

```
lernjournal/
├── README.md              ← Name, Klasse, Links zu deinen Einträgen
├── p1/
│   ├── woche-01.md        ← ein Eintrag pro Woche
│   ├── woche-02.md
│   └── …
├── p2/ … p5/
├── selbstlernen/
│   └── datenstrukturen.md ← Journalaufträge aus den Lernpfaden
└── images/                ← Screenshots und Fotos
```

Wie du das Repository anlegst und Dateien im Browser bearbeitest, steht unter [Git & GitHub]({{% relref "werkzeuge/git-github" %}}). Die Schreibweise erklärt der [Markdown-Spickzettel]({{% relref "werkzeuge/markdown" %}}).

## Was hinein kommt

- **Ein Eintrag pro Woche** (Pflicht): Was habe ich gemacht, was hat funktioniert, wo bin ich hängen geblieben, was nehme ich mir vor?
- **Journalaufträge** aus den Projektwochen und den [Selbstlern-Lernpfaden]({{% relref "selbstlernen" %}}), jeweils mit Nummer und Titel als Überschrift.
- **Belege:** Screenshots, Fotos vom Aufbau, Code-Ausschnitte, Skizzen, Zustandsdiagramme.
- **Quellen:** Links, die dir geholfen haben, mit einem Satz, was du daraus mitgenommen hast.

## Vorlage für einen Wocheneintrag

Datei `p1/woche-02.md`:

```markdown
# P1 · Woche 2 · 2026-09-21

## Gemacht
- …

## Geklappt
- …

## Hängen geblieben
- …

## Nächster Schritt
- …

## Belege
![Screenshot schalter.py](../images/p1-w02-schalter.png)

## Quellen
- [Thonny-Anleitung](…) – hat mir beim Stopp-Button geholfen
```

## Regeln

1. **Commit spätestens am Ende jeder Unterrichtswoche.** Die Commit-Nachricht sagt, was du geändert hast, z. B. `P1 Woche 2: Eintrag und Screenshot`.
2. **Lieber kurz und ehrlich als lang und schön.** Drei Sätze pro Abschnitt reichen.
3. **Belege im Ordner `images/`** ablegen, nicht verlinkt von fremden Diensten.
4. **Keine fremden Daten:** keine Fotos von Mitschüler:innen ohne Zustimmung, keine Passwörter, keine privaten Adressen. Das Repository ist privat, aber trotzdem.

## Wann wird es angeschaut?

- **Laufend** über die Commit-Historie. Deine Lehrkraft sieht, wann du was geschrieben hast.
- Kurz bei jedem **Sprint-Review** (Zwischenpräsentation) im Team.
- Vollständig bei der **Journal-Abgabe** am Ende jedes Projekts. Abgabe heißt: der letzte Commit ist drin, es wird nichts eingesammelt.
- Die Journalaufträge aus den Selbstlern-Lernpfaden zählen als Nachweis, dass du den Lernpfad bearbeitet hast.

{{% notice style="tip" title="Warum das nicht lästig, sondern nützlich ist" %}}
Wer das Journal ehrlich führt, findet die Lösung vom letzten Mal in 30 Sekunden wieder, kann in der Retrospektive konkret sagen, was sich ändern soll, und hat für das Web-Portfolio in P5 den ganzen Inhalt schon fertig. Und die Commit-Historie zeigt dir selbst, wie viel du in einem Jahr geschafft hast.
{{% /notice %}}

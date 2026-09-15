+++
title = "Woche 1 · P1 Kickoff"
weight = 1
+++

**Schüler:innen-Seite:** [P1 Woche 1 · Kickoff]({{% relref "projekte/p1-code-gadget/woche-01-kickoff" %}}) · **Dauer:** Doppelstunde, 100 min netto

## Ziele der Stunde

- Die Jahresstruktur (5 Projekte, Rhythmus, Lernjournal) ist bekannt und im Buch verortet.
- Alle haben Thonny gestartet und zwei Programme ausgeführt und verändert (TB 02, 9. Schulstufe).
- Der Begriff **Zustand** ist über den Schalter eingeführt (Vorgriff auf TB 09).
- Alle haben ein GitHub-Konto, ein privates Lernjournal-Repository und mindestens einen Commit.
- Markdown-Grundlagen (Überschrift, Liste, Bild) sind einmal angewendet.
- Journalauftrag 1 ist begonnen, inklusive Gadget-Ideen.

## Vorbereitung

### Technik
- [ ] Thonny auf allen Schul-PCs lauffähig, Testlauf mit `input()` (manche Sandbox-Konfigurationen blockieren die Shell).
- [ ] github.com aus dem Schulnetz erreichbar, inklusive E-Mail-Empfang für den Bestätigungscode (Schul-Mail-Filter prüfen!).
- [ ] Beamer, Buch (Startseite, P1-Brief, Woche 1, Git-Anleitung) im Browser geöffnet.
- [ ] Fallback bei PC-Ausfall: [python.microbit.org](https://python.microbit.org/) im Browser.

### Classroom 50 (empfohlen)
GitHub Classroom wurde am 28. 8. 2026 eingestellt. Der freie Nachfolger ist **[Classroom 50](https://classroom50.org/)** der Fifty Foundation (CS50), Doku im [Wiki](https://github.com/foundation50/classroom50/wiki). Jede:r Schüler:in bekommt ein **privates Repository in deiner Organisation**, du hast Zugriff auf alle, und die Submissions-Seite zeigt pro Person den letzten Push mit Zeitstempel. Genau die Fortschrittsansicht, die wir wollen.

**Mindestens zwei Wochen vor der ersten Stunde:**
- [ ] Als Lehrkraft bei [GitHub Education](https://docs.github.com/en/education/about-github-education/github-education-for-teachers/apply-to-github-education-as-a-teacher) verifizieren lassen (Dienstausweis oder Schulbestätigung). Freigabe dauert Tage bis zwei Wochen.
- [ ] GitHub-**Organisation** für die Schule/Klasse anlegen und mit dem Education-Benefit auf den **Team-Plan** hochstufen. Classroom 50 braucht den Team-Plan (GitHub Pages aus privatem Repo); der Free-Plan reicht nicht. Der Benefit auf deinem Konto stuft die Organisation **nicht** automatisch hoch.

**In der Woche davor:**
- [ ] Auf classroom50.org **Sign in with GitHub** → **Set up new organization** → **Run setup** (legt ein Repo `classroom50` und Workflows an) → **Next: service token** (fine-grained PAT nur für diese Organisation) → **Done**.
- [ ] **Create classroom**: Name z. B. `Informatik 5A`, Slug kurz halten (wird Teil der Repo-Namen, z. B. `inf5a`).
- [ ] **Vorlagen-Repository** `lernjournal-vorlage` in der Organisation anlegen (Settings: *Template repository*), Inhalt siehe unten. Keine Lösungen hineinlegen: Schüler:innen können die Vorlage samt Historie lesen.
- [ ] Assignment anlegen: **Assignment type: Individual** · **Start with a template: Template repository** · **Advanced settings → Repository visibility: Private** · **Submission type: Every push to the default branch** · **Grading: Not graded** · Due date leer lassen (das Journal läuft das ganze Jahr). **Feedback pull request** kann an bleiben, dann kannst du Kommentare direkt an Journalzeilen schreiben.
- [ ] Beide Links aus **Share** bereitlegen: den **Classroom onboarding link** und den Aufgaben-Link.

**In der Stunde (Roster):** Classroom 50 kann Schüler:innen nicht per E-Mail finden und es gibt keinen Selbst-Beitritt. Die Benutzernamen müssen **vor** dem Annehmen im Roster stehen. Praktisch: Benutzernamen in der Stunde einsammeln (Formular oder Liste am Beamer), als Textliste unter **Roster → Upload roster** hochladen, dann Links freigeben. Erneutes Hochladen ist sicher, bestehende Einträge bleiben. Repos dürfen nie umbenannt werden (`<slug>-lernjournal-<username>`), sonst verschwinden sie aus der Submissions-Ansicht.

- [ ] Datenschutz: Benutzernamen sind öffentlich, Repos sind privat. Mit der Klasse eine Namenskonvention vereinbaren (z. B. Vorname plus Kürzel), keine Klarnamen erzwingen. GitHub-Mindestalter ist 13.

**Plan B ohne Classroom 50** (Education-Freigabe nicht rechtzeitig da): Tab „Selbst anlegen“ in der Git-Anleitung. Jede:r legt ein privates Repo `lernjournal` an und trägt dich als Collaborator ein. Fortschritt siehst du dann über deine GitHub-Startseite (Feed) oder eine Lesezeichenliste der Repos. Umstieg auf Classroom 50 später ist möglich, kostet aber eine Stunde Migration.

### Sonstiges
- [ ] Hardware-Schaukasten: je ein micro:bit, Pico, ESP32, Arduino, dazu 2–3 fertige Mini-Gadgets zum Anfassen (z. B. micro:bit-Würfel, Pico mit Taste + LED). Geht im Einstieg herum.
- [ ] Deinen eigenen GitHub-Benutzernamen an die Tafel (für den Fall „Selbst anlegen“).

## Verlauf

| Zeit | Phase | Lehrkraft | Schüler:innen | Material |
|------|-------|-----------|---------------|----------|
| 0–10 | **Einstieg** | Maker-Reise vorstellen: 5 Projekte, Rhythmus Kickoff→Sprints→Review→Retro, Rolle des Buchs. Zwei fertige Gadgets vorführen, Boards herumgeben. Lernjournal ankündigen: „liegt bei GitHub, ihr legt es heute an“. | Zuhören, Hardware anschauen | Beamer, Startseite, Schaukasten |
| 10–25 | **Werkzeug-Check** | Thonny gemeinsam starten, Shell vs. Editor zeigen, `print` in Shell. Stopp-Button jetzt schon zeigen. Bei Problemen Browser-Fallback. | Thonny starten, erster Befehl in Shell | PCs, Thonny-Anleitung |
| 25–55 | **Zwei Programme** | Programm 1 vorzeigen (2 min), dann Einzel-/Paararbeit. Zirkulieren. Nach ~15 min kurzer Stopp: `schalter.py` an der Tafel als zwei Kreise mit Pfeilen zeichnen, Wort **Zustand** einführen. 5 min vor Schluss: „Screenshot machen“ ansagen. | `hallo.py`, `schalter.py` ausführen und verändern, Screenshot; Schnelle: `ampel.py` | Buchseite Woche 1 |
| 55–60 | **Pause** | | | |
| 60–75 | **GitHub-Konto & Repo** | Kontoanlage Schritt für Schritt am Beamer mitmachen. Benutzernamen einsammeln (Formular/Liste), als Roster hochladen, dann Onboarding- und Aufgaben-Link zeigen. Wer fertig ist, hilft der Nachbarin. Bestätigungscode-Probleme sofort auffangen (Spam-Ordner, zweite Adresse). | Konto anlegen, Benutzernamen melden, bei classroom50.org anmelden, Assignment annehmen, Repo-Link als Lesezeichen | Git-Anleitung Teil 1+2, Roster |
| 75–80 | **Markdown-Intro** | Am Beamer: README im Web-Editor öffnen, `#`, `-`, `**fett**`, Bild-Syntax zeigen, Reiter Preview. Nicht mehr als diese vier Dinge. | Mitschauen, Spickzettel öffnen | Markdown-Spickzettel |
| 80–85 | **Erster Commit** | README mit Name und Klasse ausfüllen lassen, Commit-Nachricht vorgeben. Auf der Submissions-Seite von Classroom 50 (nach Reload) zeigen, dass die Pushes ankommen. | README bearbeiten, Preview, Commit | Git-Anleitung Teil 3 |
| 85–98 | **Journalauftrag 1** | `p1/woche-01.md` öffnen (aus der Vorlage) bzw. anlegen. Schreiben lassen; Gadget-Ideen sind Teil des Eintrags. Screenshot-Upload als Bonus, sonst Hausaufgabe. | Eintrag schreiben, committen | Journalauftrag 1 |
| 98–100 | **Ausblick** | Nächste Woche: Team- und Board-Wahl, Anforderungen ans Gadget, Kanban. Hausaufgabe nennen. | | |

## Differenzierung

- **Schnelle:** `ampel.py` mit viertem Zustand; Screenshot hochladen und einbinden; README um einen Abschnitt „Über mich“ erweitern; `schalter.py` im micro:bit-Simulator auf python.microbit.org nachbauen.
- **Langsame:** Programm 2 nur laufen lassen, Zähl-Aufgabe weglassen. Beim Journal reicht heute die Überschrift plus zwei Sätze zu den Erwartungen. Priorität hat, dass Konto und Repo existieren.
- **Vorwissen (haben schon Git oder programmiert):** als Helfer:innen für die Kontoanlage einsetzen.

## Typische Stolpersteine

- **Bestätigungs-E-Mail kommt nicht an** (Schulmail-Filter). Plan B: private Adresse erlauben oder Kontoanlage als Hausaufgabe vorziehen, wenn die Klasse vor der ersten Stunde erreichbar ist.
- **Benutzername vergeben.** Konvention mit Kürzel und Zahl vorschlagen.
- **„Accept assignment“ schlägt fehl oder die Aufgabe ist nicht sichtbar:** Benutzername fehlt im Roster oder ist falsch geschrieben. Roster ergänzen, erneut hochladen, Schüler:in lädt die Seite neu.
- **Assignment-Seite zeigt alten Stand:** Classroom 50 veröffentlicht über GitHub Pages, Änderungen brauchen 20 Sekunden bis wenige Minuten. Kurz warten, neu laden.
- **Schrägstrich im Dateinamen** ist der Trick für Ordner; explizit zeigen.
- `while True` ohne `break` blockiert; Stopp-Button explizit vor Programm 2 zeigen.
- `input()` in manchen Online-Editoren nicht unterstützt; Thonny nutzen.

## Hausaufgabe

Journalauftrag 1 fertigstellen und committen (Screenshot in `images/`). `ampel.py` ausprobieren. Thonny auf dem eigenen Gerät installieren (falls BYOD). Video „Dein erstes Programm“ ansehen.

## Nachweis und Fortschrittskontrolle

Der Commit an `p1/woche-01.md` ist der Nachweis für diese Woche. Auf der Submissions-Seite des Assignments in Classroom 50 (oder in der Organisation unter *Repositories*) siehst du vor der nächsten Stunde in zwei Minuten, wer gepusht hat und wer nicht. Die Seite aktualisiert sich nur beim Neuladen. Das ist ab jetzt die wöchentliche Routine: **vor jeder Stunde einmal die Commit-Liste durchsehen.**

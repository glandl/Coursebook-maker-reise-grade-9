+++
title = "Git & GitHub"
weight = 4
+++

**GitHub** ist der Ort, an dem dein [Lernjournal]({{% relref "projekte/lernjournal" %}}) und später der Code deiner Teams liegen. **Git** ist das Werkzeug dahinter, das jede Änderung als **Commit** festhält. In Woche 1 arbeitest du nur im Browser. Das lokale Arbeiten mit Git kommt, sobald ihr im Team Code teilt.

## Teil 1 · Konto anlegen

1. [github.com/signup](https://github.com/signup) öffnen.
2. E-Mail-Adresse (Schul-Adresse, falls vorhanden), Passwort und einen **Benutzernamen** wählen. Der Benutzername ist öffentlich sichtbar: Kein voller Klarname nötig, aber so, dass deine Lehrkraft dich zuordnen kann, z. B. `vorname-nachname-kuerzel` oder wie in der Klasse vereinbart.
3. Bestätigungscode aus der E-Mail eingeben.

{{% notice style="warning" title="Passwort" %}}
Notiere das Passwort an einem sicheren Ort. Ein vergessenes GitHub-Passwort kostet eine halbe Stunde. Wenn die Schule einen Passwort-Manager hat, verwende ihn.
{{% /notice %}}

## Teil 2 · Lernjournal-Repository anlegen

{{< tabs groupid="repo" >}}
{{% tab title="Mit Einladungslink (Classroom 50)" %}}
Die Klasse verwendet **Classroom 50**, ein freies Werkzeug, das jeder Person ein eigenes privates Repository in der Organisation der Schule anlegt.

1. **Benutzernamen melden:** Sag deiner Lehrkraft deinen GitHub-Benutzernamen (Liste an der Tafel oder Formular). Erst danach kann sie dich freischalten.
2. [classroom50.org](https://classroom50.org/) öffnen, **Sign in with GitHub** klicken und Classroom 50 im Fenster erlauben (**Authorize**).
3. Den **Klassen-Link** der Lehrkraft öffnen (Einladung in die Organisation annehmen, falls gefragt).
4. Den **Aufgaben-Link** `lernjournal` öffnen. Die Seite zeigt deinen Benutzernamen und den Namen des Repositorys, das du bekommst.
5. **Accept assignment** klicken. Eine Checkliste zeigt den Fortschritt, das dauert bis zu einer Minute.
6. **Open repository** klicken und die Seite als **Lesezeichen** speichern.

Dein Repository heißt nach dem Muster `<klasse>-lernjournal-<benutzername>`. **Nicht umbenennen**, sonst findet Classroom 50 es nicht mehr. Es ist privat: Nur du und deine Lehrkraft sehen es. Die Ordnerstruktur und eine Vorlage sind bereits drin.
{{% /tab %}}
{{% tab title="Selbst anlegen" %}}
1. Oben rechts **+ → New repository**.
2. Repository name: `lernjournal`. Sichtbarkeit: **Private**.
3. Haken bei **Add a README file**. Dann **Create repository**.
4. Lehrkraft als Mitleserin eintragen: **Settings → Collaborators → Add people**, GitHub-Benutzernamen der Lehrkraft eingeben.
5. Ordnerstruktur anlegen: **Add file → Create new file**, als Dateiname `p1/woche-01.md` eintippen (der Schrägstrich erzeugt den Ordner), Inhalt aus der [Vorlage]({{% relref "projekte/lernjournal" %}}) einfügen, **Commit changes**.
{{% /tab %}}
{{< /tabs >}}

## Teil 3 · Datei im Browser bearbeiten und committen

1. Im Repository die Datei anklicken, z. B. `README.md`.
2. Rechts oben das **Stift-Symbol** (Edit this file).
3. Text ändern. Mit dem Reiter **Preview** kontrollieren, wie das Markdown aussieht.
4. Rechts oben **Commit changes…**
5. Eine kurze **Commit-Nachricht** eintragen, die sagt, was du geändert hast, z. B. `README: Name und Klasse ergänzt`. Dann **Commit changes**.

Das ist der ganze Kreislauf: **bearbeiten → Vorschau → committen**. Jeder Commit ist ein Punkt in der Zeitleiste. Unter **Commits** (oder dem Uhr-Symbol) siehst du alle bisherigen Stände und kannst jeden alten Stand ansehen.

### Neue Datei anlegen

**Add file → Create new file**. Im Dateinamen einen Ordner mit Schrägstrich angeben: `p1/woche-02.md`.

### Bild hochladen

1. **Add file → Upload files**.
2. Screenshot hineinziehen. Vorher sinnvoll benennen, z. B. `p1-w01-schalter.png`.
3. Ganz unten **Commit changes**. Das Bild liegt jetzt im Repository (lege es in den Ordner `images/`, indem du zuerst in den Ordner wechselst).
4. Im Journal-Eintrag einbinden: `![Mein Schalter](../images/p1-w01-schalter.png)`

{{% notice style="info" title="Screenshot machen" %}}
Windows: **Win+Shift+S** · macOS: **Cmd+Shift+4** · Linux (GNOME): **Druck**-Taste. Das Bild landet in der Zwischenablage oder im Bilder-Ordner.
{{% /notice %}}

## Die drei Begriffe, die du heute brauchst

| Begriff | Bedeutung |
|---------|-----------|
| **Repository** (Repo) | Ein Projektordner mit vollständiger Geschichte aller Änderungen. |
| **Commit** | Ein gespeicherter Stand mit Nachricht, Zeitpunkt und Autor:in. Unveränderlich. |
| **Commit-Nachricht** | Ein Satz, der sagt, was sich geändert hat. Für dich in drei Monaten und für deine Lehrkraft. |

## Später: Git lokal

Sobald Teams gemeinsam Code schreiben (ab P1 Sprint 1), arbeitet ihr mit Git auf dem eigenen Rechner: klonen, ändern, committen, pushen, und mit **Branches** parallel arbeiten. Diese Anleitung wird dann erweitert. Bis dahin reicht der Browser.

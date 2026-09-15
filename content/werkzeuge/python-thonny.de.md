+++
title = "Python & Thonny"
weight = 1
+++

**Thonny** ist die Python-Entwicklungsumgebung des Kurses. Sie bringt Python mit, hat eine eingebaute Shell, einen Debugger für Anfänger:innen und kann später direkt mit MicroPython-Boards sprechen. Ein Werkzeug für das ganze Jahr.

## Installation

{{< tabs groupid="os" >}}
{{% tab title="Windows" %}}
1. Installer von [thonny.org](https://thonny.org/) laden (Button „Windows“).
2. Installer ausführen, Standardeinstellungen belassen. Python ist enthalten, es muss nichts extra installiert werden.
3. Thonny aus dem Startmenü starten.

Auf Schul-PCs ist Thonny bereits installiert; falls nicht, gibt es auf thonny.org auch eine **portable Version**, die ohne Installationsrechte aus einem Ordner oder USB-Stick läuft.
{{% /tab %}}
{{% tab title="macOS" %}}
1. Auf [thonny.org](https://thonny.org/) den Mac-Download wählen (Apple Silicon oder Intel, je nach Gerät).
2. Die `.pkg`-Datei öffnen und den Anweisungen folgen.
3. Thonny aus dem Programme-Ordner starten. Beim ersten Start eventuell Rechtsklick → Öffnen, falls macOS die Herkunft prüft.
{{% /tab %}}
{{% tab title="Linux" %}}
Am einfachsten über die Paketverwaltung:

```bash
sudo apt install thonny      # Debian / Ubuntu / Mint / Pop!_OS
```

Alternativ das Installationsskript von [thonny.org](https://thonny.org/) verwenden.
{{% /tab %}}
{{% tab title="Browser (Fallback)" %}}
Wenn nichts installiert werden kann:

- [python.microbit.org](https://python.microbit.org/) — Python-Editor mit micro:bit-Simulator, läuft komplett im Browser.
- [Wokwi](https://wokwi.com/) — Simulator für Pico, ESP32 und mehr, siehe [Wokwi & Browser-Simulatoren]({{% relref "werkzeuge/wokwi-simulator" %}}).

Für reines PC-Python ohne Board funktioniert jeder Online-Python-Editor, der `input()` unterstützt.
{{% /tab %}}
{{< /tabs >}}

## Erster Start

1. Beim ersten Start fragt Thonny nach Sprache: **Deutsch** wählen (später änderbar unter *Extras → Optionen → Allgemein*).
2. Oben ist der **Editor** (hier schreibst du Programme), unten die **Shell** (hier probierst du einzelne Befehle).
3. In die Shell tippen und Enter drücken:

```python
print("Hallo Maker-Reise!")
```

4. Ein Programm: **Datei → Neu**, Code eintippen, **Datei → Speichern** als `test.py`, dann grüner **Play-Button** (oder **F5**).

## Die wichtigsten Knöpfe

| Knopf / Taste | Bedeutung |
|---------------|-----------|
| ▶ Play (F5) | Aktuelle Datei ausführen |
| ■ Stopp | Laufendes Programm abbrechen (wichtig bei `while True`) |
| 🐞 Debug (Strg+F5) | Programm Schritt für Schritt ausführen, Variablen beobachten |
| *Ansicht → Variablen* | Zeigt alle Variablen und ihre Werte während des Programms |
| *Ansicht → Assistent* | Erklärt Fehlermeldungen in verständlicher Sprache |

{{% notice style="tip" title="Wenn ein Programm nicht mehr reagiert" %}}
Stopp-Button drücken oder in die Shell klicken und **Strg+C**. Bei einer Endlosschleife ist das normal, kein Fehler.
{{% /notice %}}

## Videos

Kurze Einführung in die Oberfläche:

{{< youtube 93J6Sxk55mg >}}

Erste Schritte mit Python in Thonny:

{{< youtube k7CLrRkzC5o >}}

## Später im Kurs

Thonny ist das Werkzeug für **P1 und P2**. Ab **P3** wechselt der Kurs zu **Visual Studio Code**, weil dort Notebooks, Datenanalyse, SQL und später Web-Entwicklung mit Git besser aufgehoben sind. Eine eigene Setup-Anleitung folgt zum Start von P3.

Ab P1 Woche 3 verbindest du Thonny mit deinem Board: *Extras → Optionen → Interpreter* → MicroPython auswählen. Anleitung unter [MicroPython-Boards]({{% relref "werkzeuge/micropython-boards" %}}).

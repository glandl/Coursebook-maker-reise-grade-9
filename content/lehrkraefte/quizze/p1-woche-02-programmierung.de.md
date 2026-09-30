+++
title = "P1 Woche 2 · Programmierung"
weight = 1
+++

Fünf Fragen zu den Python-Grundlagen aus [P1 Woche 2 · Team, Anforderungen, Kanban]({{% relref "projekte/p1-code-gadget/woche-02-anforderungen" %}}): Eingabe/Typumwandlung, Verzweigung, Vergleichs-/Booleoperatoren und Schleifen. Die ersten drei Fragen sind identisch mit dem Quiz auf der Schüler:innen-Seite; die letzten beiden sind zusätzliche Fragen für den Unterricht, z. B. als Einstieg in Woche 3 oder als Kurztest.

{{< quiz title="Quiz · P1 Woche 2 · Programmierung" >}}
{{< question correct="3" >}}
Was passiert bei diesem Code, wenn du `15` eingibst?

```python
alter = input("Alter? ")
print(alter + 1)
```
---
Es wird `16` ausgegeben.
Es wird `151` ausgegeben.
Es gibt einen Fehler.
Es wird `15` ausgegeben.
---
`input` liefert Text (`"15"`). Text und Zahl kann Python nicht addieren (`TypeError`). Richtig wäre `alter = int(input("Alter? "))`.
{{< /question >}}
{{< question correct="2" >}}
Welche Zahlen gibt `for i in range(3): print(i)` aus?
---
1, 2, 3
0, 1, 2
0, 1, 2, 3
3, 2, 1
---
`range(3)` beginnt bei 0 und endet **vor** 3.
{{< /question >}}
{{< question correct="2" >}}
`temperatur = 22`. Was gibt das Programm aus?

```python
if temperatur > 25:
    print("heiß")
elif temperatur > 18:
    print("angenehm")
else:
    print("kalt")
```
---
heiß
angenehm
kalt
angenehm und kalt
---
22 > 25 ist falsch, 22 > 18 ist wahr. Nach dem ersten zutreffenden Zweig ist Schluss.
{{< /question >}}
{{< question correct="2" >}}
`alter = 16`, `hat_ticket = False`. Was gibt das Programm aus?

```python
if alter >= 18 or hat_ticket:
    print("Einlass")
else:
    print("Kein Einlass")
```
---
Einlass
Kein Einlass
Ein Fehler
Einlass und Kein Einlass
---
`alter >= 18` ist falsch, `hat_ticket` ist falsch. Bei `or` muss **mindestens eine** Seite wahr sein, damit die Bedingung zutrifft.
{{< /question >}}
{{< question correct="2" >}}
Du gibst nacheinander `15` und dann `3` ein. Wie oft fragt das Programm insgesamt nach einer Zahl?

```python
zahl = int(input("Zahl zwischen 1 und 10: "))
while zahl < 1 or zahl > 10:
    zahl = int(input("Nochmal: "))
print("OK:", zahl)
```
---
Einmal
Zweimal
Dreimal
Endlos oft
---
Die erste Eingabe (`15`) liegt außerhalb von 1–10, die Schleifenbedingung ist also wahr und fragt ein zweites Mal. `3` liegt im Bereich, die Bedingung wird falsch und die Schleife endet.
{{< /question >}}
{{< /quiz >}}

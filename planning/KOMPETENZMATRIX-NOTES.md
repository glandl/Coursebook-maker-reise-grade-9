# Kompetenzmatrix — source verification notes

Internal companion to `PLAN.md` §4 and `content/lehrkraefte/kompetenzmatrix`. Records how the full-text matrix was verified on 2026-09-17 (issue #2). **Not published on the site** — the public pages only show the result.

## Source

- File: `planning/LP-Informatik-Sek2-v1.3-nachBegutachtung.xlsx`.
- Sheet: `PF-NachBegutachtung-V1` (sheet 2) — the only valid sheet. Sheet 1 (`9te-12teSchulstufe-2023`) is hidden and marked "DO-NOT-EDIT!!!! Outdated !!!" inside the workbook — never used, not even for cosmetic details like section titles.
- The document's own title (cell A1 of sheet 2) is "Lehrplan Informatik und Künstliche Intelligenz (Pflichtfach)". Public-facing pages refer to the source as **„Lehrplan für Informatik und KI"** — never by the xlsx filename.
- Extracted 2026-09-17 by parsing the workbook's OOXML directly (Python stdlib `zipfile` + `xml.etree` on `xl/worksheets/sheet2.xml` + `xl/sharedStrings.xml`) — neither `openpyxl` nor `pip` were available in the environment.

## Row-count discrepancy

The sheet's own header (row 5) states "9 Kompetenzen (9. Schulstufe) / 9 Kompetenzen (10. Schulstufe) / 8 Kompetenzen (11. Schulstufe)" = 26. Counting the actual competency ("K") rows gives **9 / 9 / 9 = 27**. The published matrix and `PLAN.md` §4 follow the row count (27), not the header claim (26).

## Themenbereich 04 title

At first extraction (2026-09-17, morning) the title/heading row for TB04 was empty in the sheet — only the "A" (content) row ("Rechnersysteme (z.B. Einplatinenrechner oder virtuelle Maschinen), Peripherie und vernetzte Systeme") and the "K" (competency) row were filled. We chose the working title **"Computersysteme" / "Computer Systems"**, not derived from the outdated sheet 1, and published under it.

The source workbook was edited later the same day (revision 156→157, modified timestamp 2026-09-17T13:13:55Z, resaved via ONLYOFFICE) and now has cell A30 filled with **"04 Computersysteme"** — the title is confirmed in the source itself, matching what was already published. Re-diffed the full cell contents against the previous version: this is the only data change, everything else differing between the two xlsx blobs (`[Content_Types].xml` ordering, relationship IDs, `docProps/core.xml` revision/timestamp, threaded-comment person GUIDs, and a new `xl/jsaProject.bin` with ONLYOFFICE's default empty macro/custom-function boilerplate) is resave noise from the editor, not a content change.

## Grade corrections vs. the v0.1 draft (PLAN.md, 2026-09-15)

| TB | Competency | Was (v0.1) | Is (verified) |
|----|-----------|-----------|----------------|
| 02 | „Algorithmen anhand einfacher Laufzeitabschätzungen vergleichen…" | 10 | **11** (same column as "Programmcode verbessern/korrigieren") |
| 04 | „Rechnersysteme mit Peripherie, Sensoren…" | 9–11 | **10 only** |
| 05 | „…Stufenmodell und Netzbasierte Dienste…" | 10/11 | **11 only** |
| 06 | „einfache interaktive Systeme bauen…" | 9 | **10** |
| 06 | „Interaktionsformen…beschreiben und vergleichen…" | 10 | **11** |
| 07 | „Anforderungen…nachvollziehen" | 9–11 | **10 only** |
| 09 | „…zustandsbasiert und ablauforientiert abstrahieren und modellieren." | 9–11 | **9 only** |

## TB11 merge correction

The v0.1 draft merged two distinct competencies into one row ("Ethisch/inklusive Systemgestaltung; Berufsfelder der Informatik", grade 11). They are in fact two separate "K" rows at different grades:

- Grade 9 (no semester given in the sheet): „zentrale Berufsfelder der Informatik und der Informationstechnik beschreiben, typische Aufgaben zuordnen und erklären, wo Informatik und KI im (Berufs-)Alltag und in der Gesellschaft eine Rolle spielt."
- Grade 11 (WS): „skizzenhaft Informatiksysteme unter Berücksichtigung unterschiedlicher vorgegebener Interessen und menschlicher Bedürfnisse gestalten, unter anderem unter ethischen und inklusiven Gesichtspunkten."

Both are now published as separate rows, both mapped to the Selbstlernen path "Berufsfelder & Ethik".

## Footnote numbers in the source text

Sentences in the sheet end with trailing reference numbers, e.g. „…erfasst werden.6, 7, 9, 13". These appear to reference a numbered list of overarching competency dimensions used elsewhere in the curriculum framework (not resolved within sheet 2 itself — the "Anmerkungen" block at the top of the sheet references similar numbered items, e.g. the Dagstuhl-Dreieck T/A/G dimensions, but not a matching 1–13 list). Since they're not meaningful without that external list, they were **dropped** from the wording on the published pages. Full verbatim extraction (with the numbers) is preserved in the extraction transcript of the 2026-09-17 session if ever needed again.

## Full raw extraction (for reference, verbatim incl. footnote numbers)

Themenbereich / grade 9 / grade 10 / grade 11 competency texts, one row per "K" entry in the sheet, in document order:

1. **01** — G9: "den Weg von Daten von der Erfassung bis zur Analyse untersuchen und benennen, von welchen Akteurinnen und Akteuren sie zu welchen Zwecken genutzt und erfasst werden.6, 7, 9, 13" (WS+SS)
2. **01** — G10: "einfache Datenmodellierung sowie Abfragen durchführen und Daten aus Datenbeständen zusammenführen.9" (SS)
3. **02** — G9: "Algorithmen in einer textbasierten Programmiersprache anhand einfacher Anwendungen umsetzen.10" (WS+SS)
4. **02** — G10: "Algorithmen unter Verwendung geeigneter Datenstrukturen implementieren.9" (WS)
5. **02** — G11: "gegebene Programmcodes bei Bedarf verbessern/korrigieren.10" (SS)
6. **02** — G11: "Algorithmen anhand einfacher Laufzeitabschätzungen vergleichen (rekursive und nicht rekursive) sowie ein Beispiel für ein nicht berechenbares Problem benennen." (SS)
7. **03** — G9: "einfache KI-Modelle mit Hilfe eines Algorithmus erstellen, anwenden sowie bewerten und KI-Systeme hinsichtlich ihrer Eignung sowie ethischer und inklusiver Aspekte beurteilen.5, 7, 8, 9" (WS+SS)
8. **03** — G10: "grundlegende Verfahren des maschinellen Lernens anhand geeigneter Algorithmen schrittweise durchführen und deren Funktionsweisen erklären.7, 8, 9" (WS)
9. **03** — G11: "grundlegende Funktionsweisen neuronaler Netze und generativer KI erklären, deren Ergebnisse (wie auch Fehler und Verzerrungen) analysieren sowie Auswirkungen von KI auf die Arbeitswelt reflektieren.7, 9, 13" (WS)
10. **03** — G11: "KI-Anwendungsbereiche vergleichen und begründen, welches Verfahren für einen gegebenen Problemtyp geeignet ist." (WS)
11. **04** (Computersysteme) — G10: "Rechnersysteme mit Peripherie, Sensoren oder Aktoren sowie grundlegender Netzwerkfunktionalität konfigurieren und für lebensweltliche Aufgaben einsetzen.1, 3, 9" (WS)
12. **05** — G9: "die Grundidee lokaler Netzwerke sowie einfache Protokolle erklären und ein Gerät eigenständig in ein lokales Netzwerk einbinden." (WS+SS)
13. **05** — G11: "unterschiedliche Modelle für Netzwerk-Kommunikation erklären (zB zustandslos/verbindungsorientiert) sowie netzbasierte Dienste analysieren und begründet beurteilen, welche technischen Voraussetzungen für eine zuverlässige Nutzung erforderlich sind.6, 13" (WS)
14. **06** — G10: "einfache interaktive Systeme bauen sowie deren Systemverhalten durch Variation von Eingaben und Rückmeldungen untersuchen und erklären." (WS)
15. **06** — G11: "Interaktionsformen mit Computersystemen beschreiben und vergleichen sowie deren Nutzung für diverse Benutzergruppen begründet einordnen.3, 5, 8" (WS)
16. **07** — G10: "Anforderungen an Software- oder technische Systeme in natürlicher Sprache sowie einfachen grafischen Notationen nachvollziehen.2, 10" (SS)
17. **08** — G9: "digitale Artefakte unter Berücksichtigung der Trennung zwischen Form und Inhalt erstellen, anpassen und unter Berücksichtigung von geistigem Eigentum verantwortungsvoll weiterverwenden.6, 7, 10, 13" (WS+SS)
18. **08** — G10: "multimediale Artefakte mit unterschiedlichen Zugängen bzgl. Gruppen von Benutzerinnen und Benutzern (auch unter Berücksichtigung von Inklusion) erzeugen und die verwendeten Prinzipien begründen.5, 6, 8, 10" (SS)
19. **08** — G11: "einfache webbasierte Anwendungen gestalten, client- und serverseitige Anteile unterscheiden und bestehende Webartefakte gezielt anpassen.6, 10, 13" (SS)
20. **09** — G9: "reale Objekte oder Situationen zustandsbasiert und ablauforientiert abstrahieren und modellieren." (WS+SS)
21. **10** — G9: "die Sphären der Privatheit nach DSGVO beschreiben und im Kontext der eigenen Lebenswelt ihr Verhalten begründen.3, 7" (WS+SS)
22. **10** — G10: "unterschiedliche symmetrische und asymmetrische Verschlüsselungs- und Authentifizierungsverfahren anwenden und erklären, sowie Vor- und Nachteile in Bezug auf Sicherheit, Nutzbarkeit und Privatsphäre in unterschiedlichen gesellschaftlichen und rechtlichen Kontexten begründet abwägen.7, 13" (SS)
23. **10** — G11: "Prinzipien der Open Source Intelligence (OSINT) erläutern, sowie aus dem eigenen Datenfußabdruck neue Informationen ableiten.6, 7" (SS)
24. **11** — G9: "erklären, welche technischen Faktoren (zB Rechenleistung, Datenübertragung, Speicherung) den Energie- und Ressourcenverbrauch digitaler Systeme beeinflussen und Systeme nachhaltig gestalten.11, 13" (WS+SS)
25. **11** — G9: "zentrale Berufsfelder der Informatik und der Informationstechnik beschreiben, typische Aufgaben zuordnen und erklären, wo Informatik und KI im (Berufs-)Alltag und in der Gesellschaft eine Rolle spielt.1, 13" (no Sem. given)
26. **11** — G10: "erklären, wie digitale Infrastrukturen (zB Identitätssysteme, Plattformen, eGovernment-Dienste, Soziale Medien) technisch aufgebaut sind und gesellschaftliche Teilhabe ermöglichen oder begrenzen, sowie die Chancen und Risiken digitaler Infrastrukturen begründet bewerten.6, 7, 13" (SS)
27. **11** — G11: "skizzenhaft Informatiksysteme unter Berücksichtigung unterschiedlicher vorgegebener Interessen und menschlicher Bedürfnisse gestalten, unter anderem unter ethischen und inklusiven Gesichtspunkten.3, 5, 7, 8" (WS)

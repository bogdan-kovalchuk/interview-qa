---
id: emb-elee-0142
title: "Zener regulator 9 V / 5.1 V / 390 Ω: how much current is left for the Zener with a 10 kΩ and a 1 kΩ load?"
description: "Zener regulator 9 V / 5.1 V / 390 Ω: how much current is left for the Zener with a 10 kΩ and a 1 kΩ load?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Question origin: lecture 58 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: AC circuits, reactance, phasors, impedance, filters and transformers; specific component values and circuits of the course can differ."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors and power supplies; specific component values and circuits of the course can differ."
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Choosing R1 so that at the highest load current a current not below the minimum still flows through the Zener diode (about 5 mA for Zener diodes up to 17 V, the V_Z measurement current from the datasheet), keeping the diode on the steep part of the reverse conduction curve; data are for Nexperia series, other manufacturers can have other numbers."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Parameters of the BZX84-C5V1: V_Z = 4.8–5.4 V at 5 mA, maximum r_dif of 480 Ω at 1 mA and 60 Ω at 5 mA; values for this series, not for every 5.1 V Zener diode."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The simple Zener regulator: the series resistor current I = (V_cap - V_Z)/R_limit is split between the load and the Zener diode, under light load most of it flows through the Zener diode, and when the load current is too large the Zener diode stops conducting and regulation is lost. The book does not cover the V_Z tolerance."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

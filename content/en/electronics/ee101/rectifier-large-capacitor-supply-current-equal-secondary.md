---
id: emb-elee-0175
title: "Can a rectifier with a large capacitor supply a DC current equal to the secondary's rated RMS current?"
description: "Can a rectifier with a large capacitor supply a DC current equal to the secondary's rated RMS current?"
track: electronics
section: ee101
level: junior
type: pitfall
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
    applicability: "Question origin: lecture 64 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: hammond-rectifier-guide
    title: "Hammond Manufacturing: Design Guide for Rectifier Use"
    url: https://www.hammfg.com/pdf/5c007.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "A transformer maker's guide: the relation between the DC load current and the AC current of the secondary for different rectifiers and filters (bridge with capacitor – I_DC = 0.62*I_AC, bridge with resistive load – 0.90, half-wave with capacitor – 0.28); diodes rated at least twice the output current; the RMS ripple current of the capacitor can be 2–3 times I_DC. These are guidelines for typical supplies, not an exact calculation for a specific circuit."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A diode with a capacitor filter turns on only when the input exceeds the capacitor voltage by about 0.7 V, so a larger capacitance gives shorter and taller charging-current peaks (simulation: up to ≈ 800 mA for 1000 µF and 100 Ω); the VA rating of a transformer is the nominal secondary voltage times the maximum secondary current. The book does not give the ratio of RMS to DC current."
---

## Short answer

TODO

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

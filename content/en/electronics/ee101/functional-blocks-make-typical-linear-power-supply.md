---
id: emb-elee-0151
title: "Which functional blocks make up a typical linear AC power supply?"
description: "Which functional blocks make up a typical linear AC power supply?"
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
    applicability: "Question origin: lecture 60 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A transformer scales AC voltage by the turns ratio and has a VA limit; a four-diode bridge rectifier drives load current in one direction in both half-cycles; a capacitor charges while the diode conducts and supplies the load between peaks, with ripple growing with load current; the secondary peak must exceed the output by two diode drops; a regulator can follow the filter. The book does not cover IC linear regulators."
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The relation i = C*dv/dt: a constant current through a capacitor gives a linear voltage change, i.e. ΔV = I*Δt/C; the section does not cover rectifiers, ESR or real load-current waveforms."
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA118A, April 2003, revised June 2008"
    applicability: "A linear regulator has a pass element managed by a feedback controller to keep the output voltage constant over input-voltage and load-current variation; the input-output difference at a given current is dissipated as heat, P_D = P_I - P_O; for a linear regulator Eff ≈ V_O/V_I when quiescent current is small. An application report about LDOs and their heating, not about switching converters."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

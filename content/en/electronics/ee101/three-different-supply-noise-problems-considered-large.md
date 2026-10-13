---
id: emb-elee-0182
title: "Which three different supply noise problems are considered, and why does one large capacitor not solve them all?"
description: "Which three different supply noise problems are considered, and why does one large capacitor not solve them all?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Question origin: lecture 66 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: libretexts-fiore-rectification
    title: "Fiore: Semiconductor Devices, 3.2 Rectification (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Full-wave bridge rectifier: two diodes conduct in each half-cycle, the load current has one direction in both half-cycles, and ripple is the variation of output voltage caused by capacitor discharge. Textbook level, not a datasheet for a specific bridge."
  - source_id: fiore-inductance-dc
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 9.2 Inductance and Inductors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/09:_Inductors/9.2:_Inductance_and_Inductors"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Inductance defined as a conductor's tendency to oppose a change in the current flowing through it, arising from the current's magnetic field. The section gives no numerical values for specific traces or wires."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-13
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Ideal-element relations: i = C*dv/dt for a capacitor (voltage changes at i/C) and v = L*di/dt for an inductor (a changing current gives a voltage). The document does not model resistance or parasitics of the ideal elements."
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
    accessed: 2026-10-13
    kind: official
    version: "Rev. C"
    applicability: "Switching-regulator application note: ESL limits an aluminum electrolytic at high frequencies, ESR, ESL and C form a resonant circuit, and ESR depends strongly on temperature; switching transistors and rectifiers generate EMI; IC supply pins are bypassed to a low-inductance ground with local ceramic or film capacitors. Take specific values from datasheets."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

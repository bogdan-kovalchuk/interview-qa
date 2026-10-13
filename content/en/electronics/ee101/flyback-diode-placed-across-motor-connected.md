---
id: emb-elee-0219
title: "Why is a flyback diode placed across a motor and how is it connected?"
description: "Why is a flyback diode placed across a motor and how is it connected?"
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
    applicability: "Question origin: lecture 73 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 4.7.1: the saturating switch – the transistor completes the circuit between the supply, the load and ground; for saturation the ratio of saturation current to base current must be much less than β; direct DC motor drive with a saturating BJT; a diode across the motor winding (snubbing diode) prevents the transistor from being damaged by the voltage spike when it turns off. The example numbers apply only to these circuits."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-13
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Ideal-element relations: i = C*dv/dt for a capacitor (voltage changes at i/C) and v = L*di/dt for an inductor (a changing current gives a voltage). The document does not model resistance or parasitics of the ideal elements."
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Diode models: the 0.7 V knee voltage of silicon as a behavioral approximation, the R_bulk resistance, dynamic resistance of about 26 mV / I. These are simplified models, not exact values for a specific device."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

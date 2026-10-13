---
id: emb-elee-0185
title: "Which breadboard measures reduce motor noise on the supply?"
description: "Which breadboard measures reduce motor noise on the supply?"
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
  - source_id: ti-slva959b-motor-driver-layout
    title: "TI: Best Practices for Board Layout of Motor Drivers (SLVA959B)"
    url: https://www.ti.com/lit/an/slva959b/slva959b.pdf
    accessed: 2026-10-13
    kind: official
    version: "SLVA959B, revised October 2021"
    applicability: "TI board layout recommendations for motor drivers: bulk capacitors near the supply input, bypass capacitors as close as possible to the pins, a short high-current loop, single-point power distribution and shared-impedance grounding. Rules for a printed circuit board with a driver, not for a breadboard."
  - source_id: ti-slvaft0-bulk-capacitor-sizing
    title: "TI: Bulk Capacitor Sizing for DC Motor Drive Applications (SLVAFT0)"
    url: https://www.ti.com/lit/an/slvaft0/slvaft0.pdf
    accessed: 2026-10-13
    kind: official
    version: "SLVAFT0, July 2024"
    applicability: "Bulk capacitor as a charge reservoir for motor current steps, and the estimate C > ΔI·T_PWM/ΔV with an example of 200 mA, 50 µs and 100 mV (100 µF). An idealized estimate without ESR; a specific driver and board need their own check."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

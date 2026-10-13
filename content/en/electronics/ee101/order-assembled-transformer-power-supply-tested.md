---
id: emb-elee-0180
title: "In what order is an assembled transformer power supply tested?"
description: "In what order is an assembled transformer power supply tested?"
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
    applicability: "Question origin: lecture 65 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
    applicability: "Full-wave bridge rectifier: two diodes conduct in each half-cycle, the load current has one direction in both half-cycles, and the load voltage is the secondary voltage minus two diode drops. Textbook level, not a datasheet for a specific bridge."
  - source_id: fiore-capacitors
    title: "Engineering LibreTexts: DC Electrical Circuit Analysis – A Practical Approach (Fiore), 8.2 Capacitance and Capacitors"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/DC_Electrical_Circuit_Analysis_-_A_Practical_Approach_(Fiore)/08:_Capacitors/8.2:_Capacitance_and_Capacitors"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Aluminum electrolytic capacitors are polarized: inserted backwards, they can fail catastrophically. The section also gives i = C*dv/dt; it does not cover ESR, ripple or rectifiers."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-13
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "LM340 (LM7805 family, V_O = 5 V) table: 7.5 V input required to maintain line regulation at T_J = 25 °C; dropout voltage 2 V typical at I_O = 1 A and T_J = 25 °C. The values apply to this regulator family, not to LDOs or other series."
  - source_id: openstax-rc-circuits
    title: "OpenStax University Physics Volume 2: 10.5 RC Circuits"
    url: https://openstax.org/books/university-physics-volume-2/pages/10-5-rc-circuits
    accessed: 2026-10-13
    kind: book
    version: "University Physics Volume 2"
    applicability: "Capacitor discharge through a resistor: after power is removed the capacitor gives up its charge through a resistance, not instantly. A physics textbook; specific times depend on the circuit."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

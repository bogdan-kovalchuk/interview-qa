---
id: emb-elee-0221
title: "Why is the typical active-mode β not used for a switch, and which motor current matters for component selection?"
description: "Why is the typical active-mode β not used for a switch, and which motor current matters for component selection?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Question origin: lecture 73 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
    accessed: 2026-10-14
    kind: official
    version: "2026.02.17"
    applicability: "Manufacturer guide (ROHM): during saturation switching the effective current gain decreases significantly; β_forced is chosen below the datasheet minimum h_FE (common starting point 5–10). General guide, not the datasheet of a specific transistor."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 4.2: small-signal transistors typically have β of 100 to 200, power transistors about 25 to 50; I_E = I_C + I_B. General picture, not for a specific transistor."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-14
    kind: book
    version: "Spring 2006"
    applicability: "University lecture notes: in saturation the relation between I_C and I_B is nonlinear; in the active region I_C = β·I_B. Not a manufacturer document."
  - source_id: ti-drv8231a
    title: "Texas Instruments DRV8231A: 3.7-A Brushed DC Motor Driver datasheet"
    url: https://www.ti.com/lit/ds/symlink/drv8231a.pdf
    accessed: 2026-10-14
    kind: official
    version: "SLVSFZ8A, revised January 2026"
    applicability: "TI driver datasheet: large currents at low speed, at start-up and with a stalled rotor. Figures in the tables are test conditions of the DRV8231A, not values for all motors."
  - source_id: ti-tida00786
    title: "Texas Instruments TIDA-00786: Ultra Small Brushed DC Motor Current Regulation (reference design)"
    url: https://www.ti.com/lit/ug/tiduay8/tiduay8.pdf
    accessed: 2026-10-14
    kind: official
    version: "2015"
    applicability: "TI reference design for a brushed motor: ISTART = VSUPPLY / RWINDING and steady-state current (VSUPPLY – VBEMF) / RWINDING; the real start-up current is lower because the motor starts to spin. Example for the DRV8871 at 12–24 V; the formulas are general, the design values are not."
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

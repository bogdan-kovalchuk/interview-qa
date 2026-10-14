---
id: emb-elee-0234
title: "What do `V_IL`, `V_IH`, `V_OL` and `V_OH` mean?"
description: "What do `V_IL`, `V_IH`, `V_OL` and `V_OH` mean?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Question origin: lecture 76 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
  - source_id: auburn-digital-voltages
    title: "Auburn University ELEC 3040/3050: Digital system voltages/currents and reading component data sheets (lab lecture notes)"
    url: https://www.eng.auburn.edu/~nelson/courses/elec3040_3050/LabLectures/DigitalElectricalQuantities_ARM.pdf
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "University lab-lecture notes: VOH (minimum output voltage in the high state) and VOL (maximum in the low state); VIH (minimum voltage read as high) and VIL (maximum read as low); noise margin VOH = VIH + V_noise; TTL values VIH = 2.0 V, VOH = 2.4 V, VIL = 0.8 V, VOL = 0.4 V, with unpredictable results between 0.8 V and 2.0 V. TTL values only, not other families."
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS181H"
    applicability: "Datasheet: Recommended Operating Conditions (at V_CC = 4.5 V: V_IH min = 3.15 V, V_IL max = 1.35 V) and Electrical Characteristics (at 4.5 V: V_OH min = 4.4 V at 20 µA, V_OL max = 0.1 V at 20 µA, V_OL max = 0.33 V at 4 mA over -40 to 85 °C). Values apply to the HC family."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

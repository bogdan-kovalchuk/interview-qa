---
id: emb-elee-0169
title: "The 3.3 V rail draws 100 mA from the 5 V rail, a separate 5 V load draws 50 mA, input 9 V. What are the losses in both regulators?"
description: "The 3.3 V rail draws 100 mA from the 5 V rail, a separate 5 V load draws 50 mA, input 9 V. What are the losses in both regulators?"
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
    applicability: "Question origin: lecture 63 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA118A, April 2003, revised June 2008"
    applicability: "In a linear regulator the pass element is always on and the input current is roughly equal to the output current; the power loss is P_D = P_I - P_O, almost all of it becoming heat; the maximum dissipation follows from (T_J - T_A)/θ_JA. An application report about LDOs; the formulas do not apply to switching converters, and θ_JA values depend on the package, board copper and T_J."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "LM340/LM7805 quiescent current (V_O = 5 V, V_I = 10 V, I_O ≤ 1 A) up to 8 mA at T_J = 25 °C; dropout 2 V (typical) at 1 A, input of at least 7.5 V to maintain line regulation. The values apply to the LM340/LM7805 family, not to other regulators (in particular not to a 3.3 V LDO)."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

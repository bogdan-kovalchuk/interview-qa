---
id: emb-elee-0154
title: "What are the losses and efficiency of a 9 V -> 5 V linear regulator at 100 mA and at 500 mA?"
description: "What are the losses and efficiency of a 9 V -> 5 V linear regulator at 100 mA and at 500 mA?"
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA118A, April 2003, revised June 2008"
    applicability: "In a linear regulator the pass element is always on, input current is roughly equal to output current, the power loss is P_D = P_I - P_O, and Eff = V_O/V_I for small quiescent current; with I_Q included Eff = V_O*I_O/(V_I*(I_O + I_Q)); the maximum dissipation follows from (T_J - T_A)/θ_JA, and package θ_JA in Fig. 5 (no airflow) ranges from 22–58 to 314–478 °C/W. An application report about LDOs; the formulas do not apply to switching converters, and θ_JA values depend on the package, board copper and T_J."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

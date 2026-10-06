---
id: emb-elee-0159
title: "How do you estimate the die temperature of a linear 12 V -> 5 V regulator at 0.2 A if `theta_JA` = 60 °C/W and `T_a` = 25 °C?"
description: "How do you estimate the die temperature of a linear 12 V -> 5 V regulator at 0.2 A if `theta_JA` = 60 °C/W and `T_a` = 25 °C?"
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
    applicability: "Question origin: lecture 61 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Dissipation of a linear regulator P_D = (V_i - V_o)*I_o, the definition of quiescent current I_q = I_i - I_o, the limit set by the maximum junction temperature and the formula P_D(max) = (T_Jmax - T_A)/R_θJA. The report is about LDOs; it does not cover switching converters and gives no θ_JA for a particular package."
  - source_id: ti-spra953d
    title: "Texas Instruments SPRA953D: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/an/spra953d/spra953d.pdf
    accessed: 2026-10-06
    kind: official
    version: "SPRA953D, March 2024"
    applicability: "Defines R_θJA on a standardized test board, gives T_J = T_A + R_θJA*Power, warns that R_θJA depends on the board and system and that applying it directly to a real board can give wrong values, and introduces R_θJA(effective). It gives no θ_JA value for a particular package or board."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0162
title: "Does an SMD chip on a DIP adapter reproduce the thermal conditions of a real board?"
description: "Does an SMD chip on a DIP adapter reproduce the thermal conditions of a real board?"
track: electronics
section: ee101
level: junior
type: pitfall
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
  - source_id: ti-spra953
    title: "Texas Instruments SPRA953: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/pdf/spra953
    accessed: 2026-10-06
    kind: official
    version: "SPRA953D, March 2024"
    applicability: "R_θJA depends not only on the package but also on the board and the measurement conditions (the board acts as a heat sink; in still-air JEDEC measurements 70–95 % of the power leaves through the test board rather than the package surface); PCB design has a 'strong' influence on R_θJA (Table 1-1); the notion of R_θJA(effective) for a device in a real system; Ψ_JT as a way to estimate T_J from the measured top-of-package temperature, which depends on board construction and airflow. A general note: it gives no values for specific boards or adapters."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Absolute Maximum Ratings note: for the DDPAK/TO-263 package θ_JA can be reduced by increasing the PCB copper area connected to the package: 50 °C/W with 0.5 in², 37 with 1 in², 32 with 1.6 in² or more; section 10.3: above 1 in² the improvement is small, and the minimum θ_JA for DDPAK on a board is 32 °C/W. The values were measured on a TI test board for this family; other boards and packages give other numbers."
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

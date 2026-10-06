---
id: emb-elee-0160
title: "How do you calculate the thermal resistance of a regulator with a heatsink?"
description: "How do you calculate the thermal resistance of a regulator with a heatsink?"
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
  - source_id: ti-sboa020
    title: "Texas Instruments (Burr-Brown) SBOA020 / AB-037: Mounting Considerations for TO-3 Packages"
    url: https://www.ti.com/lit/an/sboa020/sboa020.pdf
    accessed: 2026-10-06
    kind: official
    version: "SBOA020 (AB-037), March 1992"
    applicability: "Model T_J = T_A + P_D*θ_JA, θ_JA = θ_JC + θ_CH + θ_HA (θ_CH is the case-to-heat-sink joint); Table II: typical θ_CH for a TO-3 package (bare joint 0.5–1.0, grease 0.1–0.2, Kapton with grease 0.3–0.5, bare mica 1.0–1.5 °C/W); electrically insulating pads generally have a worse θ_CH than grease because of the dielectric layer. The numbers apply to TO-3; TO-220 values differ."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "Absolute Maximum Ratings note: P_DMAX = (T_JMAX - T_A)/θ_JA with T_JMAX 125 or 150 °C, thermal shutdown above 150 °C; with a heat sink θ_JA is the sum of the package θ_JC (4 °C/W for TO-3 and TO-220) and the heat sink's case-to-ambient resistance; for TO-220 the note gives θ_JA 54 °C/W while the Thermal Information table gives 23.9 °C/W (the values do not agree); first page: 'Tab/Case is Ground or Output'; quiescent current up to 6 mA (LM340A, 25 °C). The values apply to the LM340/LM7805 family, not to all regulators."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Power dissipated by a regulator P_D = (V_i - V_o)*I_o; quiescent (ground) current defined as the difference between input and output current I_q = I_i - I_o; the efficiency expression; P_D(max) = (T_Jmax - T_A)/R_θJA. The report is about LDOs: its numbers and examples apply to LDOs, not to the 7805."
  - source_id: ti-spra953
    title: "Texas Instruments SPRA953: Semiconductor and IC Package Thermal Metrics"
    url: https://www.ti.com/lit/pdf/spra953
    accessed: 2026-10-06
    kind: official
    version: "SPRA953D, March 2024"
    applicability: "R_θJA depends not only on the package but also on the board and the measurement conditions (the board acts as a heat sink; in still-air JEDEC measurements 70–95 % of the power leaves through the test board rather than the package surface); PCB design has a 'strong' influence on R_θJA (Table 1-1). A general note: it gives no values for specific boards or adapters."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

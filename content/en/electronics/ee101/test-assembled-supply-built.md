---
id: emb-elee-0167
title: "How do you test an assembled 5 V supply built on a 7805?"
description: "How do you test an assembled 5 V supply built on a 7805?"
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
    applicability: "Question origin: lecture 62 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "LM340/LM7805 table (V_O = 5 V, V_I = 10 V, T_J = 25 °C): output voltage 4.8–5.2 V for 5 mA ≤ I_O ≤ 1 A; load regulation for 5 mA ≤ I_O ≤ 1.5 A typically 10 mV, maximum 50 mV; line regulation for 7.5 V ≤ V_IN ≤ 20 V and I_O ≤ 1 A maximum 50 mV; input of at least 7.5 V to maintain line regulation; quiescent current up to 8 mA; characteristics measured with pulse techniques (t_w ≤ 10 ms, duty cycle ≤ 5 %), output changes due to heating must be taken into account separately. The values apply to the LM340/LM7805 family, not to other regulators."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Power dissipated by a regulator P_D = (V_i - V_o)*I_o. A report about LDOs; its numbers and examples do not apply to the 7805."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

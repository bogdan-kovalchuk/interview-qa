---
id: emb-elee-0168
title: "What should you check when adding a 3.3 V regulator fed from the 5 V rail?"
description: "What should you check when adding a 3.3 V regulator fed from the 5 V rail?"
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
  - source_id: ti-tps769
    title: "Texas Instruments TPS769: 100mA, 16V, Low-Dropout Linear Regulator (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/tps769.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVS203F, June 1999, revised January 2025"
    applicability: "The TPS769 family (including the TPS76933) in two die versions, legacy and new. Input: 2.7–10 V (legacy) or 2.5–16 V (new); output current up to 100 mA; TPS76933 dropout at 100 mA typically 98 mV (legacy) or 150 mV (new), maximum 200 and 218 mV; output capacitor of at least 4.7 µF with ESR 0.2–10 Ω (legacy) or 2.2–200 µF with ESR 0–3 Ω (new), input capacitor 1 µF, values assumed to derate to 50 % and the effective output capacitance must stay at 1 µF or more; DBV package (SOT-23, 5 pins): 1 – IN, 2 – GND, 3 – EN (low enables), 4 – FB/NC, 5 – OUT; RθJA of the new chip 178.6 °C/W. The values apply only to this family, not to other LDOs."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "LM340/LM7805 table (V_O = 5 V, V_I = 10 V): output voltage 4.75–5.25 V for 7.5 V ≤ V_IN ≤ 20 V, P_D ≤ 15 W and 5 mA ≤ I_O ≤ 1 A; TO-220 pins: 1 – INPUT, 2 – GND, 3 – OUTPUT. The values apply to the LM340/LM7805 family, not to other regulators."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Definition of dropout (the input-to-output difference at which regulation ceases as the input is reduced further); power dissipated by a regulator P_D = (V_i - V_o)*I_o. A report about LDOs; its numbers and examples refer to specific TI devices."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

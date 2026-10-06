---
id: emb-elee-0163
title: "How do you correctly connect a 7805 linear regulator?"
description: "How do you correctly connect a 7805 linear regulator?"
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
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVS056P, January 2015"
    applicability: "TO-220 pinout (KC, KCS, KCT): 1 – INPUT, 2 – COMMON (ground), 3 – OUTPUT; typical application with 0.33 µF at the input and 0.1 µF at the output, characteristics measured with these capacitors; the input capacitor is recommended for filtering input noise and the output one for decoupling the output, and an output capacitor is not needed for stability; input decoupling capacitors should be placed as close to the device as possible; recommended V_I for the uA7805 is 7–25 V (absolute maximum 35 V), dropout 2 V (typical) at 1 A, bias current 4.2 mA (typical) and 8 mA (maximum) at 25 °C, output voltage 4.8–5.2 V at 25 °C. The values apply to TI's uA78xx family, not to 7805s from other manufacturers."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "TO-220 pinout: 1 – INPUT, 2 – GND, 3 – OUTPUT; first page: 'Tab/Case is Ground or Output'; an output capacitor is not needed for stability but improves transient response (0.1 µF); if the regulator is more than about six inches from the supply filter an input capacitor of 0.1 µF or more is required; characteristics measured with 0.22 µF at the input and 0.1 µF at the output; a protection diode from output to input for large output capacitance (generally not needed up to 10 µF); disconnecting the GND pin alone. The values apply to the LM340/LM7805 family; other manufacturers may recommend otherwise."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0170
title: "Why does the output capacitor's ESR matter for some LDOs?"
description: "Why does the output capacitor's ESR matter for some LDOs?"
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
  - source_id: ti-slva115
    title: "Texas Instruments SLVA115A: ESR, Stability, and the LDO Regulator"
    url: https://www.ti.com/lit/an/slva115/slva115.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA115A, February 2020"
    applicability: "LDOs with a PMOS or PNP pass element: three open-loop poles (dominant, load pole, pass-device pole), the zero created by the output capacitor ESR `f_Z = 1/(2*pi*ESR*C_out)`, the lower and upper conditions on ESR, load-transient testing, an example with ringing for a 2.2 µF ceramic capacitor and a stable result with an added 1 Ω, and newer ceramic-stable LDOs. The note covers LDOs of these types; its numeric example for 0.1 Ω and 2.2 µF gives 72.3 kHz, which does not match the formula (about 723 kHz), so no numbers are taken from it."
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "A specific LDO: minimum capacitance 47 µF and ESR from 100 mΩ to 10 Ω, a note that ESR includes any external series resistance and the PCB trace resistance to C_O, and the conclusion that a higher ESR gives a larger droop at the start of a load step. Values apply only to the TPS752-Q1 and TPS754xx."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Section 10: the stable region of the compensation series resistance `CSR = R_ESR + R_add` depends on load current (tunnel of death), and an added resistor can be used if ESR is too small; the 0.2–9 Ω range is given as an example. A note about LDOs; the limits are an example, not universal."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0170
title: "Why does the output capacitor's ESR matter for some LDOs?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-slva115
    title: "Texas Instruments SLVA115A: ESR, Stability, and the LDO Regulator"
    url: https://www.ti.com/lit/an/slva115/slva115.pdf
  - source_id: ti-tps752q1-datasheet
    title: "Texas Instruments TPS752-Q1 datasheet"
    url: https://www.ti.com/lit/ds/symlink/tps752-q1.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

In an LDO with a `PMOS` or `PNP` pass element, the output capacitor's ESR introduces a zero that compensates for poles in the feedback loop, so the datasheet specifies an allowable ESR range and a minimum capacitance.[^ti-slva115][^ti-tps752q1-datasheet] An ESR that is too low (such as in ceramic capacitors) can leave the loop uncompensated, while an excessively high ESR can disrupt it at high frequencies; both cases risk instability. A high ESR also increases voltage sag during a load current step.[^ti-tps752q1-datasheet]

## Detailed explanation

TODO

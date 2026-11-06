---
id: emb-elee-0161
title: "What current flows through the first regulator in a 9 -> 5 -> 3.3 V cascade?"
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
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

The output of the first regulator delivers the sum of the direct 5 V rail load current and the input current of the second regulator (its 3.3 V load current plus quiescent current); the 9 V source additionally supplies the first regulator's own quiescent current.[^ti-slva079] For example, 100 mA drawn on the 5 V rail plus 50 mA on the 3.3 V rail totals roughly 150 mA through the first stage.

## Detailed explanation

TODO

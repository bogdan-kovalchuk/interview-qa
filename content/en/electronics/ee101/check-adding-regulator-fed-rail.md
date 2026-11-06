---
id: emb-elee-0168
title: "What should you check when adding a 3.3 V regulator fed from the 5 V rail?"
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
  - source_id: ti-tps769
    title: "Texas Instruments TPS769: 100mA, 16V, Low-Dropout Linear Regulator (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/tps769.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

Verify in the specific regulator datasheet that input voltage range and dropout permit 5 V operation, that maximum output current satisfies the 3.3 V load, and that required stability capacitors are present; also double-check package pinout and orientation, especially for SMD adapters. For example, a TPS76933 supports 2.5–16 V or 2.7–10 V input depending on silicon revision, delivers up to 100 mA, and uses a 5-pin SOT-23 package.[^ti-tps769] Another LDO may differ in pinout, current capability, and ESR stability criteria.

## Detailed explanation

TODO

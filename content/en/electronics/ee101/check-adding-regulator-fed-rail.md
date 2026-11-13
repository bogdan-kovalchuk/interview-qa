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

A second linear regulator powered from the 5 V rail is simply another load on that rail, but the suitability of a specific IC is determined by its datasheet. First, voltage headroom. Dropout is the input-to-output differential at which regulation ceases;[^ti-slva079] for the TPS76933 at 100 mA, it does not exceed 218 mV.[^ti-tps769] The 5 V rail from a 7805 may range between 4.75 and 5.25 V,[^ti-lm340] giving a worst-case headroom of `4.75 - 3.3 = 1.45 V`, which is well above the dropout voltage. The input range of 2.5–16 V (new) or 2.7–10 V (legacy) also accommodates 5 V.[^ti-tps769]

Second, current capability. For the TPS769, the recommended output current does not exceed 100 mA,[^ti-tps769] so if the 3.3 V rail draws 100 mA (as in qid:emb-elee-0169), the IC operates at its absolute limit, and a regulator with higher current capability should be chosen for design margin. This current is supplied by the 5 V rail and adds to the current of its own native loads (see qid:emb-elee-0161). Power dissipation in the new regulator is `P = (5 - 3.3)*0.1 = 0.17 W`,[^ti-slva079] and with `RθJA = 178.6 °C/W` (new chip, SOT-23-5), this results in a junction temperature rise of `0.17*178.6 ≈ 30 °C` above ambient.[^ti-tps769]

Third, capacitors. The TPS769 datasheet requires an output capacitor of at least 4.7 µF with an ESR of 0.2–10 Ω (legacy) or 2.2–200 µF with an ESR of 0–3 Ω (new) and a 1 µF input capacitor, where component values are assumed to derate by half and the effective output capacitance must remain at least 1 µF.[^ti-tps769] Without an appropriate output capacitor, an LDO can become unstable, and the capacitance of ceramic capacitors decreases significantly under DC bias, so nominal values should be selected with ample margin.

Fourth, pinout. In the SOT-23-5 package of the TPS769, pin 1 is IN, 2 is GND, 3 is EN, 4 is FB/NC, and 5 is OUT; EN enables the regulator with an active-low level, so it must be tied to ground rather than left floating or pulled high.[^ti-tps769] In a 7805 in the TO-220 package, pins 1–3 are input, ground, and output,[^ti-lm340] whereas in SOT-23-5 the output is pin 5 and pin 3 is EN, meaning pinouts cannot be transferred between different ICs. When using an SMD breakout board, it is especially easy to orient the package incorrectly.

**Common mistakes:**

- Assuming every 3.3 V regulator shares the same pinout and capacitor requirements.
- Failing to verify the regulator's maximum output current against the 3.3 V rail load.
- Leaving the EN pin floating without checking its active logic level.
- Overlooking the fact that the 3.3 V rail current flows through the upstream 5 V regulator.

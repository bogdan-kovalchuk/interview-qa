---
id: emb-elee-0165
title: "Why does a 7805 not give 5 V with an input of exactly 5 V?"
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
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
---

## Short answer

A 7805 is not an LDO: its dropout is typically 2 V at 1 A and `T_J = 25 °C`, and datasheets specify a minimum input of 7.5 V to guarantee line regulation.[^ti-lm340] An input of 5 V provides zero headroom over the nominal 5 V output, leaving the regulator dropped out and the output below 5 V.[^ti-slva079]

## Detailed explanation

A linear regulator places a pass element between the input and output, and that element remains functional only as long as there is sufficient voltage across it. The input-to-output voltage difference at which the circuit drops out of regulation as the input continues to decrease is called the dropout voltage.[^ti-slva079] Therefore, to obtain 5 V at the output, the input must exceed 5 V by at least the dropout voltage: with a 5 V input, the differential is 0 V, which is less than any dropout voltage.

The 7805 is not an LDO. In the TI datasheet for the LM340/LM7805 family, the dropout is typically 2 V at `I_O = 1 A` and `T_J = 25 °C`, and the input voltage required to maintain line regulation is 7.5 V (at `T_J = 25 °C` and `I_O ≤ 1 A`).[^ti-lm340] Thus, at 1 A the minimum input is approximately `5 + 2 = 7 V` typically, while the threshold guaranteed by the datasheet is 7.5 V. Dropout depends on current and temperature, so for other operating conditions one must consult the corresponding datasheet curves rather than relying on this single number.

**Example.** 5 V input, 1 A load. In the dropout region, the input-to-output differential equals the dropout voltage, so the output is approximately `V_in - V_dropout ≈ 5 - 2 = 3 V` (typically) and unregulated: its level is set by the input rather than by the internal reference voltage. At lower currents, the dropout voltage is different, but a 5 V output remains unattainable because there is zero headroom. Increasing the input to 9 V provides `9 - 5 = 4 V` of headroom; however, the power dissipation `P_D = (V_in - V_out)*I_out`[^ti-slva079] at 1 A rises to 4 W, compared to only 2.5 W at 7.5 V. Therefore, the input voltage is chosen with sufficient headroom above the minimum, but without excessive margin that turns into waste heat.

If the input is truly close to 5 V (for instance, a 5.5 V rail), the 7805 is unsuitable, and a low-dropout regulator is required; for comparing ripple troughs with dropout, see qid:emb-elee-0156.

**Common mistakes:**

- Assuming a 5 V regulator operates from a 5 V input: the 7805 requires several volts of headroom.
- Treating 2 V as a fixed dropout voltage: the datasheet specifies this value specifically for 1 A and 25 °C.
- Comparing the threshold against the average input voltage rather than the lowest instantaneous input voltage.
- Raising the input voltage excessively "just in case": the extra voltage turns into heat in the regulator.

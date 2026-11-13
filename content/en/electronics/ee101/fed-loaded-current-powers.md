---
id: emb-elee-0164
title: "A 7805 is fed from 9 V and loaded with 100 Ω. What are the current and powers?"
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
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
---

## Short answer

Output is 5 V, so load current is `I = 5/100 = 0.05 A` (50 mA) and resistor dissipation is `P = V²/R = 25/100 = 0.25 W` (0.5 W rated for margin). The regulator dissipates `(9 - 5)*0.05 = 0.2 W`[^ti-slva079] plus `V_in*I_q`: per the uA7805 datasheet `I_q` is a few milliamps, adding tens of milliwatts.[^ti-ua78] At 50 Ω, load current, resistor power, and `(V_in - V_out)*I_out` double (0.1 A, 0.5 W, 0.4 W), while `V_in*I_q` stays constant.

## Detailed explanation

The 7805 maintains 5 V at its output provided the input exceeds the output by at least the dropout voltage (typically 2 V at 1 A) and lies within the recommended 7–25 V operating range for the uA7805; a 9 V supply satisfies this requirement.[^ti-ua78] Therefore, 5 V drops across the 100 Ω resistor, giving `I = V/R = 5/100 = 50 mA`. The datasheet specifies an output voltage range of 4.8–5.2 V at 25 °C,[^ti-ua78] so the actual current falls between 48 and 52 mA, plus the component tolerance of the resistor itself.

Power dissipated in the resistor is `P_R = V²/R = 5²/100 = 0.25 W`. A resistor rated for exactly 0.25 W would operate at its absolute limit, so safety margin is added; a common guideline is a 2x derating factor (0.5 W rating), though this is a rule of thumb and appropriate margin depends on operating temperature and cooling conditions. In the regulator, the voltage difference `9 - 5 = 4 V` drops across that same 50 mA load current: `P_reg = (V_in - V_out)*I_out = 4*0.05 = 0.2 W`.[^ti-slva079] This is not the full picture: the regulator quiescent current per the uA7805 datasheet is typically 4.2 mA and up to 8 mA;[^ti-ua78] it flows from the input rail, adding `9*0.0042 ≈ 0.038 W` (up to `9*0.008 = 0.072 W`). Thus, the regulator typically dissipates about 0.24 W.

Checking the power balance: input current is `I_in = 50 + 4.2 = 54.2 mA`, input power drawn is `9*0.0542 = 0.488 W`, of which 0.25 W is delivered to the resistor and `0.488 - 0.25 ≈ 0.238 W` is dissipated in the regulator. Efficiency is `0.25/0.488 ≈ 51%`, which aligns with the formula `I_o*V_o/((I_o + I_q)*V_i)`[^ti-slva079] and does not exceed `V_out/V_in = 5/9 ≈ 56%`.

At 50 Ω, load current doubles: `I = 5/50 = 100 mA`, resistor power becomes `P_R = 25/50 = 0.5 W`, and regulator dissipation becomes `(9 - 5)*0.1 = 0.4 W` (neglecting `I_q`). A 0.5 W resistor would now operate at its maximum limit, requiring a higher-rated component such as 1 W.

**Common mistakes:**

- Calculating resistor dissipation using 9 V instead of 5 V: only the regulator output voltage appears across the resistor.
- Calculating regulator dissipation as `5*0.05` (load power) instead of `(V_in - V_out)*I_out`.
- Overlooking quiescent current `I_q`, which adds tens of milliwatts and reduces efficiency.
- Selecting a resistor rated for exactly 0.25 W without design margin.

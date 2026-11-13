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

A linear regulator is a series regulating element: almost the entire load current flows through it from input to output, with the voltage difference converted into heat. TI defines quiescent current (ground current) as the difference between input and output currents, `I_q = I_i - I_o`,[^ti-slva079] meaning `I_in = I_out + I_q`. In a 9 -> 5 -> 3.3 V cascaded chain, the second regulator is one of the loads on the first; hence its input current `I_in2 = I_3V3 + I_q2` adds to the current drawn by dedicated 5 V loads: `I_out1 = I_5V + I_3V3 + I_q2`. The 9 V source additionally supplies `I_q1`: `I_in1 = I_out1 + I_q1`.

Current does not scale by the voltage ratio. If one were to multiply 50 mA by `3.3/5`, the result would be 33 mA, but that applies only to an ideal switching converter that conserves power rather than current. In a linear regulator, current is conserved: that same 50 mA passes through both the second and the first regulator. The magnitude of `I_q` is specified in the datasheet: for a 5 V LM340A, it is up to 6 mA at 25 °C,[^ti-lm340] while for a 3.3 V regulator (often an LDO) it is given in its own datasheet, typically substantially less.

**Example.** `I_5V = 100 mA`, `I_3V3 = 50 mA`; assume `I_q2 = 1 mA` (illustrative value) and `I_q1 = 5 mA` (within the 6 mA specification). Then `I_in2 = 50 + 1 = 51 mA`, `I_out1 = 100 + 51 = 151 mA`, and `I_in1 = 151 + 5 = 156 mA`. Power dissipated in the first regulator: `P_1 = (9 - 5)*0.151 + 9*0.005 = 0.604 + 0.045 = 0.649 W` (equivalently, `9*0.156 - 5*0.151`). In the second: `P_2 = 5*0.051 - 3.3*0.05 = 0.09 W`. Useful load power is `5*0.1 + 3.3*0.05 = 0.665 W`, total power drawn from the source is `9*0.156 = 1.404 W`, yielding an efficiency of about 47%; the power balance matches: `0.665 + 0.649 + 0.09 = 1.404 W`.

Cascading regulators does not save energy; it merely redistributes heat. If the 3.3 V regulator were powered directly from 9 V, source current would remain 156 mA and total losses would remain 0.739 W, but the second regulator would dissipate about 0.29 W instead of 0.09 W.[^ti-slva079] Consequently, thermal design for the first regulator must account for the full current `I_out1`, rather than only the direct 5 V load current.

**Common mistakes:**

- Scaling the 3.3 V current into 5 V current using the voltage ratio.
- Neglecting `I_q` for both regulators.
- Calculating first-stage heating exclusively from the 5 V load while ignoring the second cascaded stage.

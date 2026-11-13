---
id: emb-elee-0169
title: "The 3.3 V rail draws 100 mA from the 5 V rail, a separate 5 V load draws 50 mA, input 9 V. What are the losses in both regulators?"
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

The 3.3 V regulator dissipates `P = (5 - 3.3)*0.1 = 0.17 W`. The 5 V regulator passes approximately 150 mA (50 mA local load plus 100 mA for the 3.3 V stage) and dissipates `P = (9 - 5)*0.15 = 0.6 W`. Combined dissipation is 0.77 W neglecting quiescent currents: cascading spreads heat across two packages, but does not reduce overall linear regulation loss.[^ti-slva118a]

## Detailed explanation

Problem assumptions: 100 mA is the current drawn by the 3.3 V stage from the 5 V rail, 50 mA is the load on the 5 V rail itself, the input is 9 V, and the regulators' internal quiescent currents are neglected. In a linear regulator, the pass element is always conducting, the input current approximately equals the output current, and losses `P_D = P_I - P_O` are almost entirely converted into heat.[^ti-slva118a] Therefore, current does not scale with the voltage ratio: the 3.3 V regulator draws 100 mA from the 5 V rail, while the 5 V regulator delivers `100 + 50 = 150 mA` to the rail and draws that same 150 mA from the 9 V source (see qid:emb-elee-0161).

The dissipation of each stage is the voltage drop across it multiplied by its current: `P_3V3 = (5 - 3.3)*0.1 = 0.17 W`, `P_5 = (9 - 5)*0.15 = 0.6 W`, totaling `0.77 W`. Power balance check: the power supplied by the source is `9*0.15 = 1.35 W`, the power delivered to the loads is `3.3*0.1 + 5*0.05 = 0.33 + 0.25 = 0.58 W`, and `0.58 + 0.77 = 1.35 W`. System efficiency is `0.58/1.35 ≈ 43%`.

Cascading yields no power savings. If both regulators were powered directly from 9 V, the 5 V regulator would supply 50 mA and the 3.3 V regulator 100 mA, giving `P_5 = (9 - 5)*0.05 = 0.2 W` and `P_3V3 = (9 - 3.3)*0.1 = 0.57 W`, again totaling `0.77 W`. The reason is that total current from the source remains the same (150 mA) and useful load power remains unchanged (0.58 W). Only the heat distribution shifts: 0.17 and 0.6 W in the cascade versus 0.57 and 0.2 W without it. This distinction is critical for package selection: based on `P_D ≤ (T_J - T_A)/θ_JA`[^ti-slva118a] and assumed conditions of `T_J = 125 °C` and `T_A = 40 °C`, dissipating 0.6 W requires `θ_JA ≤ 85/0.6 ≈ 142 °C/W`, whereas 0.17 W requires only `≤ 500 °C/W`.

Quiescent current introduces additional dissipation. In the LM340/LM7805 datasheet, it reaches up to 8 mA at `T_J = 25 °C`,[^ti-lm340] meaning the 7805 input current is up to `150 + 8 = 158 mA`, raising its dissipation to `9*0.158 - 5*0.15 ≈ 0.67 W` instead of 0.6 W; the total system loss increases by `9*0.008 = 0.072 W`.

**Common mistakes:**

- Counting the 5 V regulator current as only 50 mA while forgetting the 100 mA drawn by the 3.3 V stage.
- Converting 100 mA into 5 V rail current using the voltage ratio `3.3/5`.
- Assuming that powering 3.3 V from the 5 V rail rather than from 9 V reduces total power loss.
- Calculating the cascaded 3.3 V regulator's dissipation from 9 V rather than from the actual voltage drop `5 - 3.3`.

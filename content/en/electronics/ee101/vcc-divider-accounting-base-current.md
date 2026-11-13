---
id: emb-elee-0200
title: "`V_CC` = 5 V, 33 kΩ / 22 kΩ divider, `R_E` = 1 kΩ, β = 100. What are `V_B` and `I_E` accounting for base current?"
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
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

A divider with 33 kΩ to `V_CC` and 22 kΩ to ground yields `V_TH = 2 V` and `R_TH = 13.2 kΩ`. Accounting for base loading with `V_BE ≈ 0.7 V` and `β = 100`, the circuit gives `I_B ≈ 11.4 µA`, `V_B ≈ 1.85 V`, `V_E ≈ 1.15 V`, and `I_E ≈ 1.15 mA`. This is noticeably lower than the 1.3 mA predicted by an unloaded divider approximation.[^fiore-voltage-divider-bias]

## Detailed explanation

A divider with 33 kΩ to `V_CC` and 22 kΩ to ground is equivalent by Thevenin's theorem to a voltage source `V_TH = 5 V × 22 kΩ / 55 kΩ = 2 V` with internal resistance `R_TH = 33 kΩ ∥ 22 kΩ = 13.2 kΩ`.[^fiore-voltage-divider-bias] Without base current, base voltage would equal 2 V. However, the base draws current that flows through `R_TH`, dropping base voltage below `V_TH` by `I_B × R_TH`. This effect must be accounted for.

The base–emitter loop yields `V_TH = I_B × R_TH + V_BE + I_E × R_E`. Because `I_E = (β + 1) × I_B`, we have `I_B = (V_TH - V_BE) / (R_TH + (β + 1) × R_E) = 1.3 V / (13,200 Ω + 101,000 Ω) ≈ 11.4 µA`.[^fiore-bjt-basics] Next, `V_B = 2 V - 11.4 µA × 13.2 kΩ ≈ 2 V - 0.15 V = 1.85 V`, `V_E = V_B - 0.7 V ≈ 1.15 V`, and `I_E = 1.15 V / 1 kΩ ≈ 1.15 mA`. Consistency check: `I_E / I_B ≈ 1.15 mA / 11.4 µA ≈ 101`, as expected.

An idealized analysis neglecting base current yields `I_E = (V_TH - V_BE) / R_E = 1.3 mA`. The exact value is 1.15 mA, meaning the unloaded approximation is overstated by approximately 13%. The approximation `I_E ≈ (V_TH - V_BE) / R_E` is valid only when `R_E` is significantly larger than `R_TH / β`.[^fiore-voltage-divider-bias] Here `R_TH / β = 132 Ω` versus 1 kΩ, so the discrepancy is noticeable and cannot be ignored. The exact expression `I_E = (V_TH - V_BE) / (R_E + R_TH / (β + 1))` gives the same 1.15 mA.

Dependence on `β` also remains: the term `R_TH / (β + 1)` equals 131 Ω at `β = 100`, 259 Ω at `β = 50`, and 66 Ω at `β = 200`, resulting in `I_E ≈ 1.15 mA`, 1.03 mA, and 1.22 mA respectively. Dependence on `V_BE` is likewise apparent: an error of 0.1 V produces an error of ≈ 0.09 mA in `I_E`. Furthermore, `V_BE` varies with current and temperature: according to the exponential diode model, it increases by roughly 26 mV for each factor-of-e increase in current.[^fiore-bjt-ac-model]

**Common mistakes:**
- Assuming `V_B = V_TH` and taking `I_E = (V_TH - V_BE) / R_E` without checking base current: in this circuit that overestimates `I_E` by approximately 13%.
- Placing the 22 kΩ resistor in the top position: that would give `V_TH = 5 V × 33 / 55 = 3 V` instead of 2 V.
- Treating `V_BE = 0.7 V` as a universal constant: it is only a nominal approximation for silicon at a particular current level.

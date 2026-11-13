---
id: emb-elee-0203
title: "What is the differential emitter resistance `r_e`, and how do you estimate it?"
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
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

`r_e` is the small-signal (differential) resistance of the base-emitter junction at the operating point, equal to the reciprocal slope of the exponential I-V curve: `r_e = dV_BE/dI_E ≈ 26 mV / I_E` at 300 K. For `I_E = 1 mA`, this evaluates to approximately 26 Ω.[^fiore-bjt-ac-model]

## Detailed explanation

The base–emitter junction is a diode, so current depends exponentially on voltage: `I_C` = `I_S` × exp(`V_BE` / `V_T`), where `V_T` = kT/q. At 300 K, the quantity q/kT ≈ 38.6 1/V, meaning `V_T` ≈ 25.9 mV.[^fiore-bjt-ac-model] A small AC signal oscillates around the operating point, and the characteristic curve near that point can be treated as a straight line. Its slope defines conductance, and the dynamic resistance is the reciprocal of this slope: `r_e` = dV_BE/dI_E ≈ `V_T` / `I_E`.[^fiore-bjt-ac-model]

Numerical values. At `I_E` = 1 mA, we have `r_e` ≈ 25.9 mV / 1 mA ≈ 26 Ω; at 0.1 mA, it is ≈ 260 Ω; at 5 mA, it is ≈ 5.2 Ω. The textbook writes the formula in terms of `I_C`, but `I_E` = `I_C` + `I_B` and `I_B` = `I_C` / β, so for large β the difference between `I_E` and `I_C` is negligible.[^fiore-bjt-ac-model][^fiore-bjt-basics]

Application limits. The value 26 mV / `I_C` remains valid only as long as the AC component of the current remains small – in the textbook, a few percent of the quiescent current. It is slightly understated because it does not include the bulk resistance. At a constant `I_E`, the value `r_e` = `kT` / (`q` × `I_E`) increases with temperature by approximately 0.33% per kelvin (1/300 K ≈ 0.33%/K). A decrease in `r_e` with rising temperature would occur only at constant `V_BE`, where current increases because `I_S` depends strongly on temperature.[^fiore-bjt-ac-model]

**Common mistakes:**
- Taking the ratio `V_BE` / `I_E` (static resistance: 0.7 V / 1 mA = 700 Ω) instead of the slope: the dynamic resistance at the same point is approximately 27 times smaller.[^fiore-bjt-ac-model]
- Assuming that `r_e` is a discrete resistor that can be measured with an ohmmeter in circuit: an ohmmeter measures static resistance, not small-signal resistance.
- Ignoring bulk resistance and temperature when high precision is required.

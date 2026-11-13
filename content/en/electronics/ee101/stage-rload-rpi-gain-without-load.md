---
id: emb-elee-0215
title: "CE stage: `R_C` = 4.7 kΩ, `R_E` = 1 kΩ, `R_load` = 10 kΩ, β = 100, `r_pi` ≈ 2.6 kΩ. What is the gain with and without the load?"
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves
---

## Short answer

Loaded gain is `A_v = -β*R_C_ac/(r_pi + (β+1)*R_E)`, where `R_C_ac = R_C || R_load ≈ 3.20 kΩ`, yielding `A_v ≈ -3.09`; unloaded gain is `A_v ≈ -4.54`. Load resistance cannot be ignored because it reduces stage gain by nearly one-third.[^fiore-common-emitter-amplifier]

## Detailed explanation

**Conditions and model.** Assume that `R_E` is unbypassed, meaning it is fully present in the AC loop, and the signal generator has zero internal resistance. The output coupling capacitor acts as an AC short circuit in the midband, and the power supply rail serves as an AC ground; therefore, the AC collector resistance is the parallel combination of `R_C` and `R_load`: `R_C_ac = 4.7 kΩ || 10 kΩ = 47/14.7 ≈ 3.20 kΩ`.[^fiore-common-emitter-amplifier]

**Gain expression.** From `i_C = β·i_B` and `r'_e = 26 mV / I_C`, it follows that `r_pi = β·r'_e`.[^fiore-bjt-ac-model] The base AC voltage is `v_b = i_b*(r_pi + (β+1)*R_E)`, because the emitter current `(β+1)*i_b` flows through `R_E`, while the collector current `β*i_b` flows through `R_C_ac`. Hence `A_v = -β*R_C_ac/(r_pi + (β+1)*R_E)`. For β = 100 and `r_pi = 2.6 kΩ`, we have `r'_e = 26 Ω`, corresponding to `I_C = 1 mA`. Fiore formulates the same stage gain as `-r_C/(r'_e + r_E)` using the approximation `I_E ≈ I_C`.[^fiore-common-emitter-amplifier] With `r_E = 1 kΩ`, this evaluates to `-3197/1026 ≈ -3.12`, which is within 1% of the exact value -3.09.

**Numerical calculation.** Without load, `A_v = -100*4.7/(2.6 + 101*1) ≈ -4.54`. With load, `A_v = -100*3.20/103.6 ≈ -3.09`. Voltage gain is proportional to `R_C_ac`, while the denominator is independent of load resistance; thus, loading reduces the gain magnitude in direct proportion: 3.20/4.70 ≈ 0.68, or a 32% drop. Because `(β+1)*R_E = 101 kΩ` is much larger than `r_pi = 2.6 kΩ`, one can approximate `A_v ≈ -R_C_ac/R_E`, giving -3.20 and -4.70; for this stage, the approximation error is only about 4%.

**Limitations.** The formula is valid for small signals in the midband frequency range. Finite transistor output impedance (Early effect) is neglected here: collector current increases slightly with `V_CE`,[^fiore-bjt-collector-curves] and Fiore estimates `r'_C` to be on the order of 100 kΩ.[^fiore-common-emitter-amplifier] The parallel combination `4.7 kΩ || 100 kΩ ≈ 4.49 kΩ` would reduce gain magnitude by about 4.5%, which does not change the essential conclusion regarding loading effects.

**Common mistakes:**

- Using `R_load` instead of `R_C || R_load` for AC signal calculations.
- Assuming `R_E` has no impact on gain by neglecting the `(β+1)` factor in the denominator.
- Forgetting the negative sign: a common-emitter stage inverts phase, so `A_v` is negative.[^fiore-bjt-ac-model]

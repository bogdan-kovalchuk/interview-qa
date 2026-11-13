---
id: emb-elee-0217
title: "Why can the gain measured from the generator be lower than the gain calculated from the base?"
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

The generator output impedance forms a voltage divider with the stage input impedance, attenuating the signal arriving at the base: `A_v(gen) = A_v(base)*Z_in/(Z_in + R_gen)`.[^fiore-common-emitter-amplifier] Furthermore, the ideal base gain formula neglects the Early effect and high-frequency parasitic capacitances, so measured gain can deviate from calculation even without source attenuation.[^fiore-bjt-collector-curves][^fiore-bjt-ac-model]

## Detailed explanation

**Two different gains.** Calculated gain `A_v(base) = v_out/v_b` relates the output voltage directly to the voltage at the base terminal. In contrast, measurements typically evaluate `A_v(gen) = v_out/v_g`, where `v_g` is the open-circuit generator voltage and `R_gen` is its internal resistance. The stage input impedance `Z_in = R_B || β(r'_e + r_E)` forms a voltage divider with `R_gen`:[^fiore-common-emitter-amplifier] `v_b = v_g*Z_in/(Z_in + R_gen)`. Consequently, `A_v(gen) = A_v(base)*Z_in/(Z_in + R_gen)`, so whenever `R_gen` is non-zero, measured generator gain is strictly lower in magnitude than calculated base gain.

**Example.** For illustration, suppose `R_gen = 1 kΩ` and `Z_in = 5 kΩ`. The divider attenuation is `5/(5 + 1) ≈ 0.833`. For the unloaded stage from the preceding question where `A_v(base) ≈ -4.54` (see qid:emb-elee-0215), the generator-referenced gain is `A_v(gen) ≈ -3.78`, representing a 17% reduction. Input impedance increases with β and with `R_E` when `R_E` is unbypassed,[^fiore-common-emitter-amplifier] so a larger `R_E` reduces this attenuation effect.

**Why the base-referenced formula is approximate.** Calculating base gain using `r_C = R_C || R_load` neglects the finite transistor output resistance `r'_C`, which according to Fiore is on the order of 100 kΩ.[^fiore-common-emitter-amplifier] For `R_C = 4.7 kΩ`, paralleling it with `r'_C` yields 4.49 kΩ, lowering gain magnitude by about 4.5%. This stems from the Early effect: collector current increases slightly with `V_CE`, and extrapolating the active region curves intercepts the voltage axis at the Early voltage `V_A`.[^fiore-bjt-collector-curves] Furthermore, Fiore's small-signal model omits junction capacitances and is intended for low and midband frequencies, so calculated base gain also deviates at higher frequencies.[^fiore-bjt-ac-model]

**Common mistakes:**

- Assuming a signal generator delivers its full open-circuit voltage to the stage input: `R_gen` and `Z_in` always form an attenuating divider.
- Treating a 1 kΩ generator resistance as negligible: with an input resistance of 5 kΩ, it attenuates the signal by nearly 17%.
- Comparing measured generator gain directly against calculated base gain without factoring in the divider formed by `Z_in` and `R_gen`.

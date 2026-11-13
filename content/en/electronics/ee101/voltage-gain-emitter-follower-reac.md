---
id: emb-elee-0204
title: "What is the voltage gain of an emitter follower at `I_E` = 1 mA and `R_E,ac` = 1 kΩ?"
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
  - source_id: fiore-common-collector
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

The voltage gain is `A_v ≈ R_E,ac / (r_e + R_E,ac) = 1000 / (26 + 1000) ≈ 0.975`, where `R_E,ac = R_E || R_load` and `r_e ≈ 26 mV / I_E = 26 Ω`.[^fiore-common-collector][^fiore-bjt-ac-model] The output signal is in phase with the input, with zero phase inversion.[^fiore-common-collector]

## Detailed explanation

The formula is derived from the small-signal model. The AC emitter current `i_e` flows through `r_e` and `R_E,ac`, so the base voltage is `v_B` = `i_e` × (`r_e` + `R_E,ac`), and the emitter voltage is `v_E` = `i_e` × `R_E,ac`. Dividing the two yields `A_v` = `v_E` / `v_B` = `R_E,ac` / (`r_e` + `R_E,ac`).[^fiore-common-collector] At `I_E` = 1 mA, we have `r_e` ≈ 26 mV / 1 mA = 26 Ω, so `A_v` = 1000 / 1026 ≈ 0.975.[^fiore-bjt-ac-model] Consequently, about 2.5% of the input voltage drops across the base–emitter junction itself.

The dependence on `R_E,ac` illustrates how sensitive this formula is. If a 1 kΩ load is connected in parallel with `R_E` = 1 kΩ, then `R_E,ac` = 500 Ω and `A_v` = 500 / 526 ≈ 0.95. With `R_E,ac` = 100 Ω, the gain drops to 100 / 126 ≈ 0.79. The smaller `R_E,ac` is compared to `r_e`, the greater the signal loss.

Formula limitations. This is the ratio `v_E` / `v_B`, meaning it is referenced to the base rather than to the signal generator. A source with high internal resistance combined with the stage input resistance (including the base bias divider) attenuates the signal arriving at the base. In a textbook example with different component values, the gain from the base is 0.944, but accounting for a 1 kΩ source reduces it to about 0.85.[^fiore-common-collector] In addition, `r_e` depends on current and temperature, so the value 0.975 corresponds to 1 mA and 300 K; under different operating conditions, both `r_e` and the voltage gain change.[^fiore-bjt-ac-model]

**Common mistakes:**
- Using `R_E` instead of `R_E,ac` for a loaded follower: with a parallel 1 kΩ load, `A_v` ≈ 0.95, not 0.975.
- Assuming the gain is exactly 1: since `r_e` > 0, `A_v` is strictly less than 1.
- Taking 0.975 as the overall stage gain with the signal source: the source resistance and base divider reduce the net gain.

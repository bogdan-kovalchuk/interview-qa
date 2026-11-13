---
id: emb-elee-0214
title: "What are the small-signal parameters of a BJT at `I_C` ≈ 1 mA and β = 100?"
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
---

## Short answer

Transconductance is `g_m = I_C/V_T ≈ 1 mA / 26 mV ≈ 38.5 mS`, while dynamic emitter resistance is `r'_e = 26 mV / I_C ≈ 26 Ω`. The base input resistance without external emitter degeneration is `r_pi = β/g_m = β*r'_e ≈ 2.6 kΩ`.[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier]

## Detailed explanation

The small-signal model of a BJT at low and midband frequencies is constructed around the dynamic resistance of the base–emitter junction. This resistance is set by the quiescent collector current: `r'_e` = 26 mV / `I_C`. For `I_C` = 1 mA, it equals 26 Ω.[^fiore-bjt-ac-model] The figure 26 mV is an approximation of the thermal voltage `V_T` = kT/q at 300 K (≈ 25.9 mV), so this value is approximate. The reciprocal of this resistance is the transconductance `g_m` = `I_C`/`V_T`, which Fiore terms transconductance; at 25.9 mV it equals 38.6 mS, and at 26 mV it is 38.5 mS.

The base input resistance depends on β. When there is no external emitter resistance (`r_E` = 0), the base sees an input resistance of β·`r'_e` = 100·26 Ω = 2.6 kΩ. This is identical to β/`g_m`, because `g_m` = 1/`r'_e`.[^fiore-bjt-ac-model][^fiore-common-emitter-amplifier] If an emitter resistor `R_E` is present, the base input resistance increases to β(`r'_e` + `R_E`), which is significantly larger.[^fiore-common-emitter-amplifier]

**Example:** at `I_C` = 2 mA, we have `g_m` ≈ 77 mS, `r'_e` ≈ 13 Ω, and base input resistance without `R_E` is ≈ 1.3 kΩ for β = 100. Doubling the current doubles `g_m` and halves `r'_e`. Changing β at a fixed `I_C` does not alter `g_m`, because `g_m` = `I_C`/`V_T` is independent of β.[^fiore-bjt-ac-model]

This model neglects junction capacitances and lead inductances, making it valid only at low and midband frequencies.[^fiore-bjt-ac-model] Semiconductor bulk resistance is not included in `r'_e`, making the estimated resistance slightly understated. Furthermore, the reverse saturation current `I_S` varies with temperature, causing `r'_e` to shift with thermal variations.[^fiore-bjt-ac-model]

**Common mistakes:**

- Assuming that `g_m` depends on β: `g_m` = `I_C`/`V_T` is completely independent of β.[^fiore-bjt-ac-model]
- Treating 26 mV/`I_C` as an exact number: it is an approximation that excludes bulk resistance and changes with temperature.[^fiore-bjt-ac-model]
- Forgetting `R_E` when calculating base input impedance: with `R_E`, the resistance is β(`r'_e` + `R_E`).[^fiore-common-emitter-amplifier]

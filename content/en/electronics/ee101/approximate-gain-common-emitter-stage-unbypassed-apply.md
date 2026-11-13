---
id: emb-elee-0209
title: "What is the approximate gain of a common-emitter stage with an unbypassed `R_E`, and when does it apply?"
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias
---

## Short answer

With an unbypassed emitter resistor satisfying `R_E ≫ r_e` and load `R_L ≫ R_C`, the voltage gain is approximately `A_v ≈ -R_C/R_E`, where the negative sign denotes phase inversion. An unbypassed `R_E` reduces overall gain but stabilizes it against variations in `r_e` and β while lowering distortion. DC operating point stability is maintained by `R_E` regardless of AC bypassing.[^fiore-common-emitter-amplifier][^fiore-emitter-bias]

## Detailed explanation

The exact gain expression for a common-emitter stage with an unbypassed `R_E` is `A_v = -r_C/(r_e + R_E)`, where `r_C = R_C || R_L`. It is derived as follows: the AC voltage at the base equals the voltage drop produced by the AC emitter current across `r_e + R_E`, and the AC collector current nearly equals the AC emitter current because β is large. The signal source is assumed to have low internal impedance compared to the stage input impedance, so nearly all source voltage appears at the base.[^fiore-common-emitter-amplifier][^fiore-common-collector-amplifier] If `R_E ≫ r_e` and `R_L ≫ R_C`, the `r_e` term can be neglected, yielding `A_v ≈ -R_C/R_E`. Parameter β does not appear in this expression, so the gain is immune to variations in β; this approximation is valid for large β where `I_E ≈ I_C`.

Example: let `R_C = 4.7 kΩ`, `R_E = 470 Ω`, and `I_E ≈ I_C = 1 mA`, so that `r_e = 26 mV / 1 mA = 26 Ω`. The exact expression yields `-4700/(470 + 26)` ≈ -9.5, while the approximation gives `-4700/470 = -10`. The error is about 5%, because `R_E/r_e` ≈ 18. If `R_E = 47 Ω` instead, the exact value is `-4700/73` ≈ -64, whereas the approximation gives -100: an error exceeding 50%, because `R_E/r_e` ≈ 1.8. Thus, the approximation becomes more accurate as `R_E` grows relative to `r_e`, and the boundary should be chosen based on acceptable tolerance.

An unbypassed `R_E` provides DC bias stability. Provided `R_E ≫ R_B/β`, collector current `I_C` is virtually independent of β, keeping the operating point stable.[^fiore-emitter-bias] A bypass capacitor across `R_E` acts as an open circuit for DC, preserving DC stabilization. For AC signals, bypassing shorts out `R_E`: `r_E = 0`, and the gain becomes `-r_C/r_e`, which can be tens of times higher. However, gain then depends directly on `r_e` (and hence on bias current and temperature), while distortion increases significantly.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Applying `A_v = -R_C/R_E` without verifying that `R_E ≫ r_e`.
- Ignoring `R_L` connected in parallel with `R_C`.
- Assuming that bypassing `R_E` degrades DC operating point stability: the bypass capacitor affects only AC operation.

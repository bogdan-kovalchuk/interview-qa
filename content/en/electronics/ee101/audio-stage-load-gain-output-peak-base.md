---
id: emb-elee-0229
title: "Audio stage: `R_C` = 4.7 kΩ, `R_E` = 1 kΩ, `I_E` ≈ 1 mA, 10 kΩ load. What are the gain and the output for 20 mV peak at the base?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
---

## Short answer

The voltage gain is `A_v = -(R_C||R_load)/(r'_e + R_E) = -3197/1026 ≈ -3.1`, where `r'_e = 26 mV / 1 mA = 26 Ω`. The output is approximately 62 mV peak with phase inversion, provided 20 mV peak is present directly at the base.[^fiore-common-emitter-amplifier][^fiore-bjt-ac-model]

## Detailed explanation

This is a common-emitter amplifier with an unbypassed `R_E`. At signal frequencies, coupling capacitors act as short circuits, so the AC collector load resistance is the parallel combination of `R_C` and the load: `r_C = R_C || R_load = 4700 * 10000 / (4700 + 10000) ≈ 3197 Ω`. There is no bypass capacitor across the emitter resistor, so the denominator contains `R_E = 1 kΩ` directly. The voltage gain is expressed as `A_v = -r_C / (r'_e + R_E)`.[^fiore-common-emitter-amplifier]

The resistance `r'_e` is determined by the collector current: `r'_e = 26 mV / I_C`. For `I_E = 1 mA` and `I_C ≈ I_E`, we get `r'_e = 26 Ω`.[^fiore-bjt-basics] The value 26 mV is the rounded figure for 25.9 mV at 300 K, and `r'_e` varies with temperature.[^fiore-bjt-ac-model] Thus, `r'_e + R_E = 26 + 1000 = 1026 Ω`.

Voltage gain: `A_v = -3197 / 1026 ≈ -3.116`, meaning a magnitude of about 3.1, or `20 * log10(3.116) ≈ 9.9 dB`. The negative sign indicates a 180° signal phase inversion.[^fiore-common-emitter-amplifier] Output: `3.116 * 20 mV ≈ 62.3 mV peak`, that is, `-62.3 mV peak` relative to the base signal. Without a load, the denominator remains the same while `r_C = 4700 Ω`, which would yield a gain of `-4700 / 1026 ≈ -4.6`; the 10 kΩ load reduces it by roughly one-third.

Limitations. The formula gives the gain from the base to the output, so 20 mV peak is assumed directly at the base. If 20 mV is specified at a signal generator with internal impedance, the signal at the base is attenuated by the voltage divider formed with the stage's input impedance. According to Fiore, `Z_in(base) = β(r'_e + R_E)`; with β = 100, this is `100 * 1026 ≈ 103 kΩ`, but β is not specified in the problem statement, and in parallel with the base bias resistors the stage input impedance will be lower, so the attenuation of this divider cannot be evaluated without those parameters.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Taking `r_C = R_C` without placing the load resistor in parallel.
- Ignoring `R_E` in the denominator: `-3197 / 26 ≈ -123` instead of `-3.1` corresponds to a fully bypassed circuit.
- Assuming that 20 mV at the generator output is identical to 20 mV at the base, neglecting the input divider.

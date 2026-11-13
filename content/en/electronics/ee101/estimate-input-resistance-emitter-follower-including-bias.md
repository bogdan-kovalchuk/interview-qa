---
id: emb-elee-0205
title: "How do you estimate the input resistance of an emitter follower including the bias divider?"
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
  - source_id: fiore-common-collector-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.4 Common Collector Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.4:_Common_Collector_Amplifier
  - source_id: fiore-ac-model-bjt
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
---

## Short answer

Looking into the base, the input impedance of the emitter follower is `Z_in(base) = β*(r_e + r_E)`, where `r_E = R_E || R_load` is the AC emitter load resistance. For `β = 100`, `r_e = 26 Ω`, and `r_E = 1 kΩ`, this base impedance is approximately 103 kΩ. The bias divider resistors appear in parallel with this input: with a 20 kΩ Thevenin bias equivalent, total stage input impedance is approximately 16.7 kΩ.[^fiore-common-collector-amplifier]

## Detailed explanation

The input resistance of an emitter follower is measured looking into the base, as that is where the signal is applied and the bias divider is connected. Base current is approximately β times smaller than emitter current, so any resistance in the emitter circuit is reflected into the base multiplied by β: `Z_in(base) = β*(r_e + r_E)`, where `r_E = R_E ∥ R_load` is the AC emitter load resistance.[^fiore-common-collector-amplifier] Here `r_e` is the dynamic resistance of the base–emitter junction, `r_e ≈ 26 mV / I_C`. When `I_C` is around 1 mA, `r_e` is approximately 26 Ω.[^fiore-ac-model-bjt]

As an example, take `β = 100`, `r_e = 26 Ω`, and the AC emitter resistance `r_E = 1 kΩ`. Then `Z_in(base) = 100*(26 + 1000)` ≈ 103 kΩ. The bias resistors `R_B = R1 || R2` appear in parallel with this resistance, so `Z_in = R_B || Z_in(base)`. With `R_B = 20 kΩ`, we obtain `Z_in = 1/(1/20000 + 1/102600)` ≈ 16.7 kΩ.[^fiore-common-collector-amplifier] The bias divider caps the input impedance: even with infinite β, the stage input resistance cannot exceed `R_B`.

The formula highlights what governs the result. In a follower, `R_E` must not be bypassed: the output is taken from the emitter, and a bypass capacitor would short the signal to ground. The external load reduces the AC resistance at the emitter, `r_E = R_E ∥ R_load`, and with it `Z_in(base)`; therefore, `R_E` in the formula refers specifically to the AC resistance `R_E ∥ R_load`, not just the DC resistor value.[^fiore-common-collector-amplifier] This expression is a small-signal approximation for low- and mid-frequency operation.[^fiore-ac-model-bjt] A source with internal resistance `R_S` does not alter `Z_in`, but forms a voltage divider `Z_in/(Z_in + R_S)` with it, which must be evaluated separately for accurate signal calculations.[^fiore-common-collector-amplifier]

**Common mistakes:**

- Using the nominal value of `R_E` for `r_E` while ignoring parallel load resistance, or forgetting the factor of β or the parallel `R_B`.
- Assuming that a large β alone guarantees a high stage input resistance: `R_B` sets an upper bound on input impedance.
- Ignoring source impedance when evaluating the signal voltage at the input.

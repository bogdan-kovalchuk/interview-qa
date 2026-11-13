---
id: emb-elee-0231
title: "How do you debug an assembled transistor audio amplifier?"
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

Without a signal, measure `V_B`, `V_E`, and `V_C` to confirm active mode operation: in a silicon NPN, `V_BE` is approximately 0.7 V and the collector voltage is higher than the base.[^fiore-bjt-basics] Next, apply a small sine wave near 1 kHz and compare amplitude and phase: a common-emitter stage inverts the signal.[^fiore-common-emitter-amplifier] Increase the input until the output starts clipping, then back off into the linear range. Finally, sweep the frequency to observe the effect of coupling capacitors.

## Detailed explanation

Debugging begins without a signal, because an amplifier operates properly only when each transistor is biased in the active mode: the emitter junction forward-biased and the collector junction reverse-biased. In a silicon NPN transistor, base–emitter voltage in this mode is approximately 0.7 V, and the collector must be higher than the base.[^fiore-bjt-basics] If `V_BE` is near zero, the transistor is in cutoff; if `V_CE` drops to tenths of a volt, it is in saturation. The collector voltage limits are defined by `V_CE(cutoff) = V_CC` and `V_CE(sat)`.[^fiore-bjt-dc-load-line]

**Example:** `V_CC = 9 V`, measured values are `V_E = 1.00 V`, `V_B = 1.70 V`, `V_C = 5.0 V`. Then `V_BE = 1.70 - 1.00 = 0.70 V` (emitter junction is forward-biased), and `V_CB = 5.0 - 1.70 = 3.3 V` means the collector junction is reverse-biased. Therefore, the transistor is in active mode. If `V_B` equals `V_E`, then `V_BE = 0` and the transistor is in cutoff.

Next, apply a small sine wave near 1 kHz, where the reactance of coupling capacitors is small and they barely attenuate the signal.[^fiore-common-emitter-amplifier] A common-emitter stage inverts the signal, that is, shifts its phase by 180°; the negative sign in `A_v = -r_C / (r'_e + r_E)` reflects this inversion. The expected value is estimated using `r'_e = 26 mV / I_C`.[^fiore-bjt-ac-model] With `I_C = 1 mA` and `r_C = 2.2 kΩ`, we have `r'_e ≈ 26 Ω`, and with an emitter bypassed by a capacitor, `|A_v| ≈ 2200 / 26 ≈ 85`. Without this capacitor and with `r_E = 234 Ω`, gain drops to `2200 / (26 + 234) ≈ 8.5`, a ten-fold reduction.

At low frequencies, coupling capacitors produce a rolloff. With `R = 10 kΩ` and C = 100 nF, the cutoff is around 159 Hz, and at 100 Hz the output is lower by approximately 5.5 dB.[^fiore-ac-circuit-analysis] Therefore, if the amplifier works well at 1 kHz but rolls off at low audio frequencies, the first check should be the coupling capacitor values rather than the transistor.

The input signal amplitude is increased gradually until the output begins to clip. Clipping on one side typically means that the operating point is shifted toward one of the extremes, while clipping on both sides indicates that the input is too large for the stage. After that, reduce the amplitude back into the linear range and measure gain there.

**Common mistakes:**

- Measuring gain without verifying DC voltages: in cutoff or saturation, the result is meaningless.
- Treating phase inversion as a malfunction: a common-emitter stage inverts the signal.
- Concluding that an amplifier is defective based on loss at 100 Hz without checking coupling capacitors.

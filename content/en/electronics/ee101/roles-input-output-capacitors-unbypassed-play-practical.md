---
id: emb-elee-0228
title: "What roles do the input and output capacitors and the unbypassed `R_E` play in a practical common-emitter audio amplifier?"
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
---

## Short answer

The input capacitor blocks DC base bias voltage from reaching the source, while the output capacitor blocks DC collector voltage from reaching the load; both pass the AC signal.[^fiore-common-emitter-amplifier] An unbypassed `R_E` lowers the voltage gain, but it also stabilizes gain against variations in `r'_e` and reduces distortion.[^fiore-common-emitter-amplifier]

## Detailed explanation

A common-emitter amplifier amplifies an AC signal superimposed on a DC bias established by resistors. To prevent the signal source and load from disturbing this bias, coupling capacitors are placed at the input and output. For direct current, they act as open circuits, so the input source does not alter the bias or shift the operating point; for the AC signal, their reactance must be small compared to surrounding resistances at the signal frequency, allowing the signal to pass.[^fiore-common-emitter-amplifier] The output capacitor does the same for the load: DC collector voltage does not reach the load or the subsequent stage.

An unbypassed `R_E` is a resistor in the emitter (emitter degeneration) that provides negative feedback. If `C_E` bypasses it, the emitter is at AC ground, and `A_v = -r_C / r'_e`: gain is maximized, but it depends on `r'_e`, and therefore on collector current and temperature. Without a bypass capacitor, `A_v = -r_C / (r'_e + R_E)`, where `r_C` is the parallel combination of the collector resistor and load.[^fiore-common-emitter-amplifier][^fiore-bjt-ac-model]

Numerical consequences. Without a load, with `R_C = 4.7 kΩ`, `R_E = 1 kΩ`, and `r'_e = 26 Ω` (current around 1 mA), `A_v = -4700 / 1026 ≈ -4.6` without bypass, and `-4700 / 26 ≈ -181` with a complete bypass. That is, `R_E` reduces voltage gain by a factor of approximately 39 (`1026 / 26 ≈ 39`). However, the denominator `r'_e + R_E` is far less sensitive to `r'_e`: if `r'_e` increases by 10% (from 26 to 28.6 Ω), the unbypassed denominator increases by only 0.25% (from 1026 to 1028.6), whereas with a full bypass it increases by 10%.[^fiore-common-emitter-amplifier]

Capacitances must be chosen such that their reactance at the signal frequency is small compared to surrounding resistances; otherwise, the signal attenuates at low frequencies. Therefore, input and output capacitors are sized together with the resistances they see, rather than in isolation.[^fiore-common-emitter-amplifier] An unbypassed `R_E` does not change this, but it reduces gain by adding resistance to the denominator.

**Common mistakes:**

- Believing that the output capacitor passes the DC collector voltage to the load.
- Expecting the same gain from an unbypassed `R_E` as with a bypass capacitor: the difference is roughly a factor of 39.
- Using `A_v = -R_C / r'_e` without `R_E` when `C_E` is absent.

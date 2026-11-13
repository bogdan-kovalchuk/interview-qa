---
id: emb-elee-0207
title: "Which resistance sets the cutoff of a coupling capacitor between two stages?"
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
  - source_id: fiore-multi-stage-amplifiers
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.6 Multi-Stage Amplifiers"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.6:_Multi-Stage_Amplifiers
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
---

## Short answer

The cutoff frequency is determined by the total resistance seen by the coupling capacitor, which is the sum of the source stage's output impedance and the load stage's input impedance, rather than `R_E` alone.[^fiore-multi-stage-amplifiers][^fiore-common-emitter-amplifier] For this high-pass RC network, `f_c = 1/(2*pi*R*C)`, and gain drops by 3 dB at `f_c` relative to the midband level.[^fiore-ac-circuit-analysis]

## Detailed explanation

A coupling capacitor between stages forms a high-pass filter together with the impedances it sees on both sides. To the left, it sees the output impedance of the driving stage. For a common-emitter stage, `Z_out ≈ R_C`, because the internal resistance of the collector current source is high.[^fiore-common-emitter-amplifier] To the right, it sees the input impedance of the succeeding stage, which acts as the load for the first stage.[^fiore-multi-stage-amplifiers] For AC signals, these two resistances appear in series with the capacitor, so `R = Z_out + Z_in` and `f_c = 1/(2*pi*R*C)`.[^fiore-ac-circuit-analysis]

For example: let `R_C = 4.7 kΩ` be the collector resistor of the first stage, the input impedance of the second stage be `Z_in = 10 kΩ` (which already includes its `R_B ∥ β(r_e + r_E)`), and `C = 1 µF`. Then `R = 14.7 kΩ`, and `f_c = 1/(2*pi*14700*1e-6)` ≈ 10.8 Hz. If one mistakenly uses only `R_E = 470 Ω` of the second stage instead, the calculation gives `1/(2*pi*470*1e-6)` ≈ 339 Hz, which is roughly thirty times higher. However, `R_E` is not in series with `C`: it enters only indirectly through `Z_in` of the second stage, so an estimate based on `R_E` alone is incorrect.

At the cutoff frequency, the voltage gain is 3 dB below the midband level, and below cutoff it rolls off at approximately 6 dB per octave.[^fiore-ac-circuit-analysis] Therefore, midband gain formulas such as `A_v = -r_C/(r_e + r_E)` are valid only well above `f_c`, where attenuation across the coupling capacitor is negligible.[^fiore-common-emitter-amplifier]

**Common mistakes:**

- Estimating the cutoff frequency from `R_E` alone when it is not directly in series with the coupling capacitor.
- Neglecting the driving stage's output impedance when calculating the total resistance seen by the capacitor.
- Forgetting that `f_c` depends on both `C` and the total loop resistance `R`, not on capacitance alone.

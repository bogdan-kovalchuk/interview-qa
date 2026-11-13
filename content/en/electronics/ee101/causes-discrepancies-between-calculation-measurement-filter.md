---
id: emb-elee-0126
title: "What causes discrepancies between the calculation and the measurement of an RL filter?"
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
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
  - source_id: vishay-ihlp-2525cz-l7
    title: "Vishay Dale: IHLP-2525CZ-L7 inductors datasheet"
    url: https://www.vishay.com/docs/34254/ihlp-2525cz-l7.pdf
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
---

## Short answer

Winding resistance (DCR) and generator output resistance add to the series resistance, reducing low-frequency transmission in a low-pass filter and shifting `f_c`. Inductance tolerance also shifts `f_c` because `f_c` is inversely proportional to L; inductor datasheets often specify tolerances up to ± 20%.[^vishay-ihlp-2525cz-l7] Long leads and probe capacitance introduce parasitic elements causing additional poles or resonance;[^tektronix-abcs-probes] inter-turn coil capacitance produces self-resonance (SRF).[^vishay-inductors-primer]

## Detailed explanation

The calculation model of an RL filter accounts only for nominal values of L and R: `f_c = R/(2*pi*L)`.[^aac-alternating-current] For R = 1 kΩ and L = 330 µH, this is `f_c ≈ 482 kHz`. Everything omitted from the model appears as a discrepancy between calculation and measurement: winding resistance, a source with non-zero output resistance, component tolerance, and parasitic layout elements.

**Resistance in the circuit.** The winding resistance R_w is the DCR, which is the DC resistance of the inductor wire.[^vishay-inductors-primer] It, along with the generator output resistance R_s, sits in series with L, so the total series resistance is `R_t = R_s + R_w + R`. Then `H(0) = R/R_t`, and `f_c' = R_t/(2*pi*L)`. In an example with assumed values R_s = 50 Ω (typical generator output resistance) and R_w = 10 Ω: `R_t = 1060 Ω`, `H(0) = 1000/1060 ≈ 0.943`, which is about -0.51 dB already at low frequencies, and `f_c' = 1060/(2*pi*330e-6) ≈ 511 kHz` instead of 482 kHz. The cutoff here is the point where the signal drops by 3 dB relative to this new, reduced DC level.

**Inductance tolerance.** In the inductor datasheet, inductance is specified with a tolerance; for example, in the IHLP-2525CZ-L7 series it is ± 20% at 100 kHz.[^vishay-ihlp-2525cz-l7] Because `f_c ~ 1/L`, for L = 330 µH a ±20% tolerance gives a range from 264 to 396 µH, meaning `f_c` ranges from `1000/(2*pi*396e-6) ≈ 402 kHz` to `1000/(2*pi*264e-6) ≈ 603 kHz`. The nominal 482 kHz lies within this interval and is not a guaranteed value; resistors also have tolerances.

**Parasitic elements at high frequencies.** Long leads add inductance, while the oscilloscope probe adds tip capacitance that loads the source and reduces the measurement system bandwidth; ground lead inductance combined with probe capacitance causes ringing at the frequency determined by their L and C.[^tektronix-abcs-probes] In addition, the distributed capacitance of the inductor itself creates a self-resonance SRF, above which the inductor behaves as a capacitor; for more details, see qid:emb-elee-0125.[^vishay-inductors-primer] Ultimately, the frequency response departs from the ideal. Therefore, before searching for arithmetic errors, one should first recalculate the model using the actual R_t and the tolerance range of L, and only then look for parasitic effects.

**Common mistakes:**

- Comparing the measurement with a calculation based on nominal L and R without adding DCR and generator output resistance.
- Treating inductance as an exact number: a ± 20% tolerance shifts `f_c` by roughly the same amount.
- Measuring `-3 dB` from 0 dB when low-frequency transmission is already reduced by series resistance.

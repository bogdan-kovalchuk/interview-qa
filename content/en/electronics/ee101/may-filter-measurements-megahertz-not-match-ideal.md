---
id: emb-elee-0125
title: "Why may RL filter measurements at megahertz not match the ideal model?"
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
---

## Short answer

For R = 1 kΩ and L = 330 µH, `f_c = R/(2*pi*L) ≈ 482 kHz`, so `10*f_c` reaches approximately 4.8 MHz. At these frequencies, the inductor's distributed capacitance (its SRF) and winding resistance alter its behavior, while breadboard capacitance, probe loading, and instrument bandwidth also distort the measurement.[^vishay-inductors-primer] If the measurement curve becomes non-monotonic, check the circuit model and layout rather than just arithmetic.

## Detailed explanation

The ideal model consists of only two components: an inductor L and a resistor R, with the output taken across R. For this circuit, `H = R/(R + j*2*pi*f*L)` and `f_c = R/(2*pi*L)`.[^aac-alternating-current] With R = 1 kΩ and L = 330 µH, we have `f_c = 1000/(2*pi*0.00033) ≈ 482 kHz`. At `10*f_c ≈ 4.82 MHz`, the inductor reactance is `X_L = 2*pi*4.82e6*330e-6 ≈ 10 kΩ = 10*R`, so the ideal `|H| = 1/sqrt(1 + 10²) ≈ 0.0995`, or about -20 dB. Such a "clean" picture holds only as long as real components behave like ideal L and R.

A real inductor is not just an inductance. Each turn of wire acts like a capacitor plate, and the total distributed capacitance appears in parallel with the inductance. This parallel combination resonates at its self-resonant frequency (SRF); above the SRF, capacitive reactance dominates, and the inductor behaves like a capacitor.[^vishay-inductors-primer] The lower the distributed capacitance for a given inductance, the higher the SRF, and vice versa.[^vishay-inductors-primer] Because `SRF = 1/(2*pi*sqrt(L*C))`, for the same `C`, a larger `L` yields a lower SRF, so an inductor of hundreds of µH reaches its limit earlier than a small inductor of a few µH.

**Illustrative calculation** (10 pF is an assumption, not a specific course inductor parameter): for `C_dist = 10 pF`, `SRF = 1/(2*pi*sqrt(L*C)) = 1/(2*pi*sqrt(330e-6*10e-12)) ≈ 2.77 MHz`. This is below 4.82 MHz, so at `10*f_c` such an inductor is already beyond its inductive region: its impedance no longer grows as `2*pi*f*L`, attenuation stops increasing, and it may start decreasing again. This is precisely how a non-monotonic frequency response curve appears. The real SRF must be taken from the specific inductor datasheet.

Other non-idealities exist as well. Winding resistance (DCR) adds to the series resistance of the circuit.[^vishay-inductors-primer] Probe and layout capacitance appears in parallel with the output: if it equals 15 pF (also an assumption), `X_C = 1/(2*pi*4.82e6*15e-12) ≈ 2.2 kΩ`, which is comparable to R = 1 kΩ, meaning the output divider is already modified. Instrument bandwidth limits and amplitude inaccuracy at megahertz frequencies also enter into the measurement. Therefore, a discrepancy at `10*f_c` is not necessarily a calculation error, but rather operation beyond the applicability limits of the two-element model.

**Common mistakes:**

- Applying the formula `f_c = R/(2*pi*L)` at all frequencies without comparing the operating frequency against the SRF from the inductor datasheet.
- Neglecting parallel probe and layout capacitance at the circuit output when R is relatively large.
- Treating a non-monotonic response curve as measurement noise rather than as evidence of resonance or parasitic elements.

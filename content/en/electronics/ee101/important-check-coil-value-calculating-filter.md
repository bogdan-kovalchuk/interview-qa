---
id: emb-elee-0124
title: "Why is it important to check the coil value before calculating an RL filter?"
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
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
---

## Short answer

The cutoff frequency `f_c = R/(2*pi*L)` is inversely proportional to `L`, and microhenries versus millihenries differ by a factor of 1000, so a unit prefix mistake shifts the calculation by three orders of magnitude. For example, with `R = 1 kΩ`, cutoff is approximately 482 kHz at 330 µH and approximately 482 Hz at 330 mH.[^fiore-ac-circuit-analysis]

## Detailed explanation

**Where the dependence comes from.** The cutoff of an RL filter occurs where the inductive reactance equals the resistance `R`: `X_L = 2*pi*f*L = R`.[^fiore-ac-circuit-analysis] Hence `f_c = R/(2*pi*L)`. Inductance is in the denominator, so cutoff varies inversely with it: a 1000-fold larger `L` yields a 1000-fold lower cutoff for an unchanged `R`. The prefixes µH (`10^-6`) and mH (`10^-3`) differ by precisely a factor of one thousand, so a single confused letter in the marking, calculation, or calculator entry shifts the cutoff frequency by three orders of magnitude.

**Example.** Let `R = 1 kΩ`. For `L = 330 µH`, we have `f_c = 1000/(2*pi*330e-6) ≈ 482 kHz`, and for `L = 330 mH` it is `≈ 482 Hz`, exactly 1000 times lower. The consequence for a low-pass filter (output across the resistor): a `1 kHz` signal in the first case passes almost without attenuation (`≈ 0 dB`), whereas in the second case `|V_out/V_in| = 1/sqrt(1 + (1000/482)^2) ≈ 0.43`, or `≈ -7.2 dB`. Even without a prefix mistake, neighboring nominal values cause significant differences: for `2.2 mH`, the cutoff is `≈ 72 kHz`, which is 6.7 times lower than for `330 µH`, because `2200/330 ≈ 6.7`.

**What the nominal value still hides.** A real inductor has an inductance tolerance and intrinsic winding resistance that adds to `R`.[^fontys-passive-hf] Furthermore, an inductor is only usable below its self-resonant frequency (SRF).[^fontys-passive-hf] Above the SRF, the capacitive reactance of the parallel distributed capacitance dominates, and the inductor behaves like a capacitor; lower distributed capacitance for the same inductance yields a higher SRF.[^vishay-inductors-primer] Therefore, a cutoff in the hundreds of kilohertz, as in the 330 µH example, must be cross-checked against that inductor's self-resonant frequency. One should verify the nominal value against component markings and datasheets, and if necessary measure with an LCR meter and measure winding resistance with an ohmmeter, before calculating the filter.

**Common mistakes:**

- Confusing `µH` and `mH` (or `kΩ` and `Ω`) when substituting into `f_c = R/(2*pi*L)`: the result shifts by entire orders of magnitude.
- Calculating strictly by nominal values without accounting for tolerance and winding resistance: the actual cutoff differs.
- Failing to sanity-check the result: a cutoff in the hundreds of kilohertz for a small inductor or in the tens of hertz for a large inductor should prompt a careful review.

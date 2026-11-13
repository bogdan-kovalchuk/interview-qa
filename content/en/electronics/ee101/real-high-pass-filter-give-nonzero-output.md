---
id: emb-elee-0121
title: "Why does a real RL high-pass filter give a nonzero output at DC and not pass \"any\" high frequency?"
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
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
---

## Short answer

Because of winding resistance `r_L`: at DC an ideal inductor is a short circuit, leaving a voltage divider `V_out = V_in*r_L/(R + r_L)` rather than zero for an unloaded coil output.[^fontys-passive-hf] At very high frequencies, parasitic capacitance causes self-resonance (SRF), above which capacitive reactance dominates and the inductor behaves like a capacitor.[^vishay-inductors-primer] The measurement bandwidth is further limited by the oscilloscope and probe.[^tektronix-abcs-probes]

## Detailed explanation

**A real inductor is more than just `L`.** The equivalent circuit of a real inductor includes an ideal inductance, series winding resistance `r_L`, and parallel parasitic capacitance `C_d`.[^fontys-passive-hf] Therefore, the output "across the inductor" is the voltage across the `r_L` + `L` branch. At DC, the reactive impedance equals zero, leaving only `r_L`, which forms a resistive voltage divider with `R`. For example, with `R = 1 kΩ` and `r_L = 50 Ω`: `V_out/V_in = 50/1050 ≈ 0.0476`, which is ≈ 4.8% of the input (`-26.4 dB`), rather than 0 as predicted by the ideal model.

**How this alters the frequency response.** The transfer function becomes `(r_L + j*2*pi*f*L)/(R + r_L + j*2*pi*f*L)`. It has a zero at `r_L/(2*pi*L)` and a pole at `(R + r_L)/(2*pi*L)`. For `L = 10 mH`, the zero is at ≈ 796 Hz and the pole is at ≈ 16.7 kHz instead of the ideal 15.9 kHz, because the total series resistance `R + r_L` now enters the cutoff expression. Below the zero, the response does not roll off further, but plateaus at ≈ 4.8%. At 16.7 kHz, the amplitude reaches ≈ 0.707 of the passband plateau level, while the phase falls short of +90° at low frequencies and approaches 0° at DC.

**Why it does not pass "any" high frequency.** The parallel capacitance `C_d` together with the inductance creates a self-resonance. Above its frequency (self-resonant frequency, SRF), capacitive reactance dominates and the inductor behaves like a capacitor.[^vishay-inductors-primer] Therefore, a practical inductor is useful only below this limit.[^fontys-passive-hf] At high frequencies, the effective winding resistance also increases due to the skin effect and core losses.[^kuphaldt-high-pass-filters] Consequently, a real inductor-based high-pass filter has a "passband window" between the cutoff and the inductor's self-resonance, rather than an infinite passband. A separate limitation arises from the measurement setup itself: the oscilloscope and probe have their own bandwidth limits (falling by 3 dB at their cutoff), and the probe additionally loads the circuit with its tip capacitance.[^tektronix-abcs-probes]

**Common mistakes:**

- Expecting near-zero output from an RL high-pass filter at DC: a real inductor has finite `r_L`, so the output is set by a voltage divider rather than being zero.
- Failing to add `r_L` (and the source output resistance) to `R` when calculating cutoff.
- Interpreting the high-frequency roll-off as a circuit design flaw when it may stem from inductor self-resonance or probe and oscilloscope bandwidth limits.

---
id: emb-elee-0120
title: "Why does the output of an RL high-pass filter (the coil voltage) have a positive phase relative to the source?"
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
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
---

## Short answer

Current in an RL circuit lags the source voltage by `arctan(2*pi*f*L/R)`, while the voltage across L leads that current by 90°. Therefore, the output phase `φ = 90° - arctan(2*pi*f*L/R)` is always positive: around +90° at low frequencies, +45° at `f_c`, and approaching 0° at high frequencies.[^fiore-ac-circuit-analysis]

## Detailed explanation

**Circuit and two shifts.** In an RL high-pass filter, the source is connected in series with resistor `R` and inductor `L`, and the output is taken across the inductor.[^kuphaldt-high-pass-filters] The same current `I` flows through both elements, so it is convenient to calculate the output phase in two steps. For an ideal inductor, `v = L*di/dt`, which means the voltage across it leads its own current by 90°.[^fiore-ac-circuit-analysis] The current itself is determined by the total impedance `R + j*2*pi*f*L`, whose reactive part is positive, so `I` lags the source voltage by an angle between 0° and 90°.

**Total phase.** Combining these two shifts: `φ = 90° - arctan(X_L/R)`, where `X_L = 2*pi*f*L`.[^fiore-ac-circuit-analysis] The magnitude gives the same divider: `|V_out/V_in| = X_L/sqrt(R^2 + X_L^2)`. At the cutoff frequency `f_c = R/(2*pi*L)`, the inductive reactance equals `R`, so the amplitude is `1/sqrt(2) ≈ 0.707` (`-3.01 dB`), and the phase is exactly +45°. The output always leads the input, but never by more than 90°. An RC high-pass filter where the output is taken across the resistor has the exact same phase profile: +90° at low frequencies, +45° at the cutoff frequency, and near 0° at very high frequencies.[^fiore-ac-circuit-analysis]

**Example.** Let `R = 1 kΩ`, `L = 10 mH`; then `f_c = 1000/(2*pi*0.01) ≈ 15.9 kHz`. At `0.1*f_c ≈ 1.59 kHz`, the ratio `X_L/R = 0.1`, so the phase is `90° - 5.71° = +84.29°`, and `|V_out/V_in| ≈ 0.0995` (`-20.04 dB`). At `f_c`, we have +45° and 0.707. At `10*f_c ≈ 159 kHz`, the phase is `+5.71°`, and the amplitude is `≈ 0.995` (`-0.04 dB`).

**Model limitations.** Everything above applies to an ideal inductor without a load. A real inductor has winding resistance and parasitic capacitance.[^fontys-passive-hf] Due to winding resistance, the voltage across the inductor terminals at low frequencies no longer approaches +90°: at DC it is not zero, and the phase approaches 0° (see qid:emb-elee-0121). If the output is taken across the resistor instead of the inductor, the phase becomes negative (`-arctan(X_L/R)`), which corresponds to an RL low-pass filter.

**Common mistakes:**

- Reasoning that "current lags, so the output must lag as well": the output is the voltage across L, which leads current by 90° and is only partially offset by the lag of the current itself.
- Assuming that the voltage across the coil is always exactly +90° relative to the source: this is only the limit for `f` much lower than `f_c` and for an ideal inductor.
- Taking the output across `R` instead of `L`: that produces an RL low-pass filter with a phase from 0° to -90°.

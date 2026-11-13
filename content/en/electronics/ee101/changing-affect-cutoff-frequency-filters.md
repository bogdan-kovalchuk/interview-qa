---
id: emb-elee-0122
title: "How does changing R affect the cutoff frequency of RC and RL filters?"
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
  - source_id: kuphaldt-low-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.2 Low-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.02:_Low-pass_Filters
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
---

## Short answer

In opposite directions. In an RC filter `f_c = 1/(2*pi*R*C)`, so increasing `R` lowers the cutoff frequency. In an RL filter `f_c = R/(2*pi*L)`, so increasing `R` raises the cutoff frequency: doubling `R` doubles `f_c`.[^fiore-ac-circuit-analysis][^kuphaldt-low-pass-filters]

## Detailed explanation

**Where the formula comes from.** The first-order cutoff occurs where the reactance equals the resistance `R`: at that point the output is 70.7% of the passband level, or `-3 dB`.[^kuphaldt-low-pass-filters] For RC, this is `X_C = 1/(2*pi*f*C) = R`, yielding `f_c = 1/(2*pi*R*C)`.[^fiore-ac-circuit-analysis] For RL, the condition `X_L = 2*pi*f*L = R` yields `f_c = R/(2*pi*L)`. This formula is easily verified: in the `R` and `L` voltage divider, the LPF transfer function magnitude is `R/sqrt(R^2 + X_L^2)`, which indeed equals `1/sqrt(2)` when `X_L = R`.

**Why the directions are opposite.** Reactances behave oppositely: `X_C` decreases with frequency, while `X_L` increases. In an RC circuit, with a larger `R`, the capacitor must reach a larger reactance to match the resistor, which happens at a lower frequency: the cutoff shifts downward. In an RL circuit, with a larger `R`, the inductor must develop a larger `X_L`, which only occurs at a higher frequency: the cutoff shifts upward. These relationships are identical for low-pass and high-pass filters of the same topology because they share the same `f_c`.

**Example.** RC with `C = 100 nF`: with `R = 1.6 kΩ` we get `f_c = 1/(2*pi*1600*1e-7) ≈ 995 Hz`, and with `R = 3.2 kΩ` it is `≈ 497 Hz`, exactly half. RL with `L = 10 mH`: with `R = 1 kΩ` we get `f_c = 1000/(2*pi*0.01) ≈ 15.9 kHz`, and with `R = 2 kΩ` it is `≈ 31.8 kHz`, exactly double.

**What `R` actually is.** The formula includes the total resistance seen by the reactive element: the resistor plus the source output resistance, and for RL, also the inductor's winding resistance.[^fontys-passive-hf] Load resistance also alters the filter response, and the unloaded formula holds only for an open-circuit output.[^kuphaldt-low-pass-filters] Therefore, "changing R" in practice means changing the sum of all such resistances.

**Common mistakes:**

- Transferring RC intuition to RL: in RL circuits, increasing `R` raises the cutoff rather than lowering it.
- Confusing `f_c` in hertz with `ω_c` in rad/s: `ω_c = R/L`, `f_c = ω_c/(2*pi)`.
- Ignoring source output resistance, winding resistance, and loading: the real cutoff differs from calculations based solely on the resistor's nominal value.

---
id: emb-elee-0058
title: "What is the impedance of an ideal inductor and an ideal capacitor?"
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
  - source_id: aac-ideal-lc-impedance
    title: "All About Circuits: Series R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-r-l-and-c/
---

## Short answer

For an ideal inductor, `Z_L = j*ω*L = j*X_L`, where `X_L = ω*L` is positive. For an ideal capacitor, `Z_C = 1/(j*ω*C) = -j/(ω*C) = -j*X_C`, where `X_C = 1/(ω*C)` is positive. Because `ω = 2π*f`, inductive impedance has an angle of `+90°` and capacitive impedance has an angle of `-90°` at frequencies `f > 0`.[^aac-ideal-lc-impedance]

## Detailed explanation

In sinusoidal steady state, an ideal inductor and an ideal capacitor have purely imaginary impedances, but with opposite signs. If `ω = 2π*f`, then `Z_L = j*ω*L`, whereas `Z_C = 1/(j*ω*C) = -j/(ω*C)`. The reactances `X_L = ω*L` and `X_C = 1/(ω*C)` are positive scalar quantities; the sign appears in the complex expression for impedance.[^aac-ideal-lc-impedance]

The sign is related to phase: for an ideal inductor, voltage leads current by `90°`, while for a capacitor, current leads voltage by `90°`. The frequency dependence also differs. For a constant inductance, `X_L` increases proportionally to `f`, whereas `X_C` decreases inversely proportionally to `f`. These relationships assume linear ideal elements without losses or parasitic parameters.[^aac-ideal-lc-impedance]

Example: for an ideal inductor with `L = 10 mH` at `f = 1 kHz`, `ω = 2π*1000 rad/s`, so `X_L ≈ 62.8 Ω` and `Z_L ≈ j*62.8 Ω`. For a capacitor with `C = 10 µF` at the same frequency, `X_C ≈ 15.9 Ω`, whence `Z_C ≈ -j*15.9 Ω`. These are not two ordinary resistors: sign and phase govern how they sum in a circuit. Calculations use exact component ratings for ideal elements rounded to three significant digits.[^aac-ideal-lc-impedance]

In real components, the inductor winding has resistance and parasitic capacitance, while the capacitor exhibits losses and lead resistance. Ideal formulas are therefore approximations within the operating range, and near self-resonance the component behavior can differ substantially. For `f = 0`, the capacitor formula as a sinusoidal phasor is a limiting case: its impedance approaches infinity, whereas the inductive impedance approaches zero.[^aac-ideal-lc-impedance]

**Common mistakes:**

- Omitting the minus sign in `Z_C` and assigning an inductive phase sign to a capacitor.
- Confusing the reactance `X_C` as a positive quantity with the imaginary part of the impedance `-j*X_C`.
- Treating ideal formulas as an exact model of a physical component at any arbitrary frequency.[^aac-ideal-lc-impedance]

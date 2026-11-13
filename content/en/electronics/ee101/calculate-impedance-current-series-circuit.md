---
id: emb-elee-0078
title: "How do you calculate the impedance and current of a series RL circuit?"
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
---

## Short answer

For a series RL circuit at frequency `f`, inductive reactance is `X_L = 2π*f*L`, and total impedance is `Z = R + jX_L`. The current phasor is calculated as `I = V/Z`. Its magnitude is `V/√(R² + X_L²)`, and the current lags the source voltage by `atan2(X_L, R)`.[^aac-alternating-current]

## Detailed explanation

In sinusoidal steady state, a resistor is ideally modeled by a real resistance `R`, and an inductor by a reactance `jX_L`, where `X_L = 2π*f*L`. Because the components are connected in series, their complex impedances add: `Z = R + jX_L`. The magnitude equals `√(R² + X_L²)`, and the angle is `atan2(X_L, R)`. The complex form is necessary because the voltages across R and L have different phases.[^aac-alternating-current]

By Ohm's law for phasors, `I = V_in/Z`. If an RMS source voltage and linear components are given, the result is an RMS current phasor. Its magnitude is `V_in/|Z|`, and its phase lags the source voltage by the impedance angle. The inductor voltage `V_L = I*jX_L` leads the current by 90°, whereas the resistor voltage is in phase with the current.[^aac-alternating-current]

Calculation example for `R = 40 Ω`, `L = 79.58 mH`, `f = 60 Hz`, and `V_in = 10 V RMS`:
```text
X_L = 2π*60*0.07958 ≈ 30 Ω
Z = 40 + j30 Ω; |Z| = 50 Ω; angle(Z) ≈ 36.87°
|I| = 10/50 = 0.20 A RMS; angle(I) ≈ -36.87°
```
These values are consistent with the impedance triangle: `R`, `X_L`, and `|Z|` form a right triangle.[^aac-alternating-current]

**Common mistakes:**
- Adding `R + X_L` as ordinary scalar numbers while ignoring phase.
- Substituting millihenries without converting to henries.
- Confusing RMS and peak values of the source.

The model assumes an ideal inductor and linear operation. A real inductor has winding resistance and parasitic parameters; its inductance can also vary with frequency and current. Therefore, for accurate measurements, use a component model or its datasheet.[^aac-alternating-current]

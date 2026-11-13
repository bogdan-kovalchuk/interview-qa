---
id: emb-elee-0064
title: "Series RC circuit: R = 100 Ω, X_C = 75 Ω, 10 V RMS source. Why do the voltages across R and C (8 V and 6 V) not add up to 14 V?"
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
  - source_id: aac-series-rc
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
---

## Short answer

For `R = 100 Ω` and `X_C = 75 Ω`, the circuit impedance is `Z = 100 - j75 Ω`, with a magnitude of `125 Ω` and an angle of approximately `-36.87°`. With a `10 V RMS` source, the current magnitude is `0.08 A`. The voltages `8 V` across R and `6 V` across C are shifted by 90° relative to each other, so their phasor sum has a magnitude of `10 V` rather than `14 V`.[^aac-series-rc]

## Detailed explanation

In a series RC circuit, instantaneous voltages across the resistor and capacitor do not reach their peaks simultaneously, so their RMS magnitudes cannot be added as scalars. The voltage across the resistor is in phase with the current, while the voltage across an ideal capacitor lags the current by 90°. Consequently, these two voltage phasors are mutually orthogonal.[^aac-series-rc]

For the specified values, `Z = R - jX_C = 100 - j75 Ω`. Its magnitude equals `sqrt(100² + 75²) = 125 Ω`, so the current is `10/125 = 0.08 A RMS`. The voltage across the resistor is `I*R = 8 V RMS`, and across the capacitor `I*X_C = 6 V RMS`. Quadrature addition gives `sqrt(8² + 6²) = 10 V RMS`, which matches the source voltage.[^aac-series-rc]

This result is a direct consequence of Kirchhoff's voltage law in phasor form: instantaneous voltages at every instant algebraically satisfy the loop equation with the source voltage, and in sinusoidal steady state complex phasors are used for calculations. The resistive and capacitive components have different phase angles, which is why the magnitude of their sum does not equal the sum of their magnitudes. For other reactive elements, the phasor direction differs, but the rule of complex addition remains the same.[^aac-series-rc]

In polar form, the impedance has an angle of approximately `-36.87°`, so for a source voltage at `0°` phase, the current has an angle of `+36.87°`, since `I = V/Z`. This provides an independent check of the phase relationship: current leads voltage in a capacitive series circuit.[^aac-series-rc]

**Common mistake:** adding `8 V + 6 V` and concluding that the source voltage must be `14 V`. Only phasors with identical phase angles can be added that way; for components with different phases, one must first express the voltages in complex form, sum them, and only then find the magnitude of the result.[^aac-series-rc]

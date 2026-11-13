---
id: emb-elee-0063
title: "How do you find the impedance of a series RLC circuit at a given frequency?"
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
  - source_id: aac-series-rlc
    title: "All About Circuits: Series R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-r-l-and-c/
---

## Short answer

For a given frequency, calculate `X_L = 2π*f*L` and `X_C = 1/(2π*f*C)`, then form `Z = R + j*(X_L - X_C)`. The magnitude is `|Z| = sqrt(R² + (X_L - X_C)²)`, and the angle is `atan2(X_L - X_C, R)`. In a series circuit, the current phasor is `I = V/Z`.[^aac-series-rlc]

## Detailed explanation

The impedance of a series RLC circuit is found by adding the complex impedances of its elements at the given frequency. First convert frequency `f` to angular frequency `ω = 2π*f`, then compute the inductive reactance `X_L = ω*L` and capacitive reactance `X_C = 1/(ω*C)`. The resistor value remains the real part.[^aac-series-rlc]

Because inductance and capacitance have opposite signs in their imaginary parts, the total impedance is `Z = R + j*(X_L - X_C)`. From this, the magnitude is `|Z| = sqrt(R² + (X_L - X_C)²)`, and the phase is `φ = atan2(X_L - X_C, R)`. The `atan2` function preserves the correct quadrant; for a passive series circuit with `R > 0`, this angle lies between -90° and +90°.[^aac-series-rlc]

When `X_L = X_C`, the reactive parts cancel each other out, so the impedance equals simply `R` with a phase angle of zero. Below this frequency, the circuit exhibits capacitive behavior, and above it, inductive behavior. If one of the components is absent from the circuit, the corresponding term is omitted: for an RC circuit, `-j*X_C` remains, and for an RL circuit, `+j*X_L`.[^aac-series-rlc]

To find current, one divides the source voltage phasor by the complex impedance: `I = V/Z`. Dividing solely by `|Z|` yields the current magnitude, but not its phase relative to voltage. Similarly, component voltages combine as phasors, even though their scalar magnitudes may not arithmetically sum to the source magnitude.[^aac-series-rlc]

**Common mistake:** subtracting reactances without tracking signs or taking the square root of merely `R² + X_L² + X_C²`. First combine the imaginary parts with their appropriate signs, and only then determine the magnitude and angle of the resulting complex number.[^aac-series-rlc]

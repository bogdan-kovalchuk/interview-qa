---
id: emb-elee-0057
title: "What is complex impedance Z?"
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
  - source_id: aac-impedance-definition
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

Impedance `Z` is the complex ratio of voltage and current phasors, `Z = V/I`, generalizing resistance for AC. For a series combination of `R` and a reactive component, it is written as `Z = R + j*X`, where the magnitude is `|Z| = sqrt(R² + X²)` and the phase angle is `atan2(X, R)`. Impedance is measured in ohms, and its angle defines the phase relationship between voltage and current.[^aac-impedance-definition]

## Detailed explanation

Impedance generalizes the action of resistance and reactive elements in a sinusoidal circuit: for voltage and current phasors, `Z = V/I`. It is a complex quantity measured in ohms that simultaneously expresses the amplitude ratio and the phase shift. For a pure resistor, the impedance angle is zero; reactive elements contribute an imaginary component.[^aac-impedance-definition]

In rectangular form `Z = R + j*X`, where `R` is the real part and `X` is the signed reactive part. A positive `X` corresponds to inductive behavior, while a negative `X` corresponds to capacitive behavior. The magnitude `|Z| = sqrt(R² + X²)` describes the ratio of voltage and current magnitudes, and the argument `φ = atan2(X, R)` represents their phase difference under the passive sign convention. For a complex circuit, these values depend on frequency, so a single number is generally insufficient for the entire frequency range.[^aac-impedance-definition]

Example: for a series circuit with `R = 3 Ω` and `X_L = 4 Ω`, the impedance is `Z = 3 + j*4 Ω`. Its magnitude is `5 Ω` and its angle is approximately `53.1°`; thus, at the given frequency, the current lags the voltage by `53.1°` under the accepted passive sign convention. The value `5 Ω` alone does not retain phase information and cannot replace complex impedance in circuit analysis.[^aac-impedance-definition]

The impedances of series elements are combined via complex addition; for parallel branches, complex admittances or the reciprocal sum are used. Therefore, one cannot simply add the branch magnitudes as if they were resistors: phase is an integral part of the result. Applicability of the phasor model assumes linear steady-state operation at a shared frequency.[^aac-impedance-definition]

**Common mistakes:**

- Referring to impedance solely by its magnitude and discarding the angle.
- Using the sign of `X` without distinguishing between inductive and capacitive reactance.
- Applying simple scalar addition of resistances to complex quantities.[^aac-impedance-definition]

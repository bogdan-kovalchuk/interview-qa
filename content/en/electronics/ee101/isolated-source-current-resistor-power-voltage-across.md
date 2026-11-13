---
id: emb-elee-0088
title: "Isolated 6 V RMS source, R = 1 kΩ, `X_C` = 1 kΩ. What are the current, the resistor power and the voltage across C?"
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

For a series RC circuit with `R = X_C = 1 kΩ`, the current equals `4.24 mA RMS` and the power dissipated by R is `18 mW`.[^aac-alternating-current] The voltage across the capacitor equals `4.24 V RMS` (approximately `6 V peak` for a sine wave).[^aac-alternating-current]

## Detailed explanation

In an isolated series RC circuit, the resistor and capacitor divide the source voltage as phasors: the voltage across R is in phase with the current, while the voltage across C lags the current by 90 degrees.[^aac-alternating-current]

Therefore, `V_R` and `V_C` cannot simply be added as scalar quantities. For ideal components, the total impedance has a magnitude of `sqrt(R^2 + X_C^2)`, and the RMS current is the RMS source voltage divided by this magnitude. Given `R = 1 kΩ` and `X_C = 1 kΩ`, the impedance magnitude is approximately `1.414 kΩ`, which yields `I = 6/1414 = 4.24 mA RMS`.[^aac-alternating-current]

The power dissipated as heat in R is `I_RMS^2*R`, which is approximately `18 mW`. The magnitude of the voltage across the capacitor is `I_RMS*X_C = 4.24 V RMS`. If the source is sinusoidal, the peak value of this voltage is the RMS value multiplied by `sqrt(2)`, or approximately `6.0 V peak`.[^aac-alternating-current]

This calculation assumes an ideal source, and ideal R and C components with the specified reactance at the source frequency. Real component tolerances, capacitor ESR, and source output resistance will alter the result. An isolated source means its output has no fixed reference to earth ground; this does not alter the phasor calculation, but it is important for safe measurement.[^aac-alternating-current]

**Common mistake:** Adding the voltage drops of `4.24 V` across R and `4.24 V` across C arithmetically and concluding that the source produces `8.48 V`. Because the components are orthogonal in phase, their resulting vector sum magnitude is `sqrt(4.24^2 + 4.24^2)`, which is approximately 6 V RMS.[^aac-alternating-current]

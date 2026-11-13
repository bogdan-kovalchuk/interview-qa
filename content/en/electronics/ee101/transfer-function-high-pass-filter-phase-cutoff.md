---
id: emb-elee-0109
title: "What is the transfer function of an RC high-pass filter and its phase at the cutoff frequency?"
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
  - source_id: aac-high-pass-transfer-function
    title: "All About Circuits: Understanding the First-Order High-Pass Filter Transfer Function"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-the-first-order-high-pass-filter-transfer-function/
---

## Short answer

For an ideal RC high-pass filter, `H(jω) = jωRC/(1 + jωRC)`, and at the cutoff frequency `f_c = 1/(2*pi*R*C)` the output leads the input by 45°.[^aac-high-pass-transfer-function] This holds when any external load is already accounted for in the effective R.

## Detailed explanation

The transfer function is the ratio of the complex phasors of output and input voltages for a steady-state sinusoidal signal. For an ideal RC high-pass filter with the output taken across R, it equals `H(jω) = jωRC/(1 + jωRC)`, where `ω = 2*pi*f`.[^aac-high-pass-transfer-function]

The magnitude shows what fraction of the input amplitude appears at the output: `|H| = (f/f_c)/sqrt(1 + (f/f_c)^2)`. At frequencies well below cutoff it is small, while at frequencies well above cutoff it approaches unity. The cutoff frequency equals `f_c = 1/(2*pi*R*C)` for an unloaded circuit or for an R that already accounts for effective loading.[^aac-high-pass-transfer-function]

The phase of the output relative to the input is `φ = 90° - arctan(f/f_c)`: at low frequencies it approaches +90°, and at high frequencies it approaches 0°. At the cutoff frequency `f = f_c`, the arctangent equals 45°, so the output leads the input by 45°. At that same point, the amplitude is `1/sqrt(2)`, or approximately 0.707 of the maximum, which corresponds to -3 dB.[^aac-high-pass-transfer-function]

**Example:** if `R = 1 kΩ` and `C = 100 nF`, then `f_c` is approximately `1.59 kHz`. At this frequency, a sinusoidal output has approximately 70.7% of the high-frequency passband amplitude and leads the input by 45° under the standard phasor convention.

**Common mistakes:**
- Attributing a 45° phase lag to the high-pass filter: the sign is opposite to that of a low-pass filter under the same convention.
- Confusing `ω` in radians per second with `f` in hertz; they differ by a factor of `2*pi`.
- Applying the ideal formula without accounting for output loading.

This is the frequency transfer function of a linear circuit in steady state. It does not describe startup transients, component nonlinearities, or breadboard parasitics; the measured result may deviate if these effects are significant.

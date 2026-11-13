---
id: emb-elee-0119
title: "RL high-pass filter: R = 1 kΩ, L = 2.2 mH. What are the cutoff frequency and gain at 0.1 f_c, f_c, and 10 f_c?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal RL high-pass filter with output across the inductor, `f_c = R/(2π*L) ≈ 72.3 kHz` with R = 1 kΩ and L = 2.2 mH. At `0.1 f_c`, `f_c`, and `10 f_c`, the magnitude of the transfer function is approximately 0.0995, 0.707, and 0.995, respectively; the phase is approximately +84.3°, +45°, and +5.7°.[^aac-high-pass-filters]

## Detailed explanation

For an ideal RL high-pass filter with a series R and an inductor from the output to common ground, the cutoff frequency is `f_c = R/(2π*L)`. At this frequency, the voltage magnitude across the inductor is approximately 70.7 % of the high-frequency level. The transfer function `H(jω) = jωL/(R + jωL)` shows why the circuit passes high frequencies: the inductor's reactance increases with frequency, so an increasingly smaller fraction of the signal drops across the series R.[^aac-high-pass-filters]

Calculation example for the given components:

```text
R = 1000 Ω
L = 2.2 mH = 0.0022 H
f_c = R/(2π*L) ≈ 72.3 kHz
```

Let the ratio of frequency to cutoff be denoted by `x = f/f_c`. Then the transfer magnitude is `|H| = x/sqrt(1 + x²)`, and the phase is `atan(1/x)`. For `x = 0.1`, we obtain approximately 0.0995 and +84.3°: the inductor almost shorts the output to common ground. For `x = 1`, we obtain 0.707 and +45°. For `x = 10`, we obtain approximately 0.995 and +5.7°, meaning the signal passes almost without attenuation or phase shift. The gain here is defined as the ratio of output voltage to input voltage; it is not power.[^aac-high-pass-filters]

These numbers assume ideal R and L, low source resistance, and the absence of loading that alters the equivalent resistance. In a practical circuit, a subsequent stage may shunt the inductor; winding resistance also alters the low-frequency level. Verify the circuit and measurement point before substituting nominal values. A common mistake is using this same formula for a low-pass filter: for an LPF, the output is taken across the resistor, not across the inductor.[^aac-high-pass-filters]

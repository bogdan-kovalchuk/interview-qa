---
id: emb-elee-0095
title: "Why does a square wave have rounded edges after an RC low-pass filter?"
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
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

A square wave consists of a fundamental frequency and higher harmonics, and the RC low-pass filter attenuates its high-frequency components. As a result, sharp transitions become rounded. In the time domain, the capacitor charges and discharges exponentially through the resistor with a time constant of `τ = R*C`.[^aac-low-pass-filters]

## Detailed explanation

Rounded edges occur because an RC low-pass filter cannot instantly track a step change in input voltage. In the frequency domain, a periodic square wave consists of a fundamental frequency and higher harmonics; the edge transition speed depends on these high-frequency components. A low-pass filter attenuates high frequencies more heavily, leaving a smoother waveform at the output.[^aac-low-pass-filters]

In the time domain, the same process is described by the charging and discharging of the capacitor through the resistor. For an ideal voltage source, a series resistor `R`, and an output capacitor `C`, the circuit time constant is `τ = R*C`. Following an input step, the capacitor voltage approaches the new steady-state value exponentially rather than jumping instantaneously; after one time constant `τ`, it covers approximately 63% of the difference between its initial and final levels. As a result, the transition edge has a finite rise time.[^aac-low-pass-filters]

The degree of edge rounding depends on the ratio of the time constant to the half-period duration. If the period is much longer than `τ`, the output reaches both steady-state voltage levels. If the period is shorter than or comparable to `τ`, the capacitor does not have enough time to charge and discharge fully, which also reduces the output amplitude. The cutoff frequency of an ideal unloaded RC low-pass filter is `f_c = 1/(2π*R*C)`; above this frequency, sinusoidal components are progressively attenuated rather than disappearing abruptly.[^aac-low-pass-filters]

**Common mistakes:**

- Assuming that the filter simply 'clips' or rounds the corners without altering the rest of the signal; each harmonic is attenuated according to the filter's frequency response.
- Treating `f_c` as a brick-wall boundary. It is a transition frequency where the output amplitude of a standard RC low-pass filter drops to approximately 70.7% of its low-frequency passband level.[^aac-low-pass-filters]
- Forgetting about output loading: a real load resistance connected to the output alters both the passband gain and the cutoff frequency.

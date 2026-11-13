---
id: emb-elee-0055
title: "What is a phasor?"
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
  - source_id: aac-phasor-definition
    title: "All About Circuits: Sinusoidal Steady-State Analysis"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-analysis/
---

## Short answer

A phasor is a complex number that encodes the amplitude and phase of a sinusoidal signal relative to a chosen reference at a given frequency. For `v(t) = V_m*sin(ω*t + φ)`, it can be written as `V = V_m∠φ` under the sine convention, with the exponential form tied to Euler's formula. Phasors simplify the analysis of linear circuits in sinusoidal steady state, but they do not by themselves describe an arbitrary transient or a signal with mixed frequencies.[^aac-phasor-definition]

## Detailed explanation

A phasor represents a single-frequency sinusoid by its constant amplitude and phase, eliminating explicit time dependence from calculations. For example, if a voltage has the form `v(t) = V_m*sin(ω*t + φ)`, the phasor quantity contains `V_m` and `φ`, while the common time factor with angular frequency `ω` is omitted from each equation. This is useful in steady state when sources and responses share the same frequency.[^aac-phasor-definition]

Phase angle is not an absolute property of a signal: it is measured relative to a chosen reference sinusoid. Therefore, a source is often conventionally assigned a phase of `0°`, and other voltages and currents are described as leading or lagging relative to it. Complex notation with `j` is convenient because the real and imaginary parts represent two orthogonal components; electrical engineering uses `j` to avoid confusing the imaginary unit with current `i`.[^aac-phasor-definition]

When converting between time-domain and phasor forms, one must ensure consistency in the sine or cosine convention, peak or RMS amplitude, and angle units. A phasor specified in RMS cannot be substituted into a formula where amplitude denotes peak without conversion. The analysis also assumes circuit linearity and steady state; for a non-sinusoidal periodic signal, different harmonics are analyzed as separate frequency components.[^aac-phasor-definition]

Example: if `v(t) = 10*sin(ω*t + 30°) V`, then under the peak sine convention the phasor has a magnitude of `10 V` and an angle of `30°`. If that same voltage is chosen as the reference in the circuit, its angle becomes `0°`, and all other angles shift by that same difference, preserving relative phases.[^aac-phasor-definition]

**Common mistakes:**

- Treating phase as absolute without specifying a reference signal.
- Mixing peak and RMS amplitudes or sine and cosine conventions.
- Using a single phasor for signals of different frequencies or for transient processes.[^aac-phasor-definition]

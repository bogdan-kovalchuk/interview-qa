---
id: emb-elee-0083
title: "What are the transfer functions and cutoff frequency of an RL circuit with the output across R and across L?"
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
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

For an unloaded ideal circuit, `H_R = R/(R + j*ω*L)`, `H_L = j*ω*L/(R + j*ω*L)`, and the cutoff frequency is `f_c = R/(2π*L)`. At cutoff, both magnitudes equal `1/√2`, while the phases are −45° for R and +45° for L. For R = 200 Ω and L = 2.2 mH, the cutoff frequency is approximately 14.47 kHz.[^aac-series-rl]

## Detailed explanation

The transfer function `H(f)` is the complex ratio of the output voltage phasor to the input voltage phasor at a specified frequency. For a series circuit with ideal R and L, the total impedance is `Z = R + j*ω*L`. If the output is taken across the resistor, its phasor voltage equals `I*R`; dividing by the input voltage `I*Z` yields `H_R = R/(R + j*ω*L)`. For the output taken across the inductor, the corresponding drop is `I*j*ω*L`, so `H_L = j*ω*L/(R + j*ω*L)`. These relationships assume that the output is unloaded.[^aac-series-rl]

The first-order cutoff frequency is defined at the point where the output magnitude equals `1/√2` of the passband level, or approximately −3 dB. For this RL divider, the condition is equivalent to `X_L = R`, yielding `f_c = R/(2π*L)`. At this frequency, the magnitudes of both outputs are identical: `|H_R| = |H_L| = 1/√2`. However, their phases differ: the voltage across R has a phase of −45° relative to the input, while that across L has +45°. These are phasor relationships, not two in-phase voltages with the same orientation.[^aac-series-rl]

Calculation example: for R = 200 Ω and L = 2.2 mH, we obtain `f_c = 200/(2π*0.0022) ≈ 14468 Hz`, or approximately 14.47 kHz. At this frequency, `X_L` equals 200 Ω. If voltages are measured with an oscilloscope, the RMS or peak magnitudes of each output will be about 0.707 of the input, but their phase angles yield a vector sum that equals the input.[^aac-series-rl]

This model and the cutoff frequency will change if the inductor has significant series resistance or if the output is loaded. In a calculation with a real component, winding resistance is added to the inductor's impedance; for a loaded output, the input impedance of the subsequent stage is taken into account. Furthermore, the simple lumped-element ideal model does not describe behavior above the self-resonant frequency of the inductor.[^aac-series-rl]

**Common mistake:** substituting millihenries as 2.2 instead of 0.0022 H or referring to `f_c` as a universal property of the inductor itself. One must convert R and L to units of Ω and H, clarify the output circuit configuration, and check for loading. For each output, the magnitude and phase must be consistent with its respective formula: R corresponds to a low-pass filter, and L corresponds to a high-pass filter in this ideal topology.[^aac-series-rl]

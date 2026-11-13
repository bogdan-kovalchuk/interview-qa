---
id: emb-elee-0110
title: "RC high-pass filter: R = 10 kΩ, C = 100 nF, input 1 V RMS. What is the cutoff frequency and the outputs at 15.9 Hz, 159 Hz and 1.59 kHz?"
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
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

The cutoff frequency `f_c` is approximately 159.15 Hz. For an ideal unloaded RC high-pass filter, the outputs are approximately 0.0995 V, 0.707 V, and 0.995 V RMS, respectively.[^aac-high-pass-filters]

## Detailed explanation

An RC high-pass filter passes signals better as frequency increases because the series capacitor exhibits a lower impedance magnitude at higher frequencies. For an ideal source with zero output impedance, a series C, and R connected to common ground, the output is taken across R. The transfer function magnitude is `|H| = 1/sqrt(1 + (f_c/f)^2)`, and the cutoff frequency is `f_c = 1/(2π*R*C)`.[^aac-high-pass-filters]

In this problem, `R*C = 10 kΩ*100 nF = 1 ms`, so `f_c ≈ 159.15 Hz`. At the cutoff frequency, the transfer magnitude is `1/sqrt(2) ≈ 0.707`, or about -3 dB. Below cutoff, the voltage decreases rapidly, while well above cutoff it approaches the input voltage. This is the frequency response for a steady-state sine wave; it does not describe the transient waveform by itself.[^aac-high-pass-filters]

Calculation example for a 1 V RMS input: at 15.9 Hz, the ratio `f/f_c` is close to 0.1, so the output is approximately 0.0995 V RMS; at 159 Hz, it is close to 1, and the output is approximately 0.707 V RMS; at 1.59 kHz, it is close to 10, and the output is approximately 0.995 V RMS. These values are rounded, and nominal component values are assumed to be exact.[^aac-high-pass-filters]

A real circuit may deviate from these numbers due to source resistance, output loading, R and C tolerances, and parasitic parameters. A load connected in parallel with R reduces the effective resistance and changes the cutoff frequency, so the formula cannot be applied without checking the topology and measurement instrument.[^aac-high-pass-filters]

---
id: emb-elee-0103
title: "What is the cutoff frequency of an RC low-pass filter with 1 kΩ and 100 nF, and which outputs should you expect at 1 V RMS at 160 Hz, 1.59 kHz and 15.9 kHz?"
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
  - source_id: aac-low-pass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

For an ideal RC low-pass filter, `f_c = 1/(2π*R*C) ≈ 1.59 kHz`. With a 1 V RMS input, the outputs at 160 Hz, 1.59 kHz, and 15.9 kHz are approximately 0.995 V, 0.707 V, and 0.0995 V. At the cutoff frequency, the phase lags by 45°.[^aac-low-pass]

## Detailed explanation

A simple RC low-pass filter consists of a resistor in series with the input and a capacitor from the output node to ground. As frequency increases, the capacitor impedance decreases, so more of the signal is shunted to ground and the output weakens. For an ideal unloaded output, the cutoff frequency equals `f_c = 1/(2π*R*C)`; at this frequency, the amplitude is `1/sqrt(2) ≈ 0.707` of its low-frequency value.[^aac-low-pass]

For `R = 1 kΩ` and `C = 100 nF`, the product `R*C` equals `0.0001 s`, so `f_c ≈ 1591.5 Hz`. The amplitude ratio of an ideal filter at frequency `f` equals `1/sqrt(1+(f/f_c)^2)`. At 160 Hz, the frequency is roughly one-tenth of the cutoff; at 1.59 kHz, it is nearly equal to the cutoff; at 15.9 kHz, it is roughly ten times higher.[^aac-low-pass]

Example for a 1 V RMS sinusoidal input:

```text
160 Hz:   1/sqrt(1+(160/1591.5)^2) ≈ 0.995, Vout ≈ 0.995 V RMS
1591.5 Hz: 1/sqrt(2) ≈ 0.707, Vout ≈ 0.707 V RMS
15915 Hz: 1/sqrt(1+(15915/1591.5)^2) ≈ 0.0995, Vout ≈ 0.0995 V RMS
```

This calculation is for nominal components, an ideal source, and an unloaded output; the real input resistance of the next stage can alter both the gain and the cutoff frequency. At the cutoff frequency, the output also has a 45° phase lag in this circuit. A common mistake is believing that the 'cutoff frequency' completely terminates the signal, even though the rolloff is smooth, or that 0.707 represents half the amplitude; it is roughly half the power across equal resistances.[^aac-low-pass]

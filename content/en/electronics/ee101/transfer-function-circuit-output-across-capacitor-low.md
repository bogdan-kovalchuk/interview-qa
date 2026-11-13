---
id: emb-elee-0073
title: "What is the transfer function of an RC circuit with the output across the capacitor, and why is it a low-pass filter?"
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
  - source_id: aac-rc-lowpass
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

For an ideal unloaded RC circuit with the output across the capacitor, the transfer function is `H_C = V_C/V_in = 1/(1 + j*2π*f*R*C)`. As frequency increases, the capacitor's impedance decreases, so a larger portion of the signal drops across the resistor and the output weakens. The cutoff frequency `f_c = 1/(2π*R*C)` corresponds to a transfer magnitude of `1/sqrt(2)`.[^aac-rc-lowpass]

## Detailed explanation

In a series RC circuit, the output is taken across the capacitor connected between the output node and ground. Using `Z_C = 1/(j*2π*f*C)` and the complex impedance divider, we have `H_C = V_C/V_in = Z_C/(R + Z_C) = 1/(1 + j*2π*f*R*C)`. This relationship assumes ideal components, zero source impedance, and no load altering the output node.[^aac-rc-lowpass]

At low frequencies, `|Z_C|` is much larger than `R`, so most of the input voltage appears across the capacitor. At high frequencies, `|Z_C|` becomes small, the output node is shunted more strongly to ground, and the voltage across the capacitor decreases. This is why the circuit passes low-frequency components better than high-frequency components. The cutoff frequency `f_c = 1/(2π*R*C)` is the point where the transfer magnitude equals approximately 0.707 and the output phase is −45° relative to the input.[^aac-rc-lowpass]

**Example:** for `R = 1 kΩ` and `C = 100 nF`, we obtain `f_c ≈ 1.592 kHz`. At this frequency, the magnitude of the capacitor's reactance is approximately `1 kΩ`, so the magnitudes of the resistive and capacitive voltage drops are identical, though their phases differ. Above this frequency, the output amplitude rolls off; for an ideal first-order network, the roll-off in the far stopband approaches 20 dB per decade.[^aac-rc-lowpass]

A real load matters: the input impedance of the subsequent stage in parallel with the capacitor alters the transfer function and can shift the cutoff frequency. Likewise, source impedance adds to the series resistance. Before applying the formula, verify whether the circuit matches the unloaded RC circuit assumption.[^aac-rc-lowpass]

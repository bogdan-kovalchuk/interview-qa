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

TODO

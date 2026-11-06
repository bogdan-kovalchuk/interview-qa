---
id: emb-elee-0094
title: "How do you design a 1 kHz RC low-pass filter with R = 1 kΩ, and what should you do after choosing a standard value?"
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

For `R = 1 kΩ` and `f_c = 1 kHz`, the required capacitance is `C = 1/(2*pi*R*f_c) ≈ 159 nF`. Selecting the standard value `150 nF` shifts the actual cutoff to `1/(2*pi*1 kΩ*150 nF) ≈ 1.06 kHz`. After choosing standard components, recalculate the cutoff frequency while accounting for component tolerances and load impedance.[^aac-rc-low-pass-transfer]

## Detailed explanation

TODO

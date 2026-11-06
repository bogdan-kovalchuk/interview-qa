---
id: emb-elee-0091
title: "What are the magnitude and phase of the RC low-pass transfer function?"
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

For a passive RC low-pass filter without significant loading, `H(f) = 1/(1 + j*f/f_c)`, where `f_c = 1/(2*pi*R*C)`. Then `|H| = 1/sqrt(1 + (f/f_c)^2)`, and the output phase relative to the input is `-atan(f/f_c)`. At the cutoff frequency, the magnitude is `1/sqrt(2)` of its low-frequency value, and the phase is `-45°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

TODO

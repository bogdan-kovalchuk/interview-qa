---
id: emb-elee-0115
title: "What is the transfer function and cutoff frequency of an RL low-pass filter?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For a series RL low-pass filter with output across R, the transfer function is `H(jω) = R/(R + jωL)`, the cutoff frequency is `f_c = R/(2π*L)`, and the time constant is `τ = L/R`. For R = 1 kΩ and L = 330 µH, we obtain `f_c ≈ 482 kHz`. With R kept constant, doubling L cuts the cutoff frequency in half.[^aac-low-pass-filters]

## Detailed explanation

TODO

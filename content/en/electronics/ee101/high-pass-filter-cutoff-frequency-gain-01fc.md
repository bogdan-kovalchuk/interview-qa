---
id: emb-elee-0119
title: "RL high-pass filter: R = 1 kΩ, L = 2.2 mH. What are the cutoff frequency and gain at 0.1 f_c, f_c, and 10 f_c?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal RL high-pass filter with output across the inductor, `f_c = R/(2π*L) ≈ 72.3 kHz` with R = 1 kΩ and L = 2.2 mH. At `0.1 f_c`, `f_c`, and `10 f_c`, the magnitude of the transfer function is approximately 0.0995, 0.707, and 0.995, respectively; the phase is approximately +84.3°, +45°, and +5.7°.[^aac-high-pass-filters]

## Detailed explanation

TODO

---
id: emb-elee-0092
title: "What are the magnitude and phase of an RC low-pass filter at 0.1*f_c, f_c, and 10*f_c?"
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

For an unloaded first-order RC low-pass filter, `|H| = 1/sqrt(1 + (f/f_c)^2)` and the phase is `-atan(f/f_c)`. At `0.1*f_c`, `|H| ≈ 0.995` with a phase of `-5.7°`. At `f_c`, `|H| ≈ 0.707` with a phase of `-45°`. At `10*f_c`, `|H| ≈ 0.0995` with a phase of `-84.3°`.[^aac-rc-low-pass-transfer]

## Detailed explanation

TODO

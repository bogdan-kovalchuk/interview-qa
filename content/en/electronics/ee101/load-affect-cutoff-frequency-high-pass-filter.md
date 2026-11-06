---
id: emb-elee-0112
title: "How does a load R_L affect the cutoff frequency of an RC high-pass filter?"
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

A load `R_L` connected in parallel with the output resistor R decreases the effective resistance to `R_eff = R || R_L`, so the cutoff frequency `f_c = 1/(2π*R_eff*C)` increases. For `R = R_L = 10 kΩ` and `C = 100 nF`, it shifts from approximately 159 Hz to 318 Hz.[^aac-high-pass-filters]

## Detailed explanation

TODO

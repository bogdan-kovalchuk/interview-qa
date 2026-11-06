---
id: emb-elee-0116
title: "Why is RC chosen more often than RL for simple low-frequency filters?"
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

For an ideal RL low-pass filter with a 1 kHz cutoff and R = 1 kΩ, an inductance of L ≈ 159 mH is required. In many low-power signal circuits, an RC filter is simpler and more compact because an inductor of that value can have large physical dimensions, high cost, and significant winding resistance. This is a practical preference rather than a strict ban on RL filters: inductors are advantageous when low series resistance and high current capability are essential.[^aac-low-pass-filters]

## Detailed explanation

TODO

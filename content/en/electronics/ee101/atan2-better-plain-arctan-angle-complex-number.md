---
id: emb-elee-0070
title: "Why is atan2 better than a plain arctan(b/a) for the angle of a complex number?"
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
  - source_id: aac-atan2-quadrants
    title: "All About Circuits: Quadrature Frequency and Phase Demodulation"
    url: https://www.allaboutcircuits.com/textbook/radio-frequency-analysis-design/radio-frequency-demodulation/quadrature-frequency-and-phase-demodulation/
---

## Short answer

A plain `arctan(b/a)` cannot determine the quadrant of a complex number because the ratio loses the signs of the individual components; for `-3 + j4`, it gives −53.13°, whereas the true angle is 126.87°. The `atan2(b, a)` function accepts both coordinates and returns the angle in the correct quadrant. Always verify whether the returned angle is in radians or degrees.[^aac-atan2-quadrants]

## Detailed explanation

TODO

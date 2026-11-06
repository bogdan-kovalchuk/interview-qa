---
id: emb-elee-0063
title: "How do you find the impedance of a series RLC circuit at a given frequency?"
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
  - source_id: aac-series-rlc
    title: "All About Circuits: Series R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-r-l-and-c/
---

## Short answer

For a given frequency, calculate `X_L = 2π*f*L` and `X_C = 1/(2π*f*C)`, then form `Z = R + j*(X_L - X_C)`. The magnitude is `|Z| = sqrt(R² + (X_L - X_C)²)`, and the angle is `atan2(X_L - X_C, R)`. In a series circuit, the current phasor is `I = V/Z`.[^aac-series-rlc]

## Detailed explanation

TODO

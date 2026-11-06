---
id: emb-elee-0078
title: "How do you calculate the impedance and current of a series RL circuit?"
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
---

## Short answer

For a series RL circuit at frequency `f`, inductive reactance is `X_L = 2π*f*L`, and total impedance is `Z = R + jX_L`. The current phasor is calculated as `I = V/Z`. Its magnitude is `V/√(R² + X_L²)`, and the current lags the source voltage by `atan2(X_L, R)`.[^aac-alternating-current]

## Detailed explanation

TODO

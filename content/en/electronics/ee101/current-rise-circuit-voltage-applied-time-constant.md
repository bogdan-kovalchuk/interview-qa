---
id: emb-elee-0041
title: "How does current rise in an RL circuit after voltage is applied, and what is its time constant?"
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

For an ideal series RL circuit with constant voltage source `V_0` and zero initial current, `I(t) = (V_0/R)*(1 - e^(-t/τ))`, where `τ = L/R`. After `5τ`, the current reaches approximately 99.3% of `V_0/R`; this estimate assumes constant `R` and `L` values.[^aac-alternating-current]

## Detailed explanation

TODO

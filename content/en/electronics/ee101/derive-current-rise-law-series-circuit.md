---
id: emb-elee-0044
title: "How do you derive the current rise law in a series RL circuit?"
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

For an ideal series RL circuit, Kirchhoff's voltage law yields `V_0 = I*R + L*dI/dt`. Under constant applied voltage `V_0` and initial condition `I(0) = 0`, the differential equation solution is `I(t) = (V_0/R)*(1 - e^(-t/τ))`, where `τ = L/R`.[^aac-alternating-current]

## Detailed explanation

TODO

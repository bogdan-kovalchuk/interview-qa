---
id: emb-elee-0079
title: "RL circuit: R = 200 Ω, L = 2.2 mH, f = 100 Hz, input 7 V RMS. Why is the voltage across the coil only about 48 mV?"
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

For an ideal inductor, `X_L = 2π*f*L ≈ 1.38 Ω`, which is far smaller than `R = 200 Ω`, so nearly all of the source voltage drops across the resistor. Calculations yield approximately `35.0 mA RMS` and `48.4 mV RMS` across the inductor, with the inductor voltage leading the current by 90°.[^aac-alternating-current]

## Detailed explanation

TODO

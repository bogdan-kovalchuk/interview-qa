---
id: emb-elee-0064
title: "Series RC circuit: R = 100 Ω, X_C = 75 Ω, 10 V RMS source. Why do the voltages across R and C (8 V and 6 V) not add up to 14 V?"
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
  - source_id: aac-series-rc
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
---

## Short answer

For `R = 100 Ω` and `X_C = 75 Ω`, the circuit impedance is `Z = 100 - j75 Ω`, with a magnitude of `125 Ω` and an angle of approximately `-36.87°`. With a `10 V RMS` source, the current magnitude is `0.08 A`. The voltages `8 V` across R and `6 V` across C are shifted by 90° relative to each other, so their phasor sum has a magnitude of `10 V` rather than `14 V`.[^aac-series-rc]

## Detailed explanation

TODO

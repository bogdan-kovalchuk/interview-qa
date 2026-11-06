---
id: emb-elee-0074
title: "RC circuit: R = 1 kΩ, C = 100 nF, f ≈ 1591.5 Hz, input 1 V RMS. What are the current and the voltages across R and C?"
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
  - source_id: aac-series-rc-analysis
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
---

## Short answer

At `f ≈ 1591.5 Hz`, with `R = 1 kΩ` and `C = 100 nF`, reactance is `X_C ≈ 1 kΩ`, yielding `Z ≈ 1000 - j1000 Ω`. For an input of `1 V RMS∠0°`, the current is approximately `0.707 mA∠45°`, giving `V_R ≈ 0.707 V∠45°` and `V_C ≈ 0.707 V∠−45°`, whose complex sum equals the input phasor. Rounding intermediate numbers yields only approximate values.[^aac-series-rc-analysis]

## Detailed explanation

TODO

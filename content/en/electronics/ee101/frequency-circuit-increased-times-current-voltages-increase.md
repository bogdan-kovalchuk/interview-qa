---
id: emb-elee-0080
title: "If the frequency in an RL circuit is increased 10 times, do the current and voltages also increase 10 times?"
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
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

No. For constant inductance, `X_L = 2π*f*L`, so a tenfold increase in frequency yields a tenfold increase in inductive reactance, but current and voltages depend on the total complex impedance of the circuit. The voltages across the resistor and inductor are phasors, so their magnitudes cannot simply be added as scalar numbers.[^aac-series-rl]

## Detailed explanation

TODO

---
id: emb-elee-0035
title: "Why is the charging current of an RC circuit highest at the start and why does it fall to zero?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor transient response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
---

## Short answer

For an ideal constant voltage source `V_0`, series resistor `R`, and initially discharged capacitor `C`, the initial current is `V_0/R`. As the capacitor charges, the resistor voltage and charging current decay exponentially with time constant `τ = R*C`; in steady state, the current approaches zero.[^aac-capacitor-transient]

## Detailed explanation

TODO

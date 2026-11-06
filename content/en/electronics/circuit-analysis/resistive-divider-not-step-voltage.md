---
id: emb-elcirc-0031
title: "Why can a resistive divider not step voltage up?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
---

## Short answer

For two resistors connected across a source, the transfer ratio is `V_out = V_in*R_2/(R_1+R_2)`. Because passive resistances satisfy `R_1 >= 0` and `R_2 >= 0`, the scaling factor `R_2/(R_1+R_2)` can never exceed 1, making voltage step-up impossible. Stepping voltage above the input rail requires an active power conversion topology or energy storage element, such as a boost converter or transformer circuit.[^aac-direct-current]

## Detailed explanation

TODO

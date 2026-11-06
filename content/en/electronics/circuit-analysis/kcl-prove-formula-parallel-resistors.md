---
id: emb-elcirc-0013
title: "How does KCL derive the equivalent resistance of resistors in parallel?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-parallel-resistors
    title: "All About Circuits: Resistance in Parallel Networks"
    url: https://www.allaboutcircuits.com/technical-articles/resistance-in-parallel-networks
---

## Short answer

For resistors connected across the same two nodes, the branch voltage `V` is identical across each element. Applying KCL and Ohm's law yields total current `I_s = V/R_1 + V/R_2`, which gives `1/R_eq = 1/R_1 + 1/R_2`, reducing for two resistors to `R_eq = R_1*R_2/(R_1+R_2)`.[^aac-parallel-resistors]

## Detailed explanation

TODO

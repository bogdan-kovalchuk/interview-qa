---
id: emb-elcirc-0019
title: "How do you quickly find the currents in parallel resistors once the common voltage is known?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
---

## Short answer

In a parallel bank, the voltage across every branch is identical because all components terminate at the same two nodes.[^aac-direct-current] Calculate each individual branch current using Ohm's law, `I_i = V/R_i`, and verify that their sum matches total current using KCL: `I_total = I_1 + I_2 + ...`.[^aac-direct-current]

## Detailed explanation

TODO

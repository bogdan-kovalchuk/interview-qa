---
id: emb-elcirc-0028
title: "What is the voltage divider \"stiffness\" rule – what is the minimum acceptable load?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

As a rule of thumb, maintaining `R_load >= 10*R_2` limits loaded output voltage sag to approximately 9.1% or less compared to the unloaded divider. Because `R_load` is connected in parallel with the lower resistor `R_2`, the exact output voltage must be calculated using the parallel combination `R_2 || R_load`.[^ti-slaa067]

## Detailed explanation

TODO

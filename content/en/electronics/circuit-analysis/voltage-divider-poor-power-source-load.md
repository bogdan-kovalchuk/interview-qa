---
id: emb-elcirc-0034
title: "Why is a voltage divider a poor power source for a load?"
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

A divider has a finite output resistance: the load shunts `R_2`, altering the lower resistance and dropping `V_out`. Smaller resistor values reduce this sag but increase quiescent current and power losses. Therefore, a divider is typically suitable for a signal or high-impedance input rather than for powering a variable load.[^aac-direct-current]

## Detailed explanation

TODO

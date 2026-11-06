---
id: emb-elintro-0229
title: "Why did 100 Ω in the collector fail to start the motor while 10 Ω let it start?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: pololu-motor-stall
    title: "Pololu Jrk G2 Motor Controller User’s Guide: Choosing the motor, power supply, and Jrk"
    url: https://www.pololu.com/docs/0J73/4.1
---

## Short answer

With an idealized 5 V drop, a 100 Ω resistor yields an upper-bound current of 50 mA, while 10 Ω gives 0.5 A by Ohm's law. Actual current is lower and depends on winding resistance, the transistor, and the power source; a smaller resistor can increase starting torque, but whether it is sufficient depends on the specific motor.[^aac-direct-current]

## Detailed explanation

TODO

---
id: emb-elintro-0228
title: "Why is it better to place a motor in the collector branch of an NPN than in the emitter branch?"
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
---

## Short answer

For a low-side NPN switch, the motor is placed between the supply and the collector while the emitter is connected to ground; placing it in the emitter creates an emitter follower, leaving less voltage for the motor due to `V_BE`. A protective diode is required in parallel with the motor to provide a path for inductive current during turn-off.[^aac-semiconductors]

## Detailed explanation

TODO

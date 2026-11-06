---
id: emb-elintro-0239
title: "What is `V_th` in a MOSFET?"
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

`V_GS(th)` is the gate-source voltage measured at a specified small drain current and test conditions in the datasheet; it is not the full turn-on voltage. Achieving low `R_DS(on)` typically requires a significantly higher `V_GS`, which should be taken from the specified test conditions of the given MOSFET.[^aac-semiconductors]

## Detailed explanation

TODO

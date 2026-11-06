---
id: emb-elee-0086
title: "Which frequencies are convenient for checking an RL filter in a simulator and on a breadboard?"
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
---

## Short answer

Test the RL filter at frequencies of `0.1*f_c`, `f_c`, and `10*f_c`, measuring `V_in`, `V_out`, the amplitude ratio, and the phase at each point.[^aac-alternating-current] A real inductor has winding resistance, so practical results will deviate from the ideal model.[^aac-alternating-current]

## Detailed explanation

TODO

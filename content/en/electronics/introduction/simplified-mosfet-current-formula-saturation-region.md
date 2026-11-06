---
id: emb-elintro-0240
title: "What is the simplified MOSFET current formula in the saturation region?"
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

For an ideal long-channel NMOS in the saturation region, `I_D = K*(V_GS - V_th)^2`, where `K` combines process and geometry parameters and depends on whether the `1/2` factor is absorbed. The model requires `V_GS > V_th` and `V_DS >= V_GS - V_th`; real current also deviates due to device non-idealities.[^aac-semiconductors]

## Detailed explanation

TODO

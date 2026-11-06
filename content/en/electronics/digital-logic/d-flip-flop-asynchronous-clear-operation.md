---
id: emb-eldig-0019
title: "How does the asynchronous clear input /CLR operate in a D-type flip-flop?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: ti-sn74hc74a
    title: "Texas Instruments: SN74HC74A Dual Positive-Edge-Triggered D-Type Flip-Flops Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc74a.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
---

## Short answer

The `/CLR` pin is typically an active-low asynchronous input, taking immediate effect regardless of the D input or CLK clock edge. Asserting logic 0 on `/CLR` immediately forces output Q to 0 (and `/Q` to 1) after the internal propagation delay. During normal synchronous operation, this pin is tied or pulled up to `V_CC` through a 10 kΩ resistor to avoid spurious reset events.[^ti-sn74hc74a] [^floyd-digital]

## Detailed explanation

TODO

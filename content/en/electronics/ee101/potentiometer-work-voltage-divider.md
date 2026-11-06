---
id: emb-elee-0012
title: "How does a potentiometer work as a voltage divider?"
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
  - source_id: bourns-potentiometer
    title: "Bourns: 3386 Trimpot Trimming Potentiometer Datasheet"
    url: https://bourns.com/docs/Product-Datasheets/3386.pdf
---

## Short answer

The outer terminals of the potentiometer connect to `V_in` and GND, with the output taken from the wiper. For an unloaded ideal divider, `V_out = V_in*R_2/(R_1+R_2)`, where `R_1+R_2 = R_total`; thus, the output varies between the voltages at the outer terminals. Output loading alters this voltage division, so the unloaded formula does not always describe a real circuit.[^bourns-potentiometer]

## Detailed explanation

TODO

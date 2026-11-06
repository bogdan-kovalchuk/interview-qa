---
id: emb-elee-0220
title: "How do you calculate the base resistor for a 100 mA motor switch with a forced gain of 10 driven from 5 V?"
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf
---

## Short answer

Base drive current must satisfy `I_B ≥ I_C/β_forced = 100 mA / 10 = 10 mA`.[^rohm-bjt-basics] This gives `R_B = (5 - 0.8)/0.01 ≈ 420 Ω`, where saturated `V_BE = 0.8 V` typically falls in the 0.7–0.9 V range.[^rohm-bjt-basics] The chosen `β_forced` must sit well below the datasheet minimum `h_FE` at this current.[^rohm-bjt-basics] The 5 V control source must be capable of sourcing the required 10 mA.

## Detailed explanation

TODO

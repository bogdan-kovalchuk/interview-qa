---
id: emb-elee-0233
title: "What do logic 0 and 1 really mean in a digital circuit?"
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
  - source_id: auburn-digital-voltages
    title: "Auburn University ELEC 3040/3050: Digital system voltages/currents and reading component data sheets (lab lecture notes)"
    url: https://www.eng.auburn.edu/~nelson/courses/elec3040_3050/LabLectures/DigitalElectricalQuantities_ARM.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Logic 0 and 1 are voltage ranges rather than exact numbers: an input recognizes LOW up to `V_IL` (maximum) and HIGH from `V_IH` (minimum), while voltages between them produce an undefined state.[^auburn-digital-voltages] Half of the supply voltage is not the threshold: for 74HC at `V_CC = 4.5 V`, the input limits are 1.35 V and 3.15 V, so 2.25 V falls entirely in the undefined region.[^ti-hc00]

## Detailed explanation

TODO

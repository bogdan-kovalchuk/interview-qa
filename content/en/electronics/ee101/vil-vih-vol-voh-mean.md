---
id: emb-elee-0234
title: "What do `V_IL`, `V_IH`, `V_OL` and `V_OH` mean?"
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

`V_IL` is the highest input voltage guaranteed to be recognized as logic 0, while `V_IH` is the lowest input voltage recognized as logic 1. `V_OL` is the maximum output voltage in logic state 0, and `V_OH` is the minimum output voltage in logic state 1.[^auburn-digital-voltages] These parameters are worst-case limits specified in the datasheet rather than nominal voltages.[^ti-hc00]

## Detailed explanation

TODO

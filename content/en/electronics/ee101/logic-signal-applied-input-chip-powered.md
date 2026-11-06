---
id: emb-elee-0171
title: "Can a 5 V logic signal be applied to the input of a chip powered from 3.3 V?"
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  - source_id: ti-sn74lvc1g125
    title: "Texas Instruments SN74LVC1G125 datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1g125.pdf
---

## Short answer

Only if the chip's datasheet confirms that the input is 5 V tolerant when powered from 3.3 V. A standard CMOS input has clamp diodes to `V_CC` and to ground, and the recommended input voltage is limited to `V_CC`, so applying 5 V exceeds recommended conditions and stresses the upper diode.[^ti-hc00] Certain inputs, such as the `SN74LVC1G125`, explicitly tolerate up to 5.5 V with a 3.3 V supply.[^ti-sn74lvc1g125] A shared ground and separate regulated rails do not by themselves ensure signal compatibility.

## Detailed explanation

TODO

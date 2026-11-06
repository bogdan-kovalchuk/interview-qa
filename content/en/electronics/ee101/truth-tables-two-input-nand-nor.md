---
id: emb-elee-0239
title: "What are the truth tables of two-input AND, NAND, OR and NOR?"
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
  - source_id: ti-hc08
    title: "TI SN74HC08 quadruple 2-input AND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc08.pdf
  - source_id: ti-hc32
    title: "TI SN74HC32 quadruple 2-input OR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc32.pdf
  - source_id: ti-hc02
    title: "TI SN74HC02 quadruple 2-input NOR gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc02.pdf
  - source_id: ti-hc04
    title: "TI SN74HC04 hex inverters datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc04.pdf
---

## Short answer

AND outputs 1 only for input 11[^ti-hc08], while NAND outputs 0 only for 11.[^ti-hc00] OR outputs 0 only for 00[^ti-hc32], while NOR outputs 1 only for 00.[^ti-hc02] The governing Boolean equations are `Y = A*B` (AND)[^ti-hc08], `Y = NOT(A*B)` (NAND)[^ti-hc00], `Y = A+B` (OR)[^ti-hc32], `Y = NOT(A+B)` (NOR)[^ti-hc02], and `Y = NOT A` (NOT).[^ti-hc04]

## Detailed explanation

TODO

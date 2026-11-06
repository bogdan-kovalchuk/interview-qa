---
id: emb-elpcb-0003
title: "What does the SMT size code 0805 mean, and why is it a good size to start with?"
track: electronics
section: pcb-design
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ipc-7351b
    title: "IPC-7351B: Generic Requirements for Surface Mount Design and Land Pattern Standard, IPC"
    url: https://www.ipc.org/ipc-7351
  - source_id: vishay-resistor-datasheet
    title: "Vishay Dale: Thick Film Chip Resistors, Industrial, CRCW Series Datasheet"
    url: https://www.vishay.com/docs/20035/dcrcw.pdf
---

## Short answer

The code uses imperial units: the first two digits indicate length and the last two indicate width in hundredths of an inch, meaning 0805 measures roughly `0.08 × 0.05` inches or `2.0 × 1.25 mm`. Components of this size remain easy to solder by hand under a magnifying glass. Designers transition to `0603` (`1.6 × 0.8 mm`) and `0402` (`1.0 × 0.5 mm`) with experience or when high packaging density is required.[^ipc-7351b]

## Detailed explanation

TODO

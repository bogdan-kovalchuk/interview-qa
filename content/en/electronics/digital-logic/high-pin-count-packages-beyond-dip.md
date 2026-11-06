---
id: emb-eldig-0024
title: "Which package types replace DIP for integrated circuits with more than 40 pins?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: jedec-jesd30
    title: "JEDEC Standard JESD30: Descriptive Designation System for Semiconductor-Device Packages"
    url: https://www.jedec.org/standards-documents/docs/jesd-30
  - source_id: ti-packaging-guide
    title: "Texas Instruments: Semiconductor and IC Packaging Terms and Guidelines"
    url: https://www.ti.com/packaging/docs/searchpackaging.tsp
---

## Short answer

A DIP package beyond 40 or 64 pins becomes excessively bulky, introducing severe PCB routing penalties. High-pin-count parts use pin grid arrays (PGA) or square PLCC packages with J-leads for socketing. Modern designs rely on surface-mount packaging (SOIC, TSSOP, QFP), employing SMT-to-DIP breakout adapters for breadboard prototyping.[^jedec-jesd30] [^ti-packaging-guide]

## Detailed explanation

TODO

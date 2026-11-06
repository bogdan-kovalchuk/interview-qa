---
id: emb-elee-0169
title: "The 3.3 V rail draws 100 mA from the 5 V rail, a separate 5 V load draws 50 mA, input 9 V. What are the losses in both regulators?"
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
  - source_id: ti-slva118a
    title: "Texas Instruments SLVA118A: Linear Regulator Design Guide For LDOs"
    url: https://www.ti.com/lit/an/slva118/slva118.pdf
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
---

## Short answer

The 3.3 V regulator dissipates `P = (5 - 3.3)*0.1 = 0.17 W`. The 5 V regulator passes approximately 150 mA (50 mA local load plus 100 mA for the 3.3 V stage) and dissipates `P = (9 - 5)*0.15 = 0.6 W`. Combined dissipation is 0.77 W neglecting quiescent currents: cascading spreads heat across two packages, but does not reduce overall linear regulation loss.[^ti-slva118a]

## Detailed explanation

TODO

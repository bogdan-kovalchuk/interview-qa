---
id: emb-elee-0185
title: "Which breadboard measures reduce motor noise on the supply?"
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
  - source_id: ti-slva959b-motor-driver-layout
    title: "TI: Best Practices for Board Layout of Motor Drivers (SLVA959B)"
    url: https://www.ti.com/lit/an/slva959b/slva959b.pdf
  - source_id: ti-slvaft0-bulk-capacitor-sizing
    title: "TI: Bulk Capacitor Sizing for DC Motor Drive Applications (SLVAFT0)"
    url: https://www.ti.com/lit/an/slvaft0/slvaft0.pdf
---

## Short answer

Key measures include bulk capacitance to buffer low-frequency motor current transients, local ceramic decoupling capacitors near ICs, short power loops, a separate return path for motor current, and small ceramics directly across the power stage.[^ti-slva959b-motor-driver-layout] A separate return path prevents motor switching currents from modulating the ground reference of sensitive logic stages.[^ti-slva959b-motor-driver-layout]

## Detailed explanation

TODO

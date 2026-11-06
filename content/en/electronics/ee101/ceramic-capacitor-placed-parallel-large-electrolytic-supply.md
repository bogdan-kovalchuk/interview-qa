---
id: emb-elee-0030
title: "Why is a 100 nF ceramic capacitor placed in parallel with a large electrolytic in a supply filter?"
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
  - source_id: ti-switching-regulator-fundamentals
    title: "Texas Instruments: Switching regulator fundamentals"
    url: https://www.ti.com/lit/an/snva559c/snva559c.pdf
---

## Short answer

A large electrolytic capacitor provides bulk capacitance for lower frequencies and slower load steps, whereas a ceramic capacitor provides a low-ESR and low-ESL path for high-frequency ripple. This is not a universal rule for arbitrary component values: impedance varies with frequency, parasitics, and layout, so any specific pair must be validated in the circuit.[^ti-switching-regulator-fundamentals]

## Detailed explanation

TODO

---
id: emb-elee-0125
title: "Why may RL filter measurements at megahertz not match the ideal model?"
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
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
---

## Short answer

For R = 1 kΩ and L = 330 µH, `f_c = R/(2*pi*L) ≈ 482 kHz`, so `10*f_c` reaches approximately 4.8 MHz. At these frequencies, the inductor's distributed capacitance (its SRF) and winding resistance alter its behavior, while breadboard capacitance, probe loading, and instrument bandwidth also distort the measurement.[^vishay-inductors-primer] If the measurement curve becomes non-monotonic, check the circuit model and layout rather than just arithmetic.

## Detailed explanation

TODO

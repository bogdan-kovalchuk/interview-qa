---
id: emb-elee-0132
title: "How does a Zener diode differ from a Schottky diode in principle and application?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: nexperia-an90056
    title: "Nexperia AN90056: Trench Schottky diodes in modern switching applications"
    url: https://assets.nexperia.com/documents/application-note/AN90056.pdf
---

## Short answer

A Zener diode operates in reverse breakdown where voltage is largely independent of current, making it useful as a reference and voltage clamp; in the forward direction it behaves like a normal silicon diode.[^nexperia-an90031] A Schottky diode features a metal-semiconductor junction with low `V_F` (typically 0.2–0.4 V versus ≈ 0.7 V for a p-n diode) and fast switching, making it ideal for switching supplies, freewheeling, and clamping.[^nexperia-an90056] The trade-offs are higher reverse leakage and lower maximum reverse voltage.[^nexperia-an90056]

## Detailed explanation

TODO

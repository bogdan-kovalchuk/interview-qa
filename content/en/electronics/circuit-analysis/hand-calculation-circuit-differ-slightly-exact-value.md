---
id: emb-elcirc-0023
title: "Why does a hand calculation of a circuit differ slightly from the exact value?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: vishay-resistor-tolerance
    title: "Vishay: Resistors – General Information"
    url: https://www.vishay.com/docs/49873/49873_sg2113.pdf
---

## Short answer

Discrepancies between manual calculations and exact solver outputs typically arise from rounding intermediate values, such as rounding `92.307... Ω` to `92.3 Ω`. This arithmetic rounding must not be confused with physical component tolerance, which specifies manufacturing variance and does not justify computational errors.[^aac-direct-current] [^vishay-resistor-tolerance]

## Detailed explanation

TODO

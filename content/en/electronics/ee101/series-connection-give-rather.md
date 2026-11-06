---
id: emb-elee-0026
title: "Why does a series connection of 10 µF and 1 µF give about 0.91 µF rather than about 11 µF?"
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
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
---

## Short answer

In a series circuit, reciprocal capacitances sum together, so for 10 µF and 1 µF, `C_total = 10*1/(10+1) ≈ 0.91 µF` rather than 11 µF. Capacitances add directly in parallel connections; a series equivalent is always smaller than the smallest individual capacitance.[^aac-capacitors-series-parallel]

## Detailed explanation

TODO

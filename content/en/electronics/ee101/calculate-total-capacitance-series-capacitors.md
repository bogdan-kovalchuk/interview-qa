---
id: emb-elee-0025
title: "How do you calculate the total capacitance of series capacitors?"
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

For a series connection, reciprocal capacitances sum together: `1/C_total = 1/C_1 + 1/C_2 + ...`; for two capacitors, this simplifies to `C_total = C_1*C_2/(C_1+C_2)`. For example, 10 µF and 22 µF yield `220/32 = 6.875 µF`, or approximately 6.88 µF. For `n` identical capacitors, the total equals the capacitance of one divided by `n`.[^aac-capacitors-series-parallel]

## Detailed explanation

TODO

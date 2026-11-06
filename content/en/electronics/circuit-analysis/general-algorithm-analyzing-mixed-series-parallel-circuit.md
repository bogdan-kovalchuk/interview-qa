---
id: emb-elcirc-0020
title: "What is the general algorithm for analyzing a mixed (series-parallel) circuit?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
---

## Short answer

Identify distinct series and parallel resistor groups and replace them with equivalent resistances until the network reduces to a single source and `R_eq`.[^aac-direct-current] Compute total source current using Ohm's law, then work backward to unfold branch voltages and currents, verifying the solution with KCL and KVL at the end.[^aac-direct-current]

## Detailed explanation

TODO

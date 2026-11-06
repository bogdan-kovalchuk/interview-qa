---
id: emb-elcirc-0032
title: "How does a load R_L change a divider's V_out and how do you calculate it?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
---

## Short answer

Connecting a load `R_L` places it in parallel with `R_2`, reducing the effective lower resistance to `R_2,eff = R_2*R_L/(R_2+R_L)`. Substitute `R_2,eff` in place of `R_2` in the standard voltage divider equation. A smaller load resistance `R_L` results in a lower effective resistance and a lower output voltage `V_out`.[^aac-direct-current]

## Detailed explanation

TODO

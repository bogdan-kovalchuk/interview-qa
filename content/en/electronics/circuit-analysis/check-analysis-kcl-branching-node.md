---
id: emb-elcirc-0024
title: "How do you check an analysis with KCL at a branching node?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-kcl
    title: "All About Circuits: Kirchhoff’s Current Law (KCL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-current-law-kcl/
---

## Short answer

Assign reference directions to every branch current and adopt a consistent sign convention, such as treating entering currents as positive and leaving currents as negative. By KCL, the algebraic sum at the node must equal zero; in the textbook example, `136 mA` enters while `125.6 mA` and `10.4 mA` leave, balancing the sum exactly to zero.[^aac-kcl]

## Detailed explanation

TODO

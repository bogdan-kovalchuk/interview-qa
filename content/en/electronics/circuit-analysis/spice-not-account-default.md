---
id: emb-elcirc-0042
title: "What does SPICE not account for by default?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-manual-models
    title: "ngspice User's Manual: Device Models and Analyses"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

SPICE calculates the behavior of specified models and operating conditions rather than automatically accounting for all real-board effects. Parasitic parameters, tolerances, temperature dependencies, and cross-coupling between traces appear in results only when represented by appropriate models or analysis directives; the available feature set depends on the simulator and netlist.[^ngspice-manual-models]

## Detailed explanation

TODO

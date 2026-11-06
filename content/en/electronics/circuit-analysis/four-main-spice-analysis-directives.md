---
id: emb-elcirc-0038
title: "What are the four main SPICE analysis directives?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-analysis-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

`.op` finds the DC operating point, `.tran` calculates time-domain transient response, `.ac` determines small-signal frequency response, and `.dc` sweeps a DC parameter or source to compute the operating point for each value.[^ngspice-analysis-manual] These names and directives follow ngspice; feature support and syntax of a specific simulator should be verified in its documentation.[^ngspice-analysis-manual]

## Detailed explanation

TODO

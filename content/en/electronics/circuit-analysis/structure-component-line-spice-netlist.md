---
id: emb-elcirc-0040
title: "What is the structure of a component line in a SPICE netlist?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-netlist-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

In ngspice, a component line typically specifies its name, the nodes required for that specific element type, and then its value or parameters.[^ngspice-netlist-manual] For example, `R1 1 2 1k` defines a resistor, while `V1 1 0 DC 5` defines a DC source between node 1 and ground node 0; the format of remaining fields depends on the component type.[^ngspice-netlist-manual]

## Detailed explanation

TODO

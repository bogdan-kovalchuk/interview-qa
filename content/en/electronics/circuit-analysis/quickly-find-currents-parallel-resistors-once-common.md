---
id: emb-elcirc-0019
title: "How do you quickly find the currents in parallel resistors once the common voltage is known?"
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

In a parallel bank, the voltage across every branch is identical because all components terminate at the same two nodes.[^aac-direct-current] Calculate each individual branch current using Ohm's law, `I_i = V/R_i`, and verify that their sum matches total current using KCL: `I_total = I_1 + I_2 + ...`.[^aac-direct-current]

## Detailed explanation

In a parallel connection, all branches share the same pair of nodes. The potential difference between these nodes is identical for every branch, meaning the same voltage `V` appears across each resistor. Each branch current can be solved independently of the others using Ohm's law: `I_i = V/R_i`.[^aac-direct-current]

After computing branch currents, sum them to find the total current entering the node from the source: `I_total = I_1 + I_2 + ...`. This is an application of KCL: at a node, total entering current equals total leaving current. If calculations are correct, substituting all branches into this relation must achieve balance.[^aac-direct-current]

Example: resistors of 2 kΩ and 4 kΩ are connected in parallel across a 12 V source. The branch currents are `12 V / 2 kΩ = 6 mA` and `12 V / 4 kΩ = 3 mA`, so the source supplies a total of 9 mA. This result assumes ideal interconnects and an ideal specified voltage without source sag.[^aac-direct-current]

A common mistake is dividing source voltage among parallel resistors as if they were connected in series. First verify that both terminals of each resistor connect to the exact same pair of nodes; also avoid adding current through a separate element that does not actually belong to this parallel group.[^aac-direct-current]

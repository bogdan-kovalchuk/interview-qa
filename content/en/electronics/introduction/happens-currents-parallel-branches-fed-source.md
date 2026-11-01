---
id: emb-elintro-0117
title: "What happens to the currents in parallel branches fed by one source?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-parallel-branches
    title: "All About Circuits: Resistors in Parallel"
    url: https://www.allaboutcircuits.com/technical-articles/resistors-in-parallel-circuit-analysis-with-parallel-resistance/
---

## Short answer

In parallel branches between the same two nodes, the voltage is the same, but the current in each branch depends on its resistance or load.[^aac-parallel-branches] At the node, the source current equals the sum of the branch currents: `I_total = I_1 + I_2 + ...`.[^aac-parallel-branches]

## Detailed explanation

In a parallel circuit, each branch is connected to the same pair of nodes, so the voltage across the branches is identical; the source current splits between the branches and equals their sum.[^aac-parallel-branches]

The current distribution is determined by the behavior of each load. For a resistive branch, Ohm's law gives `I = V/R`: at the same voltage, a branch with lower resistance draws more current. For a non-linear load, such as a lamp or an `LED`, simple division by a single constant resistance does not describe operation; the current is set by its current-voltage characteristic along with the external components.[^aac-parallel-branches]

Kirchhoff's Current Law is a consequence of charge conservation: charge does not accumulate indefinitely at a node, so the sum of currents entering equals the sum of currents leaving. For a source supplying current into a junction, this is written as the sum of the branch currents. The sign of a current depends on the chosen reference direction, so in the equation it is important to agree consistently on which currents are considered entering and leaving.[^aac-parallel-branches]

Example: resistors of `1 kΩ` and `2 kΩ` are connected in parallel to an ideal `6 V` source. The voltage across each equals the source voltage. The first resistor conducts `6 mA`, the second – `3 mA`, so the source supplies `9 mA`. A real source has internal resistance and a current limit, so the voltage can sag as the total load increases.[^aac-parallel-branches]

**Common mistake:** assuming that parallel branches divide the current equally or that the current in each branch equals the source current. It is divided equally only with corresponding identical branch characteristics; the total current is always found as the algebraic sum of the currents at the node. In a practical circuit, you must also check whether the source can handle this sum.[^aac-parallel-branches]

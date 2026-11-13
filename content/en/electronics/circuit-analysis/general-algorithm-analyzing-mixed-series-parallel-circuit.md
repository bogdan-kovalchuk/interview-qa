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

Analyzing a mixed series-parallel circuit begins with topology: trace which elements connect end-to-end along a single branch and which connect across the same pair of nodes. Resistance combination rules may only be applied to groups that strictly conform to series or parallel connections.[^aac-direct-current]

Reduce one such group to an equivalent resistance and repeat this step until the entire network simplifies to a single equivalent resistance. For a series group, resistances add directly; for a parallel group, compute the reciprocal of the sum of conductances. Then find total source current from source voltage and total resistance using Ohm's law. This constitutes the forward reduction stage of circuit analysis.[^aac-direct-current]

Next, unfold the substitutions in reverse order. Voltages across elements in a series group are determined via Ohm's law, while in a parallel group the voltage is shared; individual parallel branch currents are solved from their respective resistances. Verify that voltage drops in closed loops satisfy KVL, and currents at branch junctions satisfy KCL.[^aac-direct-current]

Example: a 1 kΩ resistor in series with a parallel pair of 2 kΩ and 2 kΩ has an equivalent resistance of `1 kΩ + 1 kΩ = 2 kΩ`. Powered by a 10 V source, the total current is 5 mA; 5 V drops across the first resistor, and the remaining 5 V appears across the parallel pair. Each branch takes 2.5 mA, so the sum of branch currents equals 5 mA.[^aac-direct-current]

**Common mistake:** applying series combination rules to elements with an intermediate branching node, or equating currents across parallel branches having unequal resistances. Verify circuit nodes rather than the geometric proximity of symbols on the schematic.[^aac-direct-current]

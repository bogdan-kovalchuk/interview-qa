---
id: emb-elcirc-0021
title: "How do you quickly check a parallel resistance calculation?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-parallel-resistance
    title: "All About Circuits: Parallel Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-parallel-circuits/
---

## Short answer

The equivalent resistance of a parallel group must always be strictly less than the smallest individual branch resistance. For `R1 = 1.2 kΩ` and `R2 = 100 Ω`, the result must be below `100 Ω`; any value equal to or greater indicates a topology or calculation mistake, such as misplaced calculator parentheses.[^aac-parallel-resistance]

## Detailed explanation

The equivalent resistance of a parallel group is the resistance of a single hypothetical resistor that produces the same voltage and total current as all branches combined. In a parallel connection, both terminals of each branch connect to the same two nodes; therefore, voltage across each resistor is identical, and branch currents sum together. By Ohm's law, branch conductances add: `1/R_eq = 1/R1 + 1/R2 + ...`; thus, an additional branch creates another current path and reduces the equivalent resistance.[^aac-parallel-resistance]

For a quick check, performing exact division every time is not necessary: because the sum of reciprocal resistances is greater than the reciprocal of any single branch resistance, `R_eq` must be smaller than the smallest branch resistor. This serves as a boundary check rather than a substitute for full calculation. It applies to resistors that genuinely share the same pair of nodes; if the circuit contains series segments or additional branches, first identify the correct topology.[^aac-parallel-resistance]

Example: for `1.2 kΩ` and `100 Ω` in parallel, the equivalent resistance is approximately `92.3 Ω`, which is strictly less than `100 Ω`. If a calculator yields a value above `100 Ω`, check the conversion of `1.2 kΩ` to ohms, operator precedence and parentheses entry, and ensure that a parallel rather than series combination is being computed.

**Common mistakes:**

- Adding nominal values directly – that is the rule for series, not parallel, connections.
- Confusing the sum of resistances with the sum of conductances; conductances `1/R` add for parallel branches.
- Applying the bounding rule to resistors that do not share both nodes on the schematic.

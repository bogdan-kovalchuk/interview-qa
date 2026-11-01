---
id: emb-elintro-0112
title: "How do you find the equivalent resistance of two parallel resistors?"
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
  - source_id: aac-simple-parallel-circuits
    title: "All About Circuits: Parallel Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-parallel-circuits/
---

## Short answer

For two resistors connected across the same two nodes, `R_eq = (R_1*R_2)/(R_1+R_2)`. This value is less than each individual resistor because the parallel connection adds an additional path for current.[^aac-simple-parallel-circuits]

## Detailed explanation

The equivalent resistance of a parallel pair is a single resistance that would draw the same total current for a given voltage between the same two nodes. In a parallel circuit, the voltage across both resistors is identical, and the total current equals the sum of the branch currents. Substituting Ohm's law for each branch gives `1/R_eq = 1/R_1 + 1/R_2`; for two resistors, this can be transformed into the product divided by the sum.[^aac-simple-parallel-circuits]

The formula assumes that both components are resistors and are connected strictly in parallel – each lead of the first is connected to the corresponding lead of the second. If they share only a single common node, they cannot be combined using this formula. For positive finite resistances, the result is less than the smaller resistance: current has two parallel paths, so conductances add. Adding resistances directly, in contrast, applies to a series connection.[^aac-simple-parallel-circuits]

Worked example:
```text
R_1 = 1 kΩ, R_2 = 2 kΩ
R_eq = (1000*2000)/(1000+2000) = 666.7 Ω
```
Thus, the equivalent resistance is approximately `667 Ω`, which is less than `1 kΩ`.[^aac-simple-parallel-circuits]

**Common mistakes:**
- Applying the formula to resistors that do not share both common nodes.
- Adding resistance values as if for a series connection.
- Forgetting to convert units to the same scale before substituting into the formula.

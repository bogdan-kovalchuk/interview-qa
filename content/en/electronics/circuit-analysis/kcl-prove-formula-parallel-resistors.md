---
id: emb-elcirc-0013
title: "How does KCL derive the equivalent resistance of resistors in parallel?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-parallel-resistors
    title: "All About Circuits: Resistance in Parallel Networks"
    url: https://www.allaboutcircuits.com/technical-articles/resistance-in-parallel-networks
---

## Short answer

For resistors connected across the same two nodes, the branch voltage `V` is identical across each element. Applying KCL and Ohm's law yields total current `I_s = V/R_1 + V/R_2`, which gives `1/R_eq = 1/R_1 + 1/R_2`, reducing for two resistors to `R_eq = R_1*R_2/(R_1+R_2)`.[^aac-parallel-resistors]

## Detailed explanation

Resistors connected in parallel have both terminals connected to the same two nodes. Because of this, the voltage across the nodes is identical for every branch, although branch currents may differ. The equivalent resistor must draw the same total current from the node as all branches combined.[^aac-parallel-resistors]

Applying KCL to the node where the source current branches yields `I_s = I_1 + I_2`. By Ohm's law, `I_1 = V/R_1` and `I_2 = V/R_2`, where `V` is the common voltage between the nodes. The equivalent resistance is defined such that for the same voltage, `I_s = V/R_eq`. Equating both expressions and dividing by non-zero `V` gives `1/R_eq = 1/R_1 + 1/R_2`. For two finite resistors, algebraic rearrangement yields the product divided by the sum.[^aac-parallel-resistors]

**Calculation example:**

Suppose `R_1 = 1 kΩ`, `R_2 = 2 kΩ`, and the voltage between the nodes equals `6 V`:

```text
I_1 = 6 V / 1 kΩ = 6 mA
I_2 = 6 V / 2 kΩ = 3 mA
I_s = I_1 + I_2 = 9 mA
R_eq = 6 V / 9 mA = 0.667 kΩ
```

The reciprocal form also yields `1/R_eq = 1/1 kΩ + 1/2 kΩ`, which is the exact same result. The equivalent resistance must be smaller than each individual branch resistance: adding a parallel path increases conductance. The formula assumes resistive elements and true parallel connection; if branches do not share the same end nodes, a common voltage cannot be substituted.[^aac-parallel-resistors]

**Common mistake:**

- Adding the resistances of parallel branches directly. Conductances `1/R` add up; the sum of resistances applies to series connections.[^aac-parallel-resistors]

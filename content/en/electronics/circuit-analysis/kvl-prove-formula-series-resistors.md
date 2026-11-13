---
id: emb-elcirc-0014
title: "How does KVL derive the equivalent resistance of resistors in series?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
---

## Short answer

In a series circuit, the identical current `I` flows sequentially through all resistors. By KVL, the source voltage equals the sum of the series voltage drops: `V_s = I*R_1 + I*R_2 + ...`, which factors into `R_eq = R_1 + R_2 + ...`.[^aac-series-circuits]

## Detailed explanation

In a series connection, elements form a single unbranched path, so the exact same current `I` passes through each resistor. The equivalent resistor is defined as a single element that produces the total voltage drop across the entire chain at that same current.[^aac-series-circuits]

Traversing the closed loop and applying KVL, the algebraic sum of voltages equals zero. If the source voltage rise is designated as `V_s` and the drops across resistors as `V_1`, `V_2`, and so forth, we obtain `V_s = V_1 + V_2 + ...`. Ohm's law for each resistor gives `V_i = I*R_i`. Substitution factors out the common current: `V_s = I*(R_1 + R_2 + ...)`. Because `V_s = I*R_eq` for the equivalent resistor, the sum of resistances is indeed the equivalent value.[^aac-series-circuits]

**Example:**

For `R_1 = 1 kΩ` and `R_2 = 2 kΩ` connected in series to an ideal `6 V` source, `R_eq = 3 kΩ` and current `I = 6 V / 3 kΩ = 2 mA`. The voltage drops are `2 V` and `4 V`; their sum reproduces the source voltage. This is consistent with KVL and Ohm's law.[^aac-series-circuits]

In a real circuit, this rule applies to components along the same unbranched path; if a parallel branch is present, currents in different branches are no longer equal. Account for wire resistance or internal source resistance separately when significant for the required accuracy. Do not confuse the sum of resistances in a series circuit with the reciprocal sum for a parallel one.[^aac-series-circuits]

**Common mistake:**

- Substituting different currents into series elements. First verify that there is no branching node between them, and then apply a single current to all voltage drops.[^aac-series-circuits]

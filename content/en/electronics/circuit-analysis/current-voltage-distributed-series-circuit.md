---
id: emb-elcirc-0008
title: "How are current and voltage distributed in a series circuit?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
---

## Short answer

In an unbranched series circuit, the identical current passes sequentially through every component. For resistors, each individual voltage drop is directly proportional to its resistance, and the sum of all component voltage drops equals the total applied source voltage.[^aac-voltage-divider]

## Detailed explanation

A series circuit provides a single unbranched path for current. Because charge cannot accumulate at intermediate nodes in steady state, the identical current passes through every component along this path. Adding another series component increases total equivalent resistance, typically decreasing circuit current for a fixed source voltage.[^aac-voltage-divider]

The voltage across a component represents the potential difference between its two terminals. For a resistor, Ohm's law gives `V = I*R`; with current held constant throughout the series string, a higher resistance produces a proportionally larger voltage drop. According to Kirchhoff's Voltage Law (KVL), the algebraic sum of voltages around any closed loop equals zero, meaning the sum of individual series voltage drops equals the total voltage supplied by an ideal source.[^aac-voltage-divider]

Example: a `12 V` source powers series resistors of `2 kΩ` and `4 kΩ`. The total resistance is `6 kΩ`, resulting in a current of `2 mA`. The first resistor drops `4 V`, and the second drops `8 V`, summing to `12 V`. This division ratio no longer holds if a load is connected in parallel with one of the resistors, as the circuit is no longer an unloaded divider.[^aac-voltage-divider]

For nonlinear components, the condition of identical series current still holds, but the rule of voltage division proportional to resistance does not apply; the component current-voltage (I-V) characteristics must be analyzed instead. Similarly, real lead resistance or source internal resistance introduces additional voltage drops when non-ideal effects are accounted for.[^aac-voltage-divider]

**Common mistakes:**

- Stating that series components share the same voltage drop; current is what remains identical throughout a series string.
- Dividing voltage proportionally by resistance values without verifying that all components are linear resistors and that the divider is unloaded.
- Forgetting to verify that individual voltage drops sum to the applied source voltage.[^aac-voltage-divider]

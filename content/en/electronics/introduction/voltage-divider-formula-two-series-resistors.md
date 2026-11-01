---
id: emb-elintro-0109
title: "What is the voltage divider formula for two series resistors?"
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
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Dividers: What They Are and What They Do"
    url: https://www.allaboutcircuits.com/technical-articles/voltage-and-current-dividers-what-they-are-and-what-they-do/
---

## Short answer

For `R1` between `V_in` and the output, and `R2` between the output and ground, the unloaded voltage is `V_out = V_in*R2/(R1 + R2)`. The formula follows from the fact that the current is identical in a series circuit, and the voltage across each resistor is proportional to its resistance. Connecting a load changes the result unless its resistance is much greater than `R2`.[^aac-voltage-divider]

## Detailed explanation

A voltage divider of two series resistors produces a fraction of the input voltage at the intermediate node. If `R1` is placed between the input and output, and `R2` between the output and ground, the same current flows through both resistors. By Ohm's law, the total current equals `V_in/(R1 + R2)`, and the voltage across the bottom resistor is the product of this current and `R2`. This gives `V_out = V_in*R2/(R1 + R2)`. This formula assumes that nothing loads the output other than `R2` itself.[^aac-voltage-divider]

Example: for `V_in = 9 V`, `R1 = 3 kΩ`, and `R2 = 6 kΩ`, the current is `9 V/(3 kΩ + 6 kΩ) = 1 mA`, so the output is `1 mA*6 kΩ = 6 V`. The resistors can be swapped, but the output is then taken from the other node and the voltage fraction changes. A divider is also not a voltage regulator: the output depends on the input voltage and the resistor values.[^aac-voltage-divider]

If you connect a load between the output and ground, it connects in parallel with `R2`; for calculation, the equivalent resistance of `R2` in parallel with the load is used instead of `R2`. A small load resistance reduces this equivalent resistance and lowers the output voltage. Common mistake – applying the unloaded divider formula to a circuit with a connected load or assuming that a divider can deliver significant current without changing voltage. For a substantial load, you typically need a buffer or voltage regulator rather than just a pair of resistors.[^aac-voltage-divider]

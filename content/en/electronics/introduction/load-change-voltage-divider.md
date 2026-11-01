---
id: emb-elintro-0110
title: "Why does a load change the voltage of a divider?"
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

A load connected from the output to ground is in parallel with the bottom resistor and reduces the equivalent resistance of that branch. Because of this, the output voltage is typically lower than in an unloaded divider; the magnitude of the change depends on the load resistance.[^aac-voltage-divider]

## Detailed explanation

In an unloaded divider, the bottom resistor `R2` is the only current path from the output node to ground. When a load `R_L` is connected to the output, it forms a parallel branch with `R2`. The equivalent resistance of this branch becomes less than `R2`, so more current flows through `R1`, and a larger fraction of the input voltage drops across the top resistor. The output voltage decreases; this is a normal consequence of loading a source that has non-zero output resistance, rather than a malfunction of the divider.[^aac-voltage-divider]

The calculation is done by replacing the pair `R2` and `R_L` with their parallel equivalent `R_eq = R2*R_L/(R2 + R_L)`, and then applying the voltage divider formula: `V_out = V_in*R_eq/(R1 + R_eq)`. For example, with `V_in = 10 V`, `R1 = 10 kΩ`, and `R2 = 10 kΩ`, without a load the output equals 5 V. If `R_L = 10 kΩ`, then `R_eq = 5 kΩ`, and `V_out` is approximately 3.33 V. All values here are ideal; actual resistor tolerances may slightly alter the result.[^aac-voltage-divider]

If the load resistance is much greater than `R2`, its effect is small and the measured voltage is close to the unloaded calculation. When `R_L` is comparable to or smaller than `R2`, the effect is already substantial. A voltmeter itself is also a load: its finite input resistance is connected in parallel with `R2`, although in many circuits it is large enough that the error can be neglected.[^aac-voltage-divider]

Common mistake – assuming that the output is determined solely by the values of the two resistors regardless of what is connected to it. To avoid it, draw the load between the output and ground and include its resistance in the parallel equivalent branch. To power a load with significant or varying current, the divider is often replaced with a buffer or regulator that better maintains the output voltage.[^aac-voltage-divider]

---
id: emb-elee-0016
title: "Why does a load change the output voltage of a potentiometer divider, and what is the practical rule?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-voltage-divider-loading
    title: "All About Circuits: Voltmeter Impact on Measured Circuit"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-8/voltmeter-impact-measured-circuit/
---

## Short answer

A connected load is in parallel with the lower section of the divider, reducing its equivalent resistance and typically lowering `V_out`. A practical rule of thumb is to choose `R_load` at least 10 times larger than the total potentiometer resistance, but this is only an approximation: loading error depends on wiper position and precision requirements.[^aac-voltage-divider-loading]

## Detailed explanation

A potentiometer operating as a divider can be modeled as two series resistors: an upper track section and a lower section between the wiper and the reference node. When a load is connected to the output, it appears in parallel with the lower section of the track. Because a parallel combination has lower equivalent resistance than either branch alone, the voltage fraction across the lower branch changes. This effect is known as loading; the unloaded voltage divider equation no longer describes the output.[^aac-voltage-divider-loading]

For a specific wiper position, let the upper section be `R_1` and the lower section be `R_2`. Then `R_2_eff = R_2 || R_load`, and the voltage is given by `V_out = V_in*R_2_eff/(R_1 + R_2_eff)`. Because `R_2_eff < R_2`, the loaded output voltage is lower than the unloaded value. In the Thévenin equivalent, the output resistance of the divider is `R_1 || R_2`; its ratio relative to `R_load` helps evaluate the loading error for the selected position.[^aac-voltage-divider-loading]

Calculation example: a 10 kΩ potentiometer is set to its midpoint, so `R_1 = R_2 = 5 kΩ`. Unloaded, the output is half of `V_in`. If `R_load = 100 kΩ`, then `R_2_eff ≈ 4.76 kΩ`, and the output fraction is approximately 0.488 of `V_in` instead of 0.500. Here, the 10:1 rule of thumb yields a small error, but a different wiper position, component tolerances, or tighter precision requirements can shift the acceptable value; always calculate the worst-case operating point or model the full range.[^aac-voltage-divider-loading]

**Common mistakes:** assuming that connecting an input does not alter the circuit, or treating 10:1 as a universal guarantee of acceptable error. A high-impedance buffer or amplifier input can mitigate loading, but for precise analog signals, one must verify input impedance, allowable tolerance, and divider output resistance. A voltmeter's internal resistance is also a load and can distort measurements unless it is substantially higher than the node resistance.[^aac-voltage-divider-loading]

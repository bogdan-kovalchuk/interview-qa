---
id: emb-elcirc-0026
title: "What does \"reverse unfolding\" mean after finding R_eq?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

After simplifying a resistive network to an equivalent resistance and solving total source current or voltage, reverse unfolding reconstructs branch voltages and currents step by step back into the original topology. Series elements share identical current while parallel branches share identical voltage, allowing Ohm's law to solve each subcircuit sequentially.[^ti-slaa067]

## Detailed explanation

"Reverse unfolding" refers to the progressive reconstruction of voltages and currents throughout the original circuit after portions of the network have been replaced by equivalent resistances. An equivalent resistance preserves network behavior only from the perspective of its external terminals: it enables solving for total source current, but by itself reveals nothing about how current divides among internal elements.[^ti-slaa067]

During circuit reduction, it is good practice to record which elements were combined and in what order. Then calculations proceed in reverse order. If an equivalent resistance replaced a series pair, the exact same current flows through each resistor, and the voltage drop across each is found via Ohm's law. If the equivalent replaced parallel branches, the voltage across each branch equals the voltage across their equivalent; each branch current is computed individually, and their sum must equal the entering node current according to KCL.[^ti-slaa067]

Example: a 12 V source powers a series 2 kΩ resistor and a parallel pair of 6 kΩ and 3 kΩ. The parallel equivalent is 2 kΩ, so total resistance equals 4 kΩ, and source current is 3 mA. The voltage drop across the series resistor is 6 V, leaving 6 V across the parallel pair. From this, branch currents are 1 mA and 2 mA; their sum returns 3 mA, verifying the calculation.[^ti-slaa067]

**Common mistakes:**

- Assuming current is identical across parallel branches. The voltage is identical, whereas current depends on branch resistance.
- Dividing total voltage among parallel resistors as if they were connected in series.
- Stopping at equivalent resistance when voltages or currents at specific nodes or components are required.

If a circuit contains multiple sources, non-linear devices, or dependent sources, simple resistance reduction may be insufficient. In such cases, nodal or mesh analysis is used while observing the constraints set by KCL, KVL, and component characteristics.[^ti-slaa067]

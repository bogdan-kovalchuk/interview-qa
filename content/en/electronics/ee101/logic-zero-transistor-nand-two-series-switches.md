---
id: emb-elee-0241
title: "Why is the logic zero of a transistor NAND with two series switches not 0 V?"
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
  - source_id: nexperia-pmbt3904
    title: "Nexperia PMBT3904 NPN switching transistor datasheet"
    url: https://assets.nexperia.com/documents/data-sheet/PMBT3904.pdf
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

In a NAND gate with two transistors in series, the output LOW level equals the sum of `V_CE(sat)` across both conducting switches, which prevents it from reaching 0 V. For a PMBT3904, the maximum `V_CE(sat)` is 0.2 V at `I_C = 10 mA` and 0.3 V at `I_C = 50 mA`, meaning two stacked transistors can introduce up to 0.4 V or 0.6 V.[^nexperia-pmbt3904] In contrast, a NOR gate with parallel transistors has its LOW level determined by a single conducting device.

## Detailed explanation

A LOW level occurs when both inputs are in state 1 and both transistors are driven into saturation: current flows from the load through the upper transistor and the lower transistor to ground. A saturated transistor is not an ideal short circuit. A saturation voltage `V_CE(sat)` remains between the collector and emitter, which depends on the collector current and the base current.

The voltage at the output equals the sum of the voltages across both transistors: `V_out = V_CE1(sat) + V_CE2(sat)`. The node between the transistors sits at a voltage of `V_CE2(sat)` relative to ground, and the upper transistor is located between the output and this node. The PMBT3904 datasheet specifies a maximum `V_CE(sat)` of 200 mV at `I_C = 10 mA`, `I_B = 1 mA`, and 300 mV at `I_C = 50 mA`, `I_B = 5 mA`.[^nexperia-pmbt3904] For two identical transistors, this results in at most 0.4 V in the first case and at most 0.6 V in the second.

**Example:** At `V_CC = 4.5 V`, the SN74HC00 has a maximum `V_IL` of 1.35 V.[^ti-hc00] If the NAND LOW level is 0.6 V (the maximum at 50 mA), the downstream input reads it as LOW with a margin of `1.35 - 0.6 = 0.75 V`. According to the same data at 10 mA, the output does not exceed 0.4 V, and the margin is `1.35 - 0.4 = 0.95 V`.

In a NOR gate, the transistors are connected in parallel, so the LOW level is determined by a single conducting transistor and is approximately equal to its `V_CE(sat)`, rather than the sum of two. Consequently, identical transistors yield different LOW levels depending on the circuit topology. A single number from a table does not guarantee a value for any current.

**Common mistakes:**

- Assuming that a saturated transistor has 0 V between its collector and emitter;
- Adding saturation voltages in a NOR gate with parallel transistors the same way as in a NAND gate with series transistors;
- Taking a single typical `V_CE(sat)` value without checking the current from the datasheet.

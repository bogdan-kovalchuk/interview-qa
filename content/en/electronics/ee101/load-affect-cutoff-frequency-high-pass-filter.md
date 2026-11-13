---
id: emb-elee-0112
title: "How does a load R_L affect the cutoff frequency of an RC high-pass filter?"
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
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
---

## Short answer

A load `R_L` connected in parallel with the output resistor R decreases the effective resistance to `R_eff = R || R_L`, so the cutoff frequency `f_c = 1/(2π*R_eff*C)` increases. For `R = R_L = 10 kΩ` and `C = 100 nF`, it shifts from approximately 159 Hz to 318 Hz.[^aac-high-pass-filters]

## Detailed explanation

For an RC high-pass filter with a series capacitor and a resistor at the output node, the resistance that defines the pole depends on the entire circuit connected to that node. If the source is ideal, its output resistance is zero, and an additional resistive load `R_L` is placed in parallel with the output R, then `R_eff = R || R_L`. Because a parallel combination cannot have a resistance greater than either branch, `R_eff` is smaller than R, and the cutoff frequency `f_c = 1/(2π*R_eff*C)` is higher.[^aac-high-pass-filters]

This does not mean that any resistor in the circuit should mechanically be placed in parallel with R. The formula assumes this exact topology, an ideal source, and a resistive load. A nonzero source resistance, the input capacitance of an instrument, or a subsequent stage may require a complete impedance analysis. In the general case, one should find the equivalent resistance seen by C after deactivating independent ideal sources, or derive the transfer function of the entire circuit directly.[^aac-high-pass-filters]

Calculation example: without a load, for `R = 10 kΩ` and `C = 100 nF`, we have `f_c = 1/(2π*10 kΩ*100 nF) ≈ 159 Hz`. If we connect `R_L = 10 kΩ`, the parallel combination is `5 kΩ`; then `f_c ≈ 318 Hz`. Thus, the same capacitance in a loaded circuit no longer matches the prior cutoff frequency calculation.[^aac-high-pass-filters]

**Common mistake:** taking only the resistor value printed on the filter schematic and ignoring the input of the next device. This can alter both the cutoff frequency and the passband gain. To avoid this, specify which nodes the load is connected between, account for its input impedance, and verify the result by analyzing or measuring the fully assembled circuit.[^aac-high-pass-filters]

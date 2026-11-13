---
id: emb-elee-0096
title: "What does a load connected to the output of an RC low-pass filter change?"
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
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

Assuming an ideal source, a load `R_L` connected in parallel with C changes both the passband gain and the cutoff frequency. For a resistive load, the effective resistance in the time constant becomes `R||R_L`, shifting the cutoff to `f_c = 1/(2π*C*(R||R_L))`. The standard formula `1/(2π*R*C)` applies only to an unloaded filter.[^aac-low-pass-filters]

## Detailed explanation

A load connected to the output of a simple RC low-pass filter provides an additional current path in parallel with the capacitor, altering the voltage divider. Consider an ideal voltage source, a series resistor `R`, and at the output node, a capacitor `C` in parallel with a resistive load `R_L`. At DC, the capacitor is an open circuit, so the output-to-input voltage ratio equals `R_L/(R+R_L)` rather than unity. Consequently, even within the passband, a real load attenuates the signal.[^aac-low-pass-filters]

For the AC component, the capacitor impedance depends on frequency, while the resistance seen by the capacitor with the ideal source zeroed out is `R||R_L`. Therefore, the first-order pole is given by `τ = (R||R_L)*C`, and the cutoff frequency is `f_c = 1/(2π*(R||R_L)*C)`. Because `R||R_L` is smaller than `R`, connecting a finite `R_L` typically raises the cutoff frequency relative to the unloaded case and reduces the low-frequency gain. The formula `1/(2π*R*C)` without accounting for the load does not provide a complete characterization here.[^aac-low-pass-filters]

**Example:** If `R = 10 kΩ`, `R_L = 10 kΩ`, and `C = 10 nF`, then `R||R_L = 5 kΩ`, yielding `f_c ≈ 3.18 kHz`, compared to approximately `1.59 kHz` for an unloaded output. The low-frequency voltage ratio in this loaded example is `10/(10+10) = 0.5`. This calculation assumes an ideal source and ideal R and C components; any nonzero source output resistance adds to the series resistance, while reactive or more complex loads require analyzing the complete impedance.[^aac-low-pass-filters]

**Common mistakes:**

- Using only `R` in the cutoff formula while ignoring the parallel load `R_L`.
- Assuming that the load can only reduce amplitude without affecting the transition frequency.
- Applying this simple formula to a load with significant frequency dependence without analyzing its complete impedance.[^aac-low-pass-filters]

---
id: emb-elee-0084
title: "At the cutoff frequency of an RL circuit, both outputs are 0.707 of the input. Why does this not contradict their forming the input together?"
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
  - source_id: aac-series-rl
    title: "All About Circuits: Series Resistor-Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/series-resistor-inductor-circuits/
---

## Short answer

For an ideal unloaded series RL circuit, `H_R + H_L = 1` as a complex equation, but this does not imply `|H_R| + |H_L| = 1`. At the cutoff frequency, both magnitudes equal `1/√2` because the voltages across R and L are 90° out of phase and add as phasors.[^aac-series-rl]

## Detailed explanation

In a series RL circuit, Kirchhoff's voltage law states that the instantaneous input voltage equals the sum of the instantaneous voltages across the resistor and the inductor. For sinusoidal steady state, the same relationships are written for complex phasors: `V_in = V_R + V_L`. Dividing by `V_in` yields `1 = H_R + H_L`, where `H_R = V_R/V_in` and `H_L = V_L/V_in`. This is an equality of complex numbers containing both magnitude and phase.[^aac-series-rl]

At the cutoff frequency, `X_L = R`. The impedances of R and L are then equal in magnitude, but the directions of the voltage phasors are mutually perpendicular: the resistor voltage is in phase with the current, while the inductor voltage leads the current by 90°. Each voltage has a magnitude of `V_in/√2`, approximately 0.707 of the input, and together the phasors form the complete input vector. By adding only the lengths of the arrows, we ignore phase and violate Kirchhoff's voltage law.[^aac-series-rl]

Example: let `V_in = 1∠0° V`. At cutoff, `V_R = 0.707∠−45° V` and `V_L = 0.707∠+45° V`. Their real components each equal approximately 0.5 V, and the imaginary components of `V_R` and `V_L` cancel each other out. The complex sum equals `1∠0° V`, even though the sum of the magnitudes equals approximately 1.414 V. RMS values or amplitudes can only be compared under a consistent convention; this does not alter the phasor logic.[^aac-series-rl]

This result applies to voltages across two series elements and does not imply that any two arbitrary outputs of any filter will have such a sum. A real winding resistance adds another component to the model, and loading can change both `V_out/V_in` ratios. To analyze a more complex circuit, one must write all impedances and apply Kirchhoff's law to phasors, rather than carrying over the number 0.707 without verifying the conditions.[^aac-series-rl]

**Common mistake:** adding 0.707 + 0.707 as scalars and claiming that the input voltage must be 1.414 units. When answering, state the phase angles and demonstrate the complex sum; when measuring with an oscilloscope, check the phase difference between channels, not just their magnitudes. Additionally, specify that both measurements are taken relative to a common reference and for the same frequency and load.[^aac-series-rl]

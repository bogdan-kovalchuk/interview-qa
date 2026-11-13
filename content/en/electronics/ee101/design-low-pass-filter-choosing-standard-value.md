---
id: emb-elee-0094
title: "How do you design a 1 kHz RC low-pass filter with R = 1 kΩ, and what should you do after choosing a standard value?"
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
  - source_id: aac-rc-low-pass-transfer
    title: "All About Circuits: Understanding Low-Pass Filter Transfer Functions"
    url: https://www.allaboutcircuits.com/technical-articles/understanding-transfer-functions-for-low-pass-filters/
---

## Short answer

For `R = 1 kΩ` and `f_c = 1 kHz`, the required capacitance is `C = 1/(2*pi*R*f_c) ≈ 159 nF`. Selecting the standard value `150 nF` shifts the actual cutoff to `1/(2*pi*1 kΩ*150 nF) ≈ 1.06 kHz`. After choosing standard components, recalculate the cutoff frequency while accounting for component tolerances and load impedance.[^aac-rc-low-pass-transfer]

## Detailed explanation

For a simple passive first-order RC low-pass filter, the cutoff frequency is determined by the product of resistance and capacitance: `f_c = 1/(2*pi*R*C)`. When `R` and the desired `f_c` are given, the required capacitance is found by rearranging the equation: `C = 1/(2*pi*R*f_c)`. This assumes the output is taken across the capacitor, the source has negligible output impedance, and the load does not significantly alter the divider.[^aac-rc-low-pass-transfer]

**Calculation example:** For `R = 1 kΩ` and `f_c = 1 kHz`, the ideal capacitance is approximately `159 nF`. Standard component series typically do not include this exact value; selecting the standard value `150 nF` shifts the recalculated cutoff frequency to approximately `1.06 kHz`. Selecting `160 nF` gives approximately `995 Hz`. The deviation from the target frequency is not a formula error; it is simply the result of standard component rounding.[^aac-rc-low-pass-transfer]

After choosing components, recalculate the actual cutoff frequency using their nominal values. For a more accurate assessment, account for the tolerances of both the resistor and the capacitor: the combination of worst-case values yields a spread of possible cutoff frequencies rather than a single guaranteed point. In addition, check the source impedance and the input impedance of the subsequent stage, as they alter the effective `R` or load the capacitor. Under significant loading, the simple single-`R` formula no longer accurately describes the cutoff; the circuit must be analyzed as a loaded divider or buffered with an active stage.[^aac-rc-low-pass-transfer]

**Common mistakes:**
- Substituting `1 kΩ` and `1 kHz` without converting units to base SI, resulting in a capacitance of the wrong order of magnitude.
- Assuming the calculated `159 nF` is an available standard value.
- Overlooking filter loading caused by the subsequent stage.

The recommended procedure is: select available standard components with suitable tolerances, recalculate `f_c`, and, if necessary, simulate or measure the physical circuit.[^aac-rc-low-pass-transfer]

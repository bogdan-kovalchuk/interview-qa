---
id: emb-elee-0074
title: "RC circuit: R = 1 kΩ, C = 100 nF, f ≈ 1591.5 Hz, input 1 V RMS. What are the current and the voltages across R and C?"
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
  - source_id: aac-series-rc-analysis
    title: "All About Circuits: Series Resistor-Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/series-resistor-capacitor-circuits/
---

## Short answer

At `f ≈ 1591.5 Hz`, with `R = 1 kΩ` and `C = 100 nF`, reactance is `X_C ≈ 1 kΩ`, yielding `Z ≈ 1000 - j1000 Ω`. For an input of `1 V RMS∠0°`, the current is approximately `0.707 mA∠45°`, giving `V_R ≈ 0.707 V∠45°` and `V_C ≈ 0.707 V∠−45°`, whose complex sum equals the input phasor. Rounding intermediate numbers yields only approximate values.[^aac-series-rc-analysis]

## Detailed explanation

In a series circuit, current is identical through the resistor and the capacitor, and the source drives the sum of two complex impedances. For `R = 1 kΩ`, `C = 100 nF`, and `f = 1591.5 Hz`, the magnitude of the capacitive reactance is approximately `1000.03 Ω`, very close to the resistor's resistance. The `1 V RMS` input is defined with a phase reference of 0°; all subsequent phasor values are likewise in RMS.[^aac-series-rc-analysis]

**Calculation:**
```text
X_C = 1/(2π*f*C) ≈ 1000.03 Ω
Z = R - j*X_C ≈ 1000 - j1000.03 Ω
I = V_in/Z ≈ 0.7071 mA∠45.001°
V_R = I*R ≈ 0.7071 V∠45.001° = 0.5000 + j0.5000 V
V_C = I*(-j*X_C) ≈ 0.7071 V∠−44.999° = 0.5000 - j0.5000 V
V_R + V_C ≈ 1.0000 + j0 V
```

The resistor voltage is in phase with the current, while the capacitor voltage lags the current by 90°. Their magnitudes are approximately equal near the cutoff frequency, but they are not in phase; therefore, one cannot add `0.7071 V + 0.7071 V` as ordinary numbers. Adding the rectangular components or complex phasors causes the imaginary parts to cancel each other out, while the real parts yield the input voltage.[^aac-series-rc-analysis]

The cutoff frequency for an ideal unloaded circuit is `1/(2π*R*C) ≈ 1591.55 Hz`. In the original formulation, the frequency is rounded to 1591.5 Hz, so the phase and reactance values are also rounded. A real source with non-zero output impedance or a load connected in parallel with the capacitor will alter the result.[^aac-series-rc-analysis]

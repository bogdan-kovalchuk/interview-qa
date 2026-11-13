---
id: emb-elee-0079
title: "RL circuit: R = 200 Ω, L = 2.2 mH, f = 100 Hz, input 7 V RMS. Why is the voltage across the coil only about 48 mV?"
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
---

## Short answer

For an ideal inductor, `X_L = 2π*f*L ≈ 1.38 Ω`, which is far smaller than `R = 200 Ω`, so nearly all of the source voltage drops across the resistor. Calculations yield approximately `35.0 mA RMS` and `48.4 mV RMS` across the inductor, with the inductor voltage leading the current by 90°.[^aac-alternating-current]

## Detailed explanation

In this series RL circuit, the inductor's reactance is determined by frequency and inductance: `X_L = 2π*f*L`. For the given values of `f = 100 Hz` and `L = 2.2 mH`, it is approximately `1.38 Ω`, significantly smaller than the `200 Ω` of the resistor. Therefore, the magnitude of the total impedance is nearly equal to the resistance of the resistor, and the current is close to `7 V/200 Ω = 35 mA`.[^aac-alternating-current]

The voltage across the inductor is the product of current and its reactance: `V_L = I*X_L ≈ 35 mA*1.38 Ω = 48.3 mV`. This is an RMS value assuming that 7 V is RMS and the components are ideal. The voltage across the inductor does not equal the source voltage: series voltages add as phasors. The resistor voltage is almost in phase with the current, while the inductor voltage leads it by 90°.[^aac-alternating-current]

Example of a complete check:
```text
X_L = 2π*100*0.0022 ≈ 1.382 Ω
|Z| = √(200² + 1.382²) ≈ 200.005 Ω
I = 7/|Z| ≈ 0.0350 A RMS
V_L = I*X_L ≈ 0.0484 V RMS
```
Thus, a result of around 48 mV is not a paradox: at this frequency, the inductor has a very low reactance compared to the resistor. If frequency or inductance is increased, `X_L` will increase and a larger portion of the voltage may drop across the inductor.[^aac-alternating-current]

**Common mistakes:**
- Assuming that a series inductor always drops most of the voltage.
- Adding `R` and `X_L` scalarly instead of vectorially.
- Confusing mH with H or RMS with peak.

A real inductor has winding resistance, and a measuring instrument has finite bandwidth and accuracy. For these parameters, their effect can be noticeable relative to the expected tens of millivolts; measure the voltage directly at the inductor terminals and account for the actual winding resistance.[^aac-alternating-current]

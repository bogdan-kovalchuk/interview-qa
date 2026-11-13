---
id: emb-elee-0072
title: "What is the sequence of phasor analysis for a series RC circuit?"
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

Set the source phase to 0°, compute `Z_C = 1/(j*2π*f*C) = -j/(2π*f*C)`, and find the total impedance as `Z = R + Z_C`. Calculate the current `I = V_in/Z`, then the voltages `V_R = I*R` and `V_C = I*Z_C`. Finally, verify the complex relationship `V_R + V_C = V_in`.[^aac-series-rc-analysis]

## Detailed explanation

Phasor analysis of a series RC circuit begins with a single specified frequency and the selection of a phase reference, typically the source voltage with an angle of 0°. At this frequency, the resistor has an impedance `Z_R = R`, and the capacitor has `Z_C = 1/(j*2π*f*C) = -j/(2π*f*C)`. In a series circuit, impedances add as complex numbers, so `Z = R + Z_C`; magnitudes of individual impedances cannot be added directly.[^aac-series-rc-analysis]

Next, apply the AC form of Ohm's law: `I = V_in/Z`. The current is identical through the series components, so `V_R = I*R` and `V_C = I*Z_C`. Because multiplication and division are performed using complex arithmetic, polar representations are convenient for finding phases, whereas rectangular representations are convenient for summation. Kirchhoff's voltage law requires that the complex sum of the voltage drops equals the source voltage.[^aac-series-rc-analysis]

**Calculation example:** for `R = 1 kΩ`, `C = 100 nF`, `f = 1 kHz`, and a `1 V RMS` source, the reactance is approximately `1.592 kΩ`. The total impedance is `1000 - j1592 Ω`, its magnitude is about `1.880 kΩ`, and the current is approximately `0.532 mA` with a positive phase of about 58°. The voltage across the resistor is in phase with the current, while the capacitor voltage lags it by 90°; their sum recovers the source phasor.[^aac-series-rc-analysis]

The model assumes linear ideal components and sinusoidal steady state. Parasitic capacitor ESR, source impedance, and loading can alter the result in a real circuit. Do not substitute the complex balance with a scalar sum of magnitudes: the phase difference means vector lengths do not add arithmetically.[^aac-series-rc-analysis]

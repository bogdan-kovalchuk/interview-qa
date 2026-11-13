---
id: emb-elee-0089
title: "How does resistor heating in an RC circuit change if the source voltage is doubled with the same R, C and frequency?"
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

For constant R, C, and frequency, doubling the sinusoidal voltage doubles the current and quadruples the average power dissipated in R, since `P_R = I_RMS^2*R`.[^aac-alternating-current] This assumes linear components that do not overheat or change parameters.[^aac-alternating-current]

## Detailed explanation

In a linear RC circuit with constant R, C, and frequency, the total impedance remains constant, so the current is directly proportional to the source voltage. Doubling the voltage doubles the current, and the power dissipated by the resistor depends on the square of the current: `P_R = I_RMS^2*R`.[^aac-alternating-current]

This conclusion applies to the average power over a cycle of a sinusoidal signal. The formula uses RMS current; for a sine wave, `I_RMS = I_peak/sqrt(2)`. If the peak voltage is doubled, the RMS voltage also doubles, so the same factor of four applies to average heating.[^aac-alternating-current]

The calculation assumes linear operation: resistance does not change with temperature, the capacitor dielectric does not break down, the source maintains its waveform, and the frequency and load remain constant. In a real circuit, substantial heating can change the resistor's resistance, while generator current limits or saturation of other elements would disrupt the simple proportionality. In that case, measure the actual RMS current and compute the power from it.[^aac-alternating-current]

**Common mistakes:**
- Doubling the power by only a factor of two simply because the voltage doubled.
- Substituting peak current into the RMS formula without the appropriate factor for a sine wave.

For example, if initially `I_RMS = 10 mA` and `R = 100 Ω`, the power is `10 mW`. After doubling the voltage and current to `20 mA RMS`, the power equals `40 mW`, which is a fourfold increase.[^aac-alternating-current]

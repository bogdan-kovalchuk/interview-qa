---
id: emb-elintro-0135
title: "What is a capacitor's ESR in simple terms?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: kemet-ripple-current-mlcc
    title: "KEMET, Ripple Current and MLCC: Basic Principles"
    url: https://www.kemet.com/en/us/technical-resources/ripple-current-and-mlcc-basic-principles.html
---

## Short answer

`ESR` is the equivalent series resistance that models the losses of a real capacitor. Ripple current heats it by approximately `P = I_rms^2*ESR`; suitability depends on current, frequency, and thermal conditions. For a switching power supply, select the component from the datasheet, rather than relying solely on a low-ESR label.[^kemet-ripple-current-mlcc]

## Detailed explanation

In a simple model, a capacitor consists of an ideal capacitance, a series ESR, and a parasitic inductance ESL. ESR summarizes the resistive losses in the dielectric, electrodes, and contacts. This is an equivalent parameter: the real loss distribution is more complex and frequency-dependent.[^kemet-ripple-current-mlcc]

Think of a capacitor as a small charge reservoir with internal resistance. When ripple current flows through it, an additional voltage drop appears across the ESR, and power is dissipated as heat. For estimation, use the RMS value of the current: `P = I_rms^2*ESR`. You cannot directly substitute the peak current value into this formula unless it equals the RMS value.[^kemet-ripple-current-mlcc]

The ESR value depends on measurement frequency, temperature, and construction. Even identical capacitance and package do not guarantee the same ESR across different series. Component heating also depends on heat dissipation by the board and surrounding air, so check the frequency curves, permissible ripple current, and temperature conditions in the datasheet.[^kemet-ripple-current-mlcc]

Example: with `I_rms = 0.2 A` and an ESR of `0.5 Ω`, the power loss is `0.2^2*0.5 = 0.02 W`. With unchanged ESR, increasing the current to `0.4 A` increases the estimate to `0.08 W`, which is a fourfold increase.

**Common mistake:** calling ESR "capacitance" or assuming its value is identical at all frequencies. For practical comparison, look at the ESR at the required frequency and ensure that heating and ripple stay within the limits of the circuit and component.[^kemet-ripple-current-mlcc]

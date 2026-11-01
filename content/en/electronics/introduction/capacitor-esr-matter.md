---
id: emb-elintro-0131
title: "What is a capacitor's ESR and why does it matter?"
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
  - source_id: analog-devices-an1099-capacitor-selection
    title: "Analog Devices, AN-1099: Capacitor Selection Guidelines for Analog Devices, Inc., LDOs"
    url: https://www.analog.com/en/resources/app-notes/an-1099.html
  - source_id: kemet-ripple-current-mlcc
    title: "KEMET, Ripple Current and MLCC: Basic Principles"
    url: https://www.kemet.com/en/us/technical-resources/ripple-current-and-mlcc-basic-principles.html
---

## Short answer

ESR (Equivalent Series Resistance) is the equivalent series resistance that models the resistive losses of a real capacitor. For a ripple current with an RMS value of `I_rms`, the power loss is approximately `P = I_rms^2*ESR`, so a high ESR can cause heating; the specific value depends on frequency and construction.[^kemet-ripple-current-mlcc]

## Detailed explanation

ESR is not a separate physical resistor that can necessarily be found inside the package, but a simplified parameter of an equivalent model. A real capacitor has losses in the dielectric, electrodes, and leads; over a certain frequency range, it is convenient to describe them with a series resistance alongside ideal capacitance and inductance.[^kemet-ripple-current-mlcc]

When an AC current component flows through a capacitor, a voltage drop develops across the ESR, and part of the energy turns into heat. For an approximately constant ESR, average power loss is estimated as `P = I_rms^2*ESR`: doubling the current results in approximately a fourfold increase in losses. Here `I_rms` is specifically the RMS value of the ripple current, not its peak or average value.[^kemet-ripple-current-mlcc]

The ESR value is not a fixed characteristic independent of operating conditions: it varies with frequency, temperature, and capacitor type. Heating also depends on the thermal resistance of the package, printed circuit board, copper traces, and surrounding environment, so the formula alone is not sufficient to confirm component suitability.[^kemet-ripple-current-mlcc]

Example: if `I_rms = 0.5 A` and the ESR at the operating frequency is `0.1 Ω`, the estimate is `P = 0.5^2*0.1 = 0.025 W`. This represents only the losses in the equivalent resistance, not a complete thermal forecast for the board.

**Common mistake:** assuming that "lower ESR" is automatically better in any circuit. It often reduces losses and ripple, but the allowable capacitance and ESR may be dictated by regulator stability requirements; they must be verified against the documentation for that specific circuit.[^analog-devices-an1099-capacitor-selection]

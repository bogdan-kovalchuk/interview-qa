---
id: emb-elintro-0132
title: "Which capacitor type is best for a supply bypass filter?"
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
  - source_id: analog-devices-an140-capacitor-selection
    title: "Analog Devices, AN-140: Basic Concepts of Linear Regulator and Switching Mode Power Supplies"
    url: https://www.analog.com/en/resources/app-notes/an-140.html
---

## Short answer

For local high-frequency bypass, MLCCs are typically chosen because of their low ESR and ESL. For bulk filtering or significant ripple current, an electrolytic capacitor may be added; the type and value depend on circuit requirements, operating frequency, and the IC datasheet.[^analog-devices-an140-capacitor-selection] For a ceramic capacitor, check the effective capacitance at the operating voltage.[^analog-devices-an140-capacitor-selection]

## Detailed explanation

For high-frequency bypass near an IC, an MLCC (multilayer ceramic capacitor) is typically chosen: it is compact and has low ESR and ESL, which helps deliver short current pulses and reduce high-frequency power supply impedance.[^analog-devices-an140-capacitor-selection]

However, the "best type" depends on the capacitor's function. In a buck converter, a ceramic capacitor can work in parallel with an aluminum electrolytic: the selection accounts for RMS ripple current, required capacitance, load, and operating frequencies. For each specific IC, also verify the recommended values and stability requirements.[^analog-devices-an140-capacitor-selection]

The nominal capacitance marked on a ceramic capacitor's package does not always equal its effective capacitance under voltage. Dielectrics such as X5R or X7R can lose part of their capacitance due to DC bias and temperature, so you must check the specific component's chart over the range of operating voltages.[^analog-devices-an140-capacitor-selection]

**Common mistake:** placing a single capacitor far from the load and expecting it to remove all ripple. For local bypass, a short connection between the power pin and ground is essential; long traces add parasitic inductance. An example of a specific solution for a buck supply is parallel MLCC and electrolytic capacitors at the input, if required by the ripple current and circuit.[^analog-devices-an140-capacitor-selection]

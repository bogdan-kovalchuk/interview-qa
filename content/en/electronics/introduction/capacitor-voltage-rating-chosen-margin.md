---
id: emb-elintro-0134
title: "Why should a capacitor's voltage rating be chosen with a margin?"
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

A capacitor's operating voltage must remain within its datasheet limits, taking into account peaks and ripple; the required margin depends on technology, temperature, and operating conditions. There is no universal `1.5×–2×` rule for all capacitors – use the derating specified by the manufacturer and the circuit.[^analog-devices-an140-capacitor-selection]

## Detailed explanation

The voltage rating in the datasheet defines the limit of applied voltage under specified conditions. In a real circuit, the voltage can include not only a DC component but also ripple and short transient spikes; all these components must be considered so that the voltage across the component does not exceed the permissible limit.[^analog-devices-an140-capacitor-selection]

A safety margin is necessary because the operating point changes due to supply tolerances, load, temperature, and transient events. However, its magnitude is not a fixed proportion for every capacitor. For a switching supply, the circuit designer may require adequate voltage derating, while the capacitor manufacturer specifies particular limits for the series and operating conditions.[^analog-devices-an140-capacitor-selection]

Check the worst-case voltage at the terminals: maximum DC voltage combined with ripple and transients, and for the AC component, its amplitude and waveform. Specifically for MLCCs, verify the effective capacitance under DC bias: a margin in rated voltage can reduce capacitance loss, but this depends on the dielectric, package, and specific part.[^analog-devices-an140-capacitor-selection]

Example: if a rail is nominally `12 V`, but peaks of `15 V` are possible across the capacitor, make the selection based on the actual maximum voltage and datasheet recommendations, rather than just the number `12 V` on the schematic. Also check ripple current and temperature, as electrical voltage is not the only factor affecting lifespan.[^analog-devices-an140-capacitor-selection]

**Common mistake:** mechanically multiplying the operating voltage by the same factor for ceramic, electrolytic, and film capacitors. First determine the maximum voltage and temperature in the circuit, then verify the specific component against manufacturer tables, charts, and requirements.[^analog-devices-an140-capacitor-selection]

---
id: emb-elintro-0204
title: "How do you calculate `I_B` through a base resistor?"
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
  - source_id: aac-ohms-law
    title: "Ohm’s Law – How Voltage, Current, and Resistance Relate, All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
---
## Short answer

If the emitter is connected to 0 V and the control source supplies `V_in` through `R_B`, then `I_B ≈ (V_in - V_BE)/R_B`. For `V_in = 5 V`, `R_B = 3.3 kΩ`, and the assumption `V_BE = 0.7 V`, this yields `I_B ≈ 1.3 mA`; the actual `V_BE` depends on the transistor and current.[^aac-ohms-law]

## Detailed explanation

Base current in a simple single-resistor circuit is calculated using Ohm's law: the voltage across the resistor divided by its resistance. If the NPN emitter is grounded, one end of `R_B` is connected to the source `V_in`, and the other is connected to the base, then approximately `I_B = (V_in - V_BE)/R_B`. Here the voltage drop between base and emitter is subtracted from the source voltage, because the remainder of the voltage drops across the resistor.[^aac-ohms-law]

The formula assumes that the source has a known output voltage, the emitter has a specified reference potential, and the base–emitter junction is forward-conducting. If the emitter is not at ground, you must use the voltage relative to the emitter. If there is output resistance or other components between the source and the resistor, they must also be taken into account in the complete circuit; you cannot simply substitute the source voltage for the actual voltage across the resistor.[^aac-ohms-law]

For an example with `V_in = 5 V`, `V_BE = 0.7 V`, and `R_B = 3.3 kΩ`, the voltage across the resistor is about 4.3 V. The calculation gives `4.3 V / 3300 Ω ≈ 0.00130 A`, which is approximately 1.3 mA. The value 0.7 V is an approximation for a silicon junction: it depends on current, temperature, and the component. For more precise design, use datasheet conditions or a transistor model.[^aac-ohms-law]

Calculating the base current is only part of selecting the resistor. You need to verify whether the driving source can deliver this current, ensure maximum input ratings are not exceeded, and determine what load current needs to be switched. For a switch, base current is typically specified with a margin relative to the minimum gain to ensure the transistor reliably enters saturation.[^aac-ohms-law]

**Common mistake:** using `V_in/R_B` and forgetting the `V_BE` drop, or automatically assuming the emitter is grounded. First determine the voltage at both terminals of the resistor, and then apply Ohm's law.

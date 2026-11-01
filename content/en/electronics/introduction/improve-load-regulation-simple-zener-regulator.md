---
id: emb-elintro-0191
title: "How can you improve the load regulation of a simple Zener regulator?"
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
  - source_id: aac-common-collector
    title: "All About Circuits: The Common-collector Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-collector-amplifier/
---

## Short answer

Add an `NPN` transistor as an emitter follower: connect the base to the Zener node, the collector to `V_in`, and the emitter to the load. The Zener diode then sets the base voltage, while the load receives the higher current from the collector; the base current is approximately equal to the load current divided by β + 1. This reduces the effect of load changes on the Zener current, but the result is limited by β, voltage headroom, and transistor power dissipation.[^aac-common-collector]

## Detailed explanation

An emitter follower based on an `NPN` transistor can improve the load regulation of a simple Zener regulator because it decouples the load from the node that establishes the reference voltage. In the basic circuit, the current through the series resistor is divided between the Zener diode and the load. When the load changes, its current directly alters the available Zener current, and therefore the voltage stability.[^aac-semiconductors]

In a follower, the base is connected to the regulated node, the collector to the power supply, and the load to the emitter. The emitter voltage follows the base voltage with an offset of approximately `V_BE`; the load current is supplied by the transistor, while the Zener node only has to supply mainly the base current. In a simplified model `I_E ≈ (β + 1)*I_B`, so the current demand on the Zener diode can be significantly reduced. Real-world β varies between individual parts and depends on current and temperature, so calculations must use the guaranteed minimum value from the datasheet rather than an expected typical value.[^aac-common-collector]

This stage is not an ideal regulator: it does not step up voltage, and the emitter cannot reach the collector voltage without the necessary headroom margin for the transistor. You must verify the minimum input voltage, maximum current, and power dissipation of the transistor, as well as the remaining Zener current under worst-case load. If the supply sags or the transistor enters saturation, the output voltage ceases to follow the target value.[^aac-common-collector] [^aac-semiconductors]

Example: if the load requires `100 mA` and β = 100 is assumed for estimation, the base current will be approximately `100 mA/101 ≈ 0.99 mA`. This is an approximate estimate for the operating point, not a universal guarantee: at a lower β, the base current and the loading on the Zener diode will increase.

**Common mistake:** assuming that the transistor itself steps up voltage or that the coefficient β is always 200. It provides current gain only within its permissible operating region, and verification requires the specific transistor parameters and thermal conditions.[^aac-common-collector]

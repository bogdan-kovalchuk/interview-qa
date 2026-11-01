---
id: emb-elintro-0206
title: "How does a simple `NPN` circuit work as a logic inverter?"
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
---
## Short answer

In a common-emitter inverter circuit, a low input turns off the `NPN` transistor, and the collector load pulls the output high.[^aac-semiconductors] A high input drives current into the base and drives the collector output low.[^aac-semiconductors]

## Detailed explanation

In a simple `NPN` inverter, the transistor pulls the output to ground when sufficient current is supplied to the base, so the output logic level is inverted relative to the input.[^aac-semiconductors]

Typically, the emitter is connected to ground, the collector is connected to the supply through a load, and the input drives the base through a resistor. With a low input, the base–emitter junction is not forward-biased, the transistor conducts negligible current, and the load resistor pulls the collector high. With a high input, base current turns on the transistor: collector current flows through the load, and the collector voltage drops. This produces inversion: a low input yields a high output, and a high input yields a low output.[^aac-semiconductors]

The base resistor limits current from the logic signal source; without it, you can exceed the maximum allowable GPIO current or damage the base–emitter junction. The collector resistor sets the load current, which is why the circuit is not an ideal switch: in the on state, a non-zero `V_CE(sat)` remains, and turn-off speed depends on stored charge. The output also cannot rise above the collector supply voltage.

Example: if the collector is connected to `5 V` through an LED with a series resistor, turning the transistor on illuminates the LED and makes the collector output low; turning the transistor off leaves the output high and the LED unlit. The LED resistor is chosen based on the LED current and available voltage, while the base resistor is selected based on the required collector current and driver capabilities.[^aac-direct-current]

**Common mistake:** treating the circuit as non-inverting or applying voltage directly to the base. First identify the output node at the collector, verify the transistor state for both input levels, and limit the base current.

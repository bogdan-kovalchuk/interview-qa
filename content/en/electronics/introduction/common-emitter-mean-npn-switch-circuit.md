---
id: emb-elintro-0225
title: "What does `common emitter` mean in an NPN switch circuit?"
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
  - source_id: aac-common-emitter
    title: "All About Circuits: The Common-emitter Amplifier"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/common-emitter-amplifier/
---

## Short answer

In a `common emitter` configuration, the base input circuit and the collector output circuit share the emitter as a common reference point; in a typical NPN switch, it connects to `GND`. With a collector load connected to the supply rail, the output is inverted: a conducting transistor results in a low collector level.[^aac-common-emitter]

## Detailed explanation

The name `common emitter` describes the connection topology: the emitter serves as a common node for both the base input circuit and the collector output circuit. "Common" refers to the shared electrical reference node of these circuits, not necessarily ground in every possible application. In a simple NPN switch, the emitter is typically tied to `GND`, the base receives the control signal, and the output is taken from the collector.[^aac-common-emitter]

When the base does not turn on the transistor, `cutoff` makes the collector–emitter path practically open; the collector resistor then pulls the output up to the supply. When base current is sufficient for saturation, the transistor conducts, the collector approaches the emitter potential, and the output level drops. Thus, inversion results from the resistive collector load and transistor behavior, rather than simply from the configuration name.[^aac-common-emitter]

**Example:** with the emitter grounded and a resistor between `V_CC` and the collector, a low level at the base leaves the collector high, while a high level providing sufficient base current pulls the collector low. Actual voltages depend on the supply, the load, and transistor characteristics.[^aac-common-emitter]

**Common mistake:** treating `common emitter` as synonymous with "emitter is always connected to ground" or as a guarantee of inversion under any load. Locate the common node on the schematic and trace separately how the load establishes the output voltage.[^aac-common-emitter]

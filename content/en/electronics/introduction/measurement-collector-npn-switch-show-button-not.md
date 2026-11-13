---
id: emb-elintro-0221
title: "What does a measurement at the collector of an NPN switch show when the button is not pressed?"
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
  - source_id: aac-bjt-switch
    title: "All About Circuits: The Bipolar Junction Transistor (BJT) as a Switch"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/transistor-switch-bjt/
---

## Short answer

When the button is not pressed and the base receives no current, the NPN transistor is in `cutoff`, so collector current is practically zero. In a typical circuit with a resistor between the collector and `V_CC`, the voltage drop across the resistor is negligible, and the collector voltage is close to `V_CC`, not necessarily 5 V.[^aac-bjt-switch]

## Detailed explanation

In a typical NPN switch, the emitter is connected to common ground, and the load connects the supply rail to the collector. The button controls base current: when open, the base receives no forward current, so the transistor enters `cutoff` and the collector–emitter path behaves approximately like an open switch.[^aac-bjt-switch]

Because practically no load current flows, the voltage drop across the series load resistor is negligible. Consequently, the collector voltage approaches the supply voltage. It cannot automatically be called 5 V: it is determined by the power source in the specific circuit. A real transistor is also not an ideal switch, so a small leakage current and measurement deviations are possible.[^aac-bjt-switch]

**Example:** if the collector load is a resistor from `V_CC` to the collector and the button supplies no base current, nearly the entire source voltage is measured across the collector and emitter. The multimeter reading will be close to `V_CC`, provided there is no other current path or load altering the node's state.[^aac-bjt-switch]

**Common mistake:** assuming the collector level is universally fixed at 5 V. First determine which supply the collector resistor is tied to and relative to which node voltage is measured; `cutoff` describes the transistor operating region, not the supply rail voltage.[^aac-bjt-switch]

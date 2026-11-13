---
id: emb-elintro-0222
title: "What does a collector measurement show when the NPN switch is on and saturated?"
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

In a saturated NPN switch, the voltage `V_CE(sat)` is low but non-zero; its specific value depends on the transistor and the load current. Therefore, the collector voltage is close to the emitter voltage if the emitter is connected to `GND`.[^aac-bjt-switch]

## Detailed explanation

An enabled NPN switch receives sufficient base current to enter saturation: both transistor junctions are forward-biased, and the collector-to-emitter voltage becomes low. The transistor resembles a closed switch, but actual `V_CE(sat)` is non-zero and depends on the device type and collector current.[^aac-bjt-switch]

If the emitter is connected to `GND`, measuring collector voltage relative to ground yields approximately `V_CE(sat)`. It should not be confused with the supply voltage or treated as a universal constant. Datasheets specify saturation under defined conditions, including collector and base currents; a value from one demonstration circuit does not automatically carry over to another.[^aac-bjt-switch]

**Example:** in a measurement with the emitter at ground, a reading of around 0.1 V indicates that the transistor is conducting and drops only a small voltage. A reading of several volts with the same supply may indicate that the transistor is not saturated, the load or wiring differs, or the wrong node is being probed.[^aac-bjt-switch]

**Common mistake:** stating that `V_CE(sat)` is zero volts or giving a guaranteed range without specifying the part number and test conditions. For design calculations, take the parameter from the transistor datasheet under conditions close to your circuit.[^aac-bjt-switch]

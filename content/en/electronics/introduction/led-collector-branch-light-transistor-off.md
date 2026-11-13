---
id: emb-elintro-0223
title: "Why does an LED in the collector branch light up when the transistor is off?"
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

If the resistor and LED form a separate closed path from `+V` to `GND`, current in this path does not flow through the transistor, so the LED can light up in the `cutoff` state. This depends on the connections of the specific circuit.[^aac-bjt-switch]

## Detailed explanation

An LED lights up only when forward current flows through it. In a circuit where its branch runs from the positive supply through a current-limiting resistor and LED to `GND`, this path is closed regardless of the NPN transistor state if the branch does not actually route through the transistor. Therefore, an off transistor does not necessarily turn off the LED.[^aac-bjt-switch]

This differs from a typical low-side switch where the load is placed between `V_CC` and the collector, and the transistor completes the path to ground. There, in `cutoff`, collector current is practically zero, so the load is turned off. Determine the state of the LED by following the complete closed current path rather than merely assuming the LED is controlled simply because it is described as being in the "collector branch."[^aac-bjt-switch]

**Example:** in a branch from `+V` through a resistor and LED to `GND`, a turned-off (`cutoff`) or removed NPN does not interrupt current because neither of these components forms part of the collector–emitter path. If the LED is connected in series with the collector, the result is different and that specific topology must be analyzed.[^aac-bjt-switch]

**Common mistake:** assuming that any LED near the collector turns off when the transistor turns off. Trace current from source to return, check LED polarity, and verify the presence of a current-limiting resistor.[^aac-bjt-switch]

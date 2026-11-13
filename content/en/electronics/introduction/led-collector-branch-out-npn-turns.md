---
id: emb-elintro-0224
title: "Why does an LED in the collector branch go out when the NPN turns on?"
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

In this circuit, the saturated NPN pulls the collector to a low voltage and shunts the LED branch, reducing the current through the LED. This produces an inversion: an active-high input signal corresponds to a low collector level.[^aac-bjt-switch]

## Detailed explanation

In a typical low-side switch, the NPN emitter is connected to ground, and the collector load is tied to the supply rail. When base current drives the transistor into saturation, the collector voltage approaches the emitter voltage. The collector node becomes low relative to ground – this represents an inversion of the input drive.[^aac-bjt-switch]

An LED goes out only in a configuration where a conducting transistor reduces the voltage across the LED or shunts its current branch. The phrase "LED in the collector branch" alone does not fully define the circuit. If an LED is placed in series with a load powered through the collector, turning on the NPN will instead pass greater current through the LED. The determining factors are the connection nodes and component polarities.[^aac-bjt-switch]

**Example:** if an LED branch is connected between the collector node and ground, and the NPN turns on in parallel with it, low `V_CE(sat)` leaves little voltage across the LED; its current may become insufficient for visible light. In a specific measurement, measure voltage directly across the LED rather than drawing conclusions solely from the logic level at the base.[^aac-bjt-switch]

**Common mistake:** asserting that a turned-on NPN always turns off an LED. First sketch the closed current paths in both states and determine whether the transistor is in series with the LED or shunts it.[^aac-bjt-switch]

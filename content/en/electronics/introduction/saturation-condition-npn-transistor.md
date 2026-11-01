---
id: emb-elintro-0203
title: "What is the saturation condition for an `NPN` transistor?"
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
  - source_id: aac-bjt-active-mode
    title: "Active-mode Operation (BJT), All About Circuits"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/active-mode-operation-bjt/
---
## Short answer

In saturation, both NPN junctions, base–emitter and base–collector, are forward-biased; in a standard configuration, this yields `V_B > V_E` and `V_B > V_C`. Collector current is then limited by the power supply and load circuit rather than the approximate relationship `I_C ≈ β*I_B`; `V_CE(sat)` depends on the transistor and measurement conditions.[^aac-bjt-active-mode]

## Detailed explanation

Saturation in a BJT is the mode in which both p-n junctions of an NPN transistor are forward-biased: base–emitter and base–collector. For a common circuit configuration with the emitter at the lowest potential, this means the base has a higher potential than both the emitter and the collector. Unlike active mode, collector current can no longer increase proportionally to base current: it is dictated by the power supply and load resistance.[^aac-bjt-active-mode]

For a switching circuit with a collector resistor, the available current is approximately determined by the difference between the supply voltage and the transistor drop, divided by the load resistance. If the base current is insufficient, the transistor remains in active mode with a larger voltage drop; when the base drive calls for more current than the load can deliver, the operating point enters saturation. Increasing the base current beyond this point primarily adds excess stored charge and can increase turn-off time, rather than appreciably increasing the load current.[^aac-bjt-active-mode]

`V_CE(sat)` is not a universal number of 0.1 V or 0.2 V. In the transistor documentation, it is specified for particular collector and base currents; the value depends on the component type and the forced current gain. To design a switch, you must use the appropriate datasheet table rather than transferring a typical example to any transistor.[^aac-bjt-active-mode]

**Example:** suppose there is a 5 V supply, a 1 kΩ collector resistor, and the saturation drop for the selected model at the given current is 0.2 V. Then the load current is approximately `(5 V - 0.2 V)/1 kΩ = 4.8 mA`; a larger base current will not force the resistor to conduct significantly more under these conditions.[^aac-bjt-active-mode]

**Common mistake:** asserting that in saturation `V_CE` is always exactly equal to 0.1 V. Verify the conditions under which the datasheet specifies `V_CE(sat)`, and do not use the active model to calculate a switch in saturation.

---
id: emb-elintro-0217
title: "`PNP` high-side switch: which signal turns it on, `HIGH` or `LOW`?"
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

A `PNP` high-side switch turns on when the base is lower than the emitter, so in a typical common-ground circuit this is often `LOW`. The junction forward voltage depends on current and device characteristics, so a fixed `0.7 V` is not an exact universal threshold; a GPIO level is suitable only when supply voltages are compatible.[^aac-semiconductors]

## Detailed explanation

In a typical PNP high-side switch, the emitter is connected to the positive rail, and the load is placed between the collector and the lower rail. To turn on the transistor, the base–emitter junction must be forward-biased: the base potential must be lower than the emitter potential. Therefore, control relative to ground often has an active-low level, unlike a common low-side NPN switch.[^aac-semiconductors]

The word "often" is important. A microcontroller `LOW` can be sufficient if the emitter supply is low, a common ground is defined, and base current is limited by a resistor. If the emitter is connected to a voltage higher than the allowable GPIO levels, directly connecting the base to the GPIO can violate its maximum ratings even in the `HIGH` state. For such circuits, a separate driver is used, such as an NPN transistor, and permissible voltages and currents are verified against component documentation.[^aac-semiconductors]

In the off state, the base must be at approximately the emitter potential so that the base–emitter junction does not remain forward-biased. When the driver pulls the base down to a lower potential through a resistor, base current flows and collector current powers the load. Thus, whether the answer is `HIGH` or `LOW` depends on the circuit: one must compare the base voltage specifically to the emitter voltage and take into account how the driver is connected.[^aac-semiconductors]

**Common mistake:** calling `LOW` an unconditional rule without defining ground and emitter voltage. To verify the circuit, trace the current path from the emitter through the collector to the load and determine whether the base is low enough relative to the emitter to turn on the junction without exceeding absolute maximum ratings. The base resistor and driver are selected considering supply voltages, required load current, and the transistor datasheet.[^aac-semiconductors]

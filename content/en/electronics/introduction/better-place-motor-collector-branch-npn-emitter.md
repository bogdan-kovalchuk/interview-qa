---
id: emb-elintro-0228
title: "Why is it better to place a motor in the collector branch of an NPN than in the emitter branch?"
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

For a low-side NPN switch, the motor is placed between the supply and the collector while the emitter is connected to ground; placing it in the emitter creates an emitter follower, leaving less voltage for the motor due to `V_BE`. A protective diode is required in parallel with the motor to provide a path for inductive current during turn-off.[^aac-semiconductors]

## Detailed explanation

In a low-side NPN circuit, the emitter shares a common node with ground, and the motor is positioned between the positive supply rail and the collector. When the base receives sufficient current through a resistor, the transistor enters saturation and conducts motor current; when base current is removed, the transistor turns off. This provides the motor with almost the full supply voltage, minus the voltage drop across the transistor and other circuit elements.[^aac-semiconductors]

If the motor is connected to the emitter and the base is driven by a signal of a given voltage, the transistor operates as an emitter follower. To turn on the base–emitter junction, the emitter must sit roughly `V_BE` below the base; the motor receives only the remaining voltage between the emitter and ground. The voltage also varies with current and transistor operating conditions, so a logic-level drive signal does not mean the motor receives full supply voltage. This does not mean emitter drive is impossible, but it is often poorly suited for the role of a simple power switch.[^aac-semiconductors]

Example: for a base driven at `3.3 V`, the emitter cannot output that same `3.3 V`; a typical base–emitter drop leaves around `2.6 V` before accounting for load and transistor characteristics. In a collector circuit, driving into saturation allows the motor to receive a voltage close to the supply rail. During turn-off, motor inductance attempts to maintain current and can generate a high-voltage spike, so a diode is placed in parallel with the motor, with cathode to the positive supply and anode to the collector.[^aac-semiconductors]

A common mistake is explaining the advantage of a collector configuration solely by "stable ground," as if the motor itself generates an uncontrollable potential. The core reason lies in the difference between a low-side switch and an emitter follower, as well as the voltage headroom required by the motor. One must also verify allowable transistor current and power dissipation, motor starting current, and protection against inductive spikes.[^aac-semiconductors]

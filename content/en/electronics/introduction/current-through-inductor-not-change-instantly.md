---
id: emb-elintro-0146
title: "Why can the current through an inductor not change instantly?"
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
  - source_id: aac-inductor-calculus
    title: "All About Circuits: Inductor Voltage and Current Relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
---

## Short answer

For an ideal inductor, `v = L*di/dt`, so a finite applied voltage changes current at a finite rate. A step in current in zero time in this model would require infinite voltage. In a real circuit, an abrupt interruption of current can produce high voltage, limited by parasitic parameters and protection circuitry.[^aac-inductor-calculus]

## Detailed explanation

An inductor stores energy in a magnetic field when current flows through its winding. If the current changes, the magnetic flux changes as well, and by the law of electromagnetic induction, a voltage appears in the winding. For a linear ideal inductor, the relationship is given by `v = L*di/dt`: for higher inductance and the same voltage, current changes more slowly.[^aac-inductor-calculus]

This does not mean that current cannot change at all. It changes gradually under the influence of voltage, and the sign of the induced voltage is determined by the direction of change and opposes it according to Lenz's law. For example, at a constant voltage of 1 V across an ideal 1 H inductor, the current changes by 1 A per second. The measured voltage depends on the choice of terminal polarity, but the magnitude of the rate of change is given by the relationship above.[^aac-inductor-calculus]

The phrase about "infinite voltage" is a conclusion of the ideal mathematical model for an instantaneous step in current, not a real voltage that a component can sustain. In a real circuit, winding resistance, parasitic capacitances, insulation, an arc, or a clamp element limit the transient process; therefore, when current is switched off, the voltage can become high, but not infinite. In a power circuit, the path for the inductor current must be designed in advance; otherwise, overvoltage can damage the switch or the insulation.[^aac-inductor-calculus]

**Common mistake:** Treating an inductor as an open circuit for any change in current. In reality, it allows current to change, but the rate depends on the applied voltage and inductance; in steady-state DC, an ideal inductor carries a constant current and has zero voltage across itself.[^aac-inductor-calculus]

---
id: emb-elintro-0141
title: "Why is breaking a circuit with an inductor dangerous?"
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
  - source_id: aac-inductor-voltage
    title: "All About Circuits, Inductor Voltage and Current Relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
---

## Short answer

When breaking a circuit, an inductor generates a voltage opposing a rapid change in current: `v = L*(di/dt)`. Its peak depends on the circuit and protection, so a value of "hundreds of volts" is not universal; a flyback diode clamps the voltage, but slows current decay.[^aac-inductor-voltage]

## Detailed explanation

When breaking a circuit, the inductor generates a voltage that attempts to maintain the current through the winding. The current in an inductor cannot change instantaneously in an ideal model: according to the relationship `v = L*(di/dt)`, a rapid decrease in current requires a large voltage with a polarity opposing this decrease. This does not mean that the inductor "produces" energy out of nowhere: prior to disconnection, energy was stored in its magnetic field.[^aac-inductor-voltage]

When switch contacts separate, the air gap has very high resistance, but the field can break down the gap via air ionization. An arc then forms, through which current decays more slowly, and the magnetic field energy converts into heat and light. Without an arc or another dissipation path, the voltage rises as far as parasitic capacitances and insulation permit; the real limit depends on the component and circuit, so it is not a fixed quantity.[^aac-inductor-voltage]

For example, in a relay circuit, turning off the coil current can create a voltage spike capable of damaging a transistor switch. A protection diode, connected in parallel with the coil and reverse-biased during normal power, provides a path for current circulation after turn-off; this limits the voltage, although it slows the decay of the coil current. For fast turn-off, other clamps are used, matched to the allowable switch voltages and the required decay time.[^aac-inductor-voltage]

**Common mistake:** Assuming that an open switch guarantees zero current and zero voltage across the coil. After opening, current initially continues to flow through an arc, a protection element, or a parasitic path; the protection plan must account for exactly where the stored energy will go.[^aac-inductor-voltage]

---
id: emb-elintro-0089
title: "Ohm's law has three forms – which one do you know by heart?"
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
  - source_id: aac-ohm
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
---

## Short answer

Ohm's law for an ohmic resistor has three algebraically equivalent forms: `V = I*R`, `I = V/R`, and `R = V/I`. They allow you to find an unknown quantity when the other two are known; for example, `5 V` across `1 kΩ` yields `5 mA`.[^aac-ohm]

## Detailed explanation

Ohm's law relates the voltage across a resistor's terminals, the current through it, and its resistance. The condition is essential: the relationship `V = I*R` describes an ohmic element under given conditions where its resistance can be considered constant. For an incandescent lamp, resistance varies with temperature, and for a diode, the current-voltage relationship is nonlinear, so you cannot unconditionally apply a single constant value of `R` to any arbitrary component.[^aac-ohm]

The three forms are obtained through ordinary algebraic manipulation of the same equation. If voltage and resistance are known, current is their quotient; if current and resistance are known, you can find voltage. Mind the units: volts divided by ohms yield amperes, and `1 kΩ` must be converted to `1000 Ω` when working in base units.[^aac-ohm]

**Worked example:** a `1 kΩ` resistor is connected to a `5 V` source. With an ideal source and constant resistance, the current is `5 V / 1000 Ω = 0.005 A = 5 mA`. If you confuse `kΩ` with `Ω`, the result will be off by a factor of one thousand. The actual current also depends on resistor tolerance and the internal resistance of the source.[^aac-ohm]

**Common mistake:** picking a formula from memory without checking units and the component model. First determine which two quantities are given, convert them to compatible units, and verify that the component actually behaves as a resistor in that operating regime.[^aac-ohm]

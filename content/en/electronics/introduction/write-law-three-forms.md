---
id: emb-elintro-0044
title: "Write Ohm's law in its three forms."
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ohmic element under constant physical conditions: `V = I*R`, `I = V/R`, `R = V/I`. In every form, the voltage and current must relate to the same element; the law is not a universal model for non-linear components.[^aac-voltage-current-resistance]

## Detailed explanation

Ohm's law relates the voltage `V` across an element, the current `I` through it, and its resistance `R`: `V = I*R`. Rearranging the terms yields two more forms: `I = V/R` and `R = V/I`. All three expressions describe the same relationship, and the choice of form depends on the unknown quantity. Ensure consistent units: volts, amperes, and ohms yield amperes or ohms, respectively, after division.[^aac-voltage-current-resistance]

An important limitation is that Ohm's law in this form applies to an ohmic element, for which the current-voltage relationship is linear under given physical conditions. For an ordinary resistor, resistance varies with temperature, so significant heating can alter the value of `R`; for a diode or an incandescent lamp, a simple constant resistance may be an unsuitable model. Voltage must be measured across that exact element and current through it, rather than taken from another part of the circuit.[^aac-voltage-current-resistance]

Example: across a `2 kΩ` resistor, `6 V` is measured. Then the current through it is `I = V/R = 6 V/2000 Ω = 0.003 A = 3 mA`. For this calculation, we assume that the resistor's resistance equals `2 kΩ` during the measurement and that it behaves ohmically. After calculating, it is useful to verify dimensions: a volt divided by an ohm equals an ampere.[^aac-voltage-current-resistance]

**Common mistake:** claiming that any two numbers from a circuit can be plugged into the formula. First establish that the voltage, current, and resistance all belong to the same element, and verify whether its behavior matches an ohmic model.[^aac-voltage-current-resistance]

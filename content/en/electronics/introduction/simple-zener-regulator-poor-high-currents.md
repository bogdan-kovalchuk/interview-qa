---
id: emb-elintro-0196
title: "Why is a simple Zener regulator poor at high currents?"
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

In such a regulator, the series resistor must pass the sum of the load current and the minimum Zener diode current. Under heavy load, it dissipates significant power, while under light load, the excess current heats the Zener diode. You must verify the circuit for both extreme operating conditions and avoid exceeding the permissible component power ratings.[^aac-semiconductors]

## Detailed explanation

A simple Zener diode regulator consists of a series resistor and a Zener diode connected in parallel with the load. The resistor limits the current and drops the difference between the input and output voltages; the Zener diode maintains approximately its breakdown voltage only when sufficient current flows through it and it is not overloaded.[^aac-semiconductors]

The current through the resistor branches between the load and the Zener diode. When the load draws more current, the Zener diode current decreases; if it falls below the required operating level, the output voltage ceases to be regulated. When the load draws little current, almost all of the resistor current flows through the Zener diode and turns into heat. Thus, the resistor must ensure the minimum Zener current at maximum load, while maintaining a power margin at minimum load.[^aac-semiconductors]

As the load current increases, dissipation in the series resistor increases, roughly proportional to the product of its voltage drop and current. The required source current also increases. For high currents, a linear pass element or a switching converter is typically more practical: a simple shunt circuit wastes energy, and its components must withstand the corresponding heat.[^aac-semiconductors]

Example: a 12 V source, a 5.1 V output, a 20 mA load, and a minimum of 5 mA for the Zener diode require at least 25 mA through the resistor. With idealized values `R = (12 V - 5.1 V)/25 mA = 276 Ω`; the standard value must be verified against tolerances and the actual minimum current of the specific Zener diode. Check the power dissipation of the resistor and Zener diode also at zero load, when the Zener diode conducts the entire resistor current.[^aac-semiconductors]

**Common mistakes:** calculating only the load current and forgetting the margin for the Zener diode; checking power dissipation only at maximum load; assuming that the Zener diode compensates for insufficient source voltage or current.[^aac-semiconductors]

---
id: emb-elintro-0045
title: "What are the three forms of the electric power formula?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-electric-power
    title: "All About Circuits: Power in Electric Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/power-electric-circuits/
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

Electric power equals `P = V*I` and is measured in watts (W). For an ohmic resistor, Ohm's law provides the equivalent forms `P = I²*R` and `P = V²/R`; the latter two specifically require the corresponding resistance.[^aac-electric-power]

## Detailed explanation

Electric power indicates the rate of energy transfer or conversion. For an element across which there is a voltage `V` and through which a current `I` flows, the power equals `P = V*I`; the unit is the watt, where `1 W = 1 J/s`. The sign depends on the chosen directions of voltage and current: a positive value under the passive sign convention means the element consumes power.[^aac-electric-power]

For a resistor that obeys Ohm's law `V = I*R`, substituting voltage or current into the original formula yields `P = I²*R` and `P = V²/R`. These expressions are convenient when other pairs of quantities are known, but they are not independent universal laws for any component: the derivation relies specifically on an ohmic relationship. In a non-linear element, voltage and current might not be related by a single constant resistance, so one must first determine its operating point or use the direct power relationship.[^aac-voltage-current-resistance]

Example: a `10 Ω` resistor carries `0.2 A`. Assuming an idealized constant resistance, the voltage drop is `2 V`, and the dissipated power is `0.4 W` using the formulas `V = I*R` and `P = I²*R`. The result agrees with `P = V*I = 2 V*0.2 A = 0.4 W`. When choosing a real resistor, one takes into account rated power and thermal conditions; the calculated value describes dissipation, rather than automatically defining the required component rating.[^aac-electric-power]

**Common mistake:** using `P = V²/R` or `P = I²*R` while substituting a voltage or current that does not belong to the same element. Verify that the quantities are defined for the resistor, and that its resistance can be assumed constant in the operating regime under consideration.[^aac-voltage-current-resistance]

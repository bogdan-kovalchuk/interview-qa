---
id: emb-elcirc-0031
title: "Why can a resistive divider not step voltage up?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-voltage-divider
    title: "All About Circuits: Voltage Divider Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/voltage-divider-circuits/
---

## Short answer

For two resistors connected across a source, the transfer ratio is `V_out = V_in*R_2/(R_1+R_2)`. Because passive resistances satisfy `R_1 >= 0` and `R_2 >= 0`, the scaling factor `R_2/(R_1+R_2)` can never exceed 1, making voltage step-up impossible. Stepping voltage above the input rail requires an active power conversion topology or energy storage element, such as a boost converter or transformer circuit.[^aac-direct-current]

## Detailed explanation

A resistive divider is a series circuit in which the output is taken across a portion of the total voltage. The same current flows through both resistors, and the voltage drop across each is proportional to its resistance; therefore, the fraction across `R_2` equals `R_2/(R_1+R_2)`. The network divides the available voltage between the elements, but it does not generate additional energy.[^aac-direct-current]

The limits are evident from extreme cases. If `R_1 = 0`, the output of an ideal unloaded circuit equals the input; if `R_2 = 0`, the output equals zero. For positive resistances between these extremes, the result lies between zero and `V_in`. This conclusion applies to a passive two-resistor divider with an ideal source. If the `V_out` node is connected to a load, it alters the lower branch, so an unloaded calculation is no longer sufficient.[^aac-direct-current]

Calculation example:

For `V_in = 9 V`, `R_1 = 10 kΩ`, and `R_2 = 20 kΩ`, the current in the unloaded circuit is `9 V/(30 kΩ) = 0.3 mA`, and the output across `R_2` is `6 V`. It is lower than the source because `R_1` accounts for the remaining `3 V`.

**Common mistakes:**

- Confusing a divider with a boost converter: increasing the lower branch resistance changes the division ratio, but it does not produce an output higher than the source.
- Applying the unloaded divider equation after connecting a load: it must then be accounted for in parallel with `R_2`.

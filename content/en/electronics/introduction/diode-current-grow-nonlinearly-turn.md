---
id: emb-elintro-0169
title: "Why does diode current grow nonlinearly after turn-on?"
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

In the forward direction, diode current increases nonlinearly: in a simplified model, it depends exponentially on voltage rather than proportionally.[^aac-semiconductors] Therefore, a small increase in voltage can significantly increase current; a resistor or driver limits it.

## Detailed explanation

Current in a forward-biased `P-N` junction depends nonlinearly on voltage. As forward bias increases, charge carriers cross the depletion region more easily, and current increases rapidly; therefore, the common phrase "a diode turns on at 0.7 V" is only a rough model rather than a switch with a sharp threshold.[^aac-semiconductors]

For an idealized junction, the relationship is described by the diode equation, which is nearly exponential. The actual `I-V` curve deviates from the simple model due to series resistance, self-heating, and specific material characteristics. The forward voltage value must be related to the specific current and temperature specified in the datasheet.[^aac-semiconductors]

This explains why an LED or rectifier diode cannot be connected directly to a voltage source without current limiting. Even if the voltage initially slightly exceeds the approximate "turn-on voltage," a further increase can cause a large surge in current and overheating. A series resistor sets the slope of the load line and stabilizes the circuit's operating point.[^aac-semiconductors] [^aac-direct-current]

A common mistake is assuming `V_f` is constant and concluding that once it is reached, current will automatically remain safe. For example, if the source has low internal resistance, a small increase in voltage can cause current exceeding the allowable limit. To avoid this, you provide current limiting, verify thermal ratings, and analyze the actual `I-V` curve rather than relying on a single forward drop value.[^aac-semiconductors]

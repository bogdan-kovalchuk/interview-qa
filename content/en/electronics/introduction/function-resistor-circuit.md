---
id: emb-elintro-0003
title: What is the function of a resistor in a circuit?
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
  - source_id: aac-resistors
    title: "All About Circuits: Resistors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
---

## Short answer

A resistor relates voltage and current through resistance: for an ideal ohmic resistor, `V = I*R`. It limits current, forms voltage dividers and dissipates electrical energy as heat, within its power rating. [^aac-resistors]

## Detailed explanation

Resistance is not a fixed voltage drop: the drop depends on current. Conversely, a fixed applied voltage produces less current when resistance increases. A resistor does not consume charge; it transfers electrical energy into heat. Use `P = V*I = I²*R = V²/R` for the ideal resistive model. [^aac-resistors]

For a calculated example, 5 V across 1 kΩ gives `I = 5/1000 = 5 mA` and `P = 25 mW`. That result is for the voltage across the resistor, not automatically the whole supply voltage if other series components are present.

For an LED with an assumed 2 V forward drop on a 5 V supply, a 220 Ω series resistor gives approximately `(5-2)/220 = 13.6 mA`; resistor dissipation is about 41 mW. This is a worked model, not a universal LED design: verify actual forward voltage, allowable LED current, resistor tolerance and rated power. Real resistance can also vary with temperature.

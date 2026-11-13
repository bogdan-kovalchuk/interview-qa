---
id: emb-elcirc-0017
title: "State Kirchhoff's voltage law (KVL)."
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
---

## Short answer

The algebraic sum of all voltages around any closed circuit loop is zero: `ΣV = 0`.[^aac-direct-current] Signs are determined by the loop traversal direction and the assigned voltage polarities, meaning the sum of voltage rises equals the sum of voltage drops.[^aac-direct-current]

## Detailed explanation

Kirchhoff's Voltage Law (KVL) states that the algebraic sum of potential changes around any complete closed loop is zero. Upon returning to the starting point, the potential has the exact same value as before the traversal; this reflects the conservation of energy for charges in a circuit.[^aac-direct-current]

The word "algebraic" is essential: each transition across an element is assigned a sign depending on whether potential rises or drops in the chosen traversal direction. A source voltage can be a rise and a resistor voltage can be a drop, but signs depend on circuit polarities and traversal direction. Reversing the traversal direction flips all signs, but leaves the equation equivalent.[^aac-direct-current]

For example, for a 12 V source with series drops of 4 V and 8 V, traversing from the source negative terminal through to positive, and then continuing through both resistors back to start gives `+12 V - 4 V - 8 V = 0`. This is the exact same balance as equating the voltage rise to the sum of drops.[^aac-direct-current]

KVL applies to any closed path, not just the simplest series circuit. In problems involving time-varying magnetic flux or distributed electromagnetic effects, a lumped-element model may be insufficient; in standard DC circuits, the assumption of ideal interconnects and lumped components is standard.[^aac-direct-current]

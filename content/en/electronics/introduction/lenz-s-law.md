---
id: emb-elintro-0138
title: "What is Lenz's law?"
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
  - source_id: openstax-inductance-energy
    title: "OpenStax College Physics 2e: 23.9 Inductance"
    url: https://openstax.org/books/college-physics-2e/pages/23-9-inductance
---

## Short answer

Lenz's law determines the direction of the induced EMF: it creates an effect that opposes the change in magnetic flux that caused it. For a coil, this means opposing an increase in current or supporting a decaying current, rather than a fixed direction of induced current.[^openstax-inductance-energy]

## Detailed explanation

Lenz's law states that the direction of the induced EMF and its associated current is such that the magnetic field of this current opposes the change in magnetic flux that caused the induction. This rule determines the direction of the system's response, rather than simply stating that the induced current is "opposite" to the external current.[^openstax-inductance-energy]

In Faraday's formula, the minus sign encodes this exact opposition. If the current in the coil increases, the magnetic flux it creates increases, and the induced EMF acts to restrain this increase. If the current decreases, the EMF reverses polarity and attempts to maintain the previous current. The direction depends on whether the flux is increasing or decreasing, as well as on how the winding orientation is defined.[^openstax-inductance-energy]

This also aligns with the law of conservation of energy. To increase the current and magnetic field, the source must perform work against the induced EMF; when the current decays, the field can deliver the stored energy back into the circuit. Therefore, an inductor does not "forbid" a change in current, but creates a voltage whose magnitude is tied to the rate of this change.[^openstax-inductance-energy]

Example: when a switch opens a circuit with a coil, the current tends to decrease. The polarity of the voltage across the coil becomes such that it supports this current; without a clamping path, the voltage can rise enough to cause a spark across the contacts. A protection diode in a corresponding DC circuit provides a path for the current to decay.

**Common mistake:** Saying that the induced current is always opposite to the cause. The correct approach is to first determine the direction of flux change, and only then apply Lenz's rule.

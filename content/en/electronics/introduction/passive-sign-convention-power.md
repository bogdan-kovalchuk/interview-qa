---
id: emb-elintro-0096
title: "What is the passive sign convention for power?"
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
  - source_id: aac-passive-power
    title: "Sinusoidal Steady-State Power Calculations"
    url: https://www.allaboutcircuits.com/technical-articles/sinusoidal-steady-state-power-calculations/
---

## Short answer

If current enters the positively marked terminal of an element, the passive sign convention defines `p = v*i`.[^aac-passive-power] A positive value means the element absorbs power, while a negative value means it delivers power to the circuit.[^aac-passive-power]

## Detailed explanation

The passive sign convention defines the sign of power through coordinated reference directions of voltage and current: the current direction is defined as positive when it enters the terminal marked with '+', and voltage is referenced from this terminal to the '-'.[^aac-passive-power]

With this convention, the instantaneous power of the element is `p = v*i`. If the result is positive, energy is entering the element at that moment; if negative, the element is returning energy to the external circuit. This rule does not dictate whether a component is physically strictly a load or strictly a source: a battery can absorb power while charging, and a capacitor or inductor periodically absorbs and delivers power.[^aac-passive-power]

The sign depends on the chosen reference directions, not on the name of the component. If the current arrow points out of the positive terminal, you must substitute a negative current value into the passive-convention definition or explicitly invert the sign in the formula. A common mistake is calling any positive `v*i` power that a source "generates": under this convention, a positive sign designates absorption. In a circuit-wide power balance, the algebraic sum of powers equals zero when all elements are accounted for.[^aac-passive-power]

Example: a source maintains `v = 5 V` across a load, and a current of `i = 0.2 A` enters its positive terminal. Then `p = 1 W`, meaning the load absorbs one watt. For a source with the same voltage but current leaving the positive terminal, the value is `p = -1 W`: the source delivers one watt.

**Common mistake:** changing voltage polarity or current direction midway through a calculation while keeping the previous sign. First mark both reference directions on the schematic, then apply them consistently in your equations.

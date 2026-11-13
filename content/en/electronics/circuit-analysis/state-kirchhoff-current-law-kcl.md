---
id: emb-elcirc-0010
title: "State Kirchhoff's current law (KCL)."
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-kcl
    title: "All About Circuits: Kirchhoff’s Current Law (KCL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-current-law-kcl/
---

## Short answer

At any circuit node, the algebraic sum of currents is zero when a consistent sign convention is applied to all connected branches.[^aac-kcl] Equivalently, the sum of currents entering the node equals the sum of currents leaving the node.

## Detailed explanation

Kirchhoff's Current Law (KCL) states that the algebraic sum of currents at any circuit node is zero. In lumped circuit theory, a node is an electrically common junction of interconnected branches. If currents directed into the node are defined as positive and currents directed away from the node are defined as negative, their algebraic sum must equal zero. The opposite sign convention may equally be chosen; the critical requirement is maintaining consistency throughout the equation.[^aac-kcl]

The physical foundation of KCL is conservation of charge: in standard lumped circuit analysis, charge does not accumulate indefinitely within an ideal geometric node. Therefore, the charge arriving per unit time must equal the charge departing over that same interval. The law does not imply that branch currents are equal; it establishes an exact balance among their signed values.[^aac-kcl]

Example: two currents of `2 mA` and `3 mA` enter a node, and a third current is also defined as entering. Using the convention that entering currents are positive yields `2 + 3 + I_3 = 0`, which gives `I_3 = -5 mA`. The negative sign indicates that the third current physically flows out of the node with a magnitude of `5 mA`. Expressed equivalently in conversational terms: `2 mA + 3 mA` enter, so `5 mA` must leave.[^aac-kcl]

In lumped circuit models, KCL serves as a fundamental analysis tool. At very high frequencies or in systems where distributed electromagnetic effects dominate, parasitic capacitive displacement currents and radiating fields must be incorporated into the circuit model; a junction cannot simply be treated as an isolated point where current discrepancies vanish.[^aac-kcl]

**Common mistakes:**

- Summing current magnitudes without accounting for reference flow directions.
- Treating a negative current result as impossible rather than indicating flow opposite to the assigned reference arrow.
- Confusing KCL at a node with the false claim that currents are equal across all branches.[^aac-kcl]

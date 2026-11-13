---
id: emb-elcirc-0012
title: "Which sign convention is used when writing KCL?"
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

When formulating KCL, currents entering a node can be defined as positive and leaving currents as negative, or vice versa. Both conventions are valid as long as one is applied consistently; a negative solved value simply indicates that the physical current flows opposite to the assumed reference arrow.[^aac-kcl]

## Detailed explanation

Kirchhoff's Current Law expresses conservation of charge at a node as an algebraic sum of currents equal to zero. To convert directions into signs, first choose a convention: for example, currents directed toward the node are positive, while those directed away from it are negative. One can also choose the opposite rule; the physical result will not change as long as conventions are not mixed within the same equation.[^aac-kcl]

The direction of an unknown current can also be assumed arbitrarily. A solution with a positive value confirms the assumed reference arrow, while a negative value shows that the actual direction is opposite. This is not an error in the equation: the sign encodes the relationship between the actual physical direction and the chosen arrow. Known currents must also receive a sign based on their arrow relative to the node, regardless of whether their magnitude was given as positive.[^aac-kcl]

**Example:**

A given current of 4 mA and an unknown current `I_x` enter a node, while 7 mA leaves. Under the "entering is positive" rule, `4 mA + I_x - 7 mA = 0`, giving `I_x = 3 mA`. The positive result confirms the assumption that `I_x` is directed toward the node. Had the arrow for `I_x` been drawn outward, the solution would be `-3 mA`, describing the exact same physical current.[^aac-kcl]

**Common mistake:**

- Reversing the sign simply because the calculated current turned out negative, and then reversing it again in the equation. Keep the equation unchanged and interpret the sign of the result relative to the initial reference arrow.[^aac-kcl]

---
id: emb-elintro-0103
title: "Why is the current the same in every element of a series circuit?"
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
  - source_id: aac-series-circuits
    title: "All About Circuits: Series Circuits and the Application of Ohm’s Law"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/simple-series-circuits/
---

## Short answer

In a series circuit, current is identical in each element because there is only one path between them for charge movement. By the law of conservation of charge, charge does not accumulate at intermediate nodes in steady-state operation, so over an equal time, an equal amount of charge passes through each element.[^aac-series-circuits]

## Detailed explanation

A series connection is one in which elements form a single continuous path without branching. Current indicates how much charge passes through a cross-section of a conductor per unit time. If more charge entered one element than exited to the next, charge would accumulate at the junction; in steady-state operation, this does not happen. Therefore, current before and after each element is identical, although voltage across the elements can differ.[^aac-series-circuits]

This is also seen from Kirchhoff's current law: at a node, the algebraic sum of currents equals zero. For a node of a series circuit entered by one element and exited by another, the entering current must equal the exiting current. Repeating this for each connection yields the same current throughout the entire circuit. The rule applies to any components connected in series, not only resistors.[^aac-series-circuits]

**Common mistakes:**
- The same current does not mean the same voltage. On resistors with different resistances, voltage drops differ according to Ohm's law.
- If there is a node in the circuit where current can split into branches, the entire circuit is no longer a single series path. Branch currents can differ, and their sum equals the current before the branch point.
- Check connections against the schematic rather than only by component placement on a breadboard: internal contacts can create parallel branches or short circuits.[^aac-series-circuits]

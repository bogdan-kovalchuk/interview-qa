---
id: emb-elcirc-0022
title: "How do you find a node's potential by walking the circuit from a known point?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-kvl
    title: "All About Circuits: Kirchhoff’s Voltage Law (KVL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-voltage-law-kvl/
  - source_id: aac-voltage-polarity
    title: "All About Circuits: Polarity of voltage drops"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/polarity-voltage-drops/
---

## Short answer

Start at a node with a known reference potential and algebraically accumulate voltage changes along a chosen path to the target node. For a resistor with current entering its labeled `+` terminal, stepping from `+` to `-` is a potential drop while the opposite is a rise; for an independent voltage source, add or subtract its fixed terminal voltage according to polarity.[^aac-kvl] [^aac-voltage-polarity]

## Detailed explanation

A node potential is the voltage of that node relative to a chosen reference node. In many circuits, the reference node is GND, which is assigned `0 V` by convention; this does not imply that ground has absolute zero potential, but merely establishes a baseline reference. The potential of any other node is found by walking from a known point to that node and algebraically summing voltage changes across elements along the path.[^aac-kvl]

The sign of each change depends on traversal direction and element polarity. Across a resistor, under the passive sign convention, current enters the terminal at higher potential; therefore, moving in the direction of current corresponds to a voltage drop, while moving against it corresponds to a rise. For a voltage source, observe the `+` and `-` markings: moving from negative to positive adds voltage, whereas moving from positive to negative subtracts it.[^aac-voltage-polarity]

For example, starting from `GND = 0 V`, passing through a `5 V` source from `-` to `+`, and then through a resistor in the direction of a `2 V` drop yields a node at `3 V`. Traversing along a closed path back to the starting point, the algebraic sum of changes must equal zero – providing a method to verify signs.[^aac-kvl]

**Common mistakes:**

- Summing the absolute values of voltages without signs, conflating voltage rises with drops.
- Believing that a node potential has meaning without specifying a reference point.
- Attributing a resistor voltage drop purely based on traversal direction without checking the current direction or defined polarity.

If unknown currents or components form an intricate network, simple inspection and path walking may not suffice: first solve the circuit equations for currents and voltages, then use them to verify the node potential.[^aac-kvl]

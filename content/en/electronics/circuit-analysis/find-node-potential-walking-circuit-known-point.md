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

TODO

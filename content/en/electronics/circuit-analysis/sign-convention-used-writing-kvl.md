---
id: emb-elcirc-0018
title: "Which sign convention is used when writing KVL?"
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

First choose a loop traversal direction and sum potential changes consistently: moving from `-` to `+` represents a voltage rise, while moving from `+` to `-` is a voltage drop.[^aac-direct-current] Under the passive sign convention, current enters a resistor at the higher-potential terminal, so traversing in the direction of assumed current corresponds to a voltage drop.[^aac-direct-current]

## Detailed explanation

To write KVL, label the voltage polarities of each element and choose an arbitrary traversal direction around the closed loop. Start at any point and, while traversing, add potential when crossing an element from lower to higher potential, and subtract it when crossing from higher to lower.[^aac-direct-current]

For a source with labeled terminals, moving from `-` to `+` represents a rise, producing a positive term; moving from `+` to `-` yields a negative term. For a resistor, the passive sign convention specifies that current enters the terminal at higher potential. Therefore, traversing in the direction of current represents a voltage drop; traversing against current represents a rise.[^aac-direct-current]

Example: a 9 V source supplies series resistors with measured drops of 3 V and 6 V. In a chosen direction through the source from negative to positive and through the resistors in the current direction, the equation is `+9 V - 3 V - 6 V = 0`. Traversing in reverse yields `-9 V + 3 V + 6 V = 0`; both formulations describe the exact same balance.[^aac-direct-current]

Reversing the traversal direction does not alter the physical solution, provided all signs are inverted consistently. Mistakes occur when applying "rise minus drop" to some elements and the reverse convention to others. Verify each sign against actual polarity on the schematic, not solely by assumed current direction if it has not yet been resolved.[^aac-direct-current]

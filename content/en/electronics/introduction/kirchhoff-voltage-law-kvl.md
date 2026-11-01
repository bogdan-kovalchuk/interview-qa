---
id: emb-elintro-0108
title: "What is Kirchhoff's voltage law (`KVL`)?"
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
  - source_id: aac-kvl
    title: "All About Circuits: Kirchhoff’s Voltage Law (KVL)"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-6/kirchhoffs-voltage-law-kvl/
---

## Short answer

Kirchhoff's voltage law states that the algebraic sum of all voltages around any closed loop is equal to zero. When summing, the sign and polarity of each voltage must be taken into account. In a simple series circuit, the source voltage equals the sum of the voltage drops across the components.[^aac-kvl]

## Detailed explanation

Kirchhoff's voltage law (KVL) describes the consistency of potential differences around any closed path in a circuit: if you start at a node, follow a loop, and return to that same node, the total change in potential must equal zero. Voltage is the potential difference between two points, so when traversing a loop, it is essential not only to list magnitudes but also to assign directions and signs: moving from negative to positive across a voltage source is a rise, while moving through a passive component in the direction of current is typically a voltage drop.[^aac-kvl]

For a source `V_s` and two series resistors, the voltage drops `V_1` and `V_2` yield the equation `V_s - V_1 - V_2 = 0`, from which `V_s = V_1 + V_2`. If the loop traversal starts at a different point or proceeds in the opposite direction, the signs change, but the equation remains equivalent. A negative result for an unknown voltage does not mean the law is violated: it means that the actual polarity is opposite to the initially assumed orientation.[^aac-kvl]

Example: a 9 V source powers series-connected resistors with measured voltage drops of 3 V and 6 V. Traversing through the source from the negative to the positive terminal, and then back through both resistors, gives `+9 V - 3 V - 6 V = 0`. KVL works in the same way for parallel branches: each individual closed path has its own algebraic sum of zero, and the branch voltage matches the source voltage. Common mistake – adding all voltmeter readings as positive; you must preserve the signs determined by probe polarity and the traversal direction.[^aac-kvl]

---
id: emb-elintro-0043
title: "Why is voltage always \"relative\"?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-voltage-current-resistance
    title: "All About Circuits: Ohm’s Law - How Voltage, Current, and Resistance Relate"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/voltage-current-resistance-relate/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

Voltage is defined between two points, not relative to an absolute zero. In a circuit, one can designate a reference point `GND` and agree by convention to define its potential as `0 V`; this is a choice of reference, not an assertion that the point possesses a universal zero potential.[^aac-voltage-current-resistance]

## Detailed explanation

Voltage is the difference in electric potential between two points, so its numerical value always depends on the chosen pair. This is analogous to height: the statement "a point is located at a height of 10 m" requires a reference level, whereas the height difference between two points can be determined without any absolute zero. Likewise, measuring voltage with a multimeter compares the potentials of its two probes.[^aac-voltage-current-resistance]

In circuit analysis, one point is often designated as the reference and labeled `GND`; its potential is written by convention as `0 V`. Following this choice, a node voltage means the difference between that node and `GND`. If the reference point is changed, individual node voltages shift by a common constant, but the voltage between any pair of nodes remains identical. Therefore, it is more accurate to say "a node has 5 V relative to `GND`" rather than "a node has an absolute 5 V."[^aac-voltage-current-resistance]

`GND` does not always signify a physical connection to earth ground. In a battery-powered device, it may merely be a common return wire and a convenient reference point; in a grounded system, the connection to protective earth depends on the specific design. The label `0 V` does not mean the absence of voltage between this node and another point, nor does it prove that the node itself is safe to touch.[^aac-voltage-current-resistance]

Example: if node A has `5 V` relative to `GND`, and node B has `2 V` relative to the same `GND`, then the voltage of A relative to B equals `3 V`. If B is chosen as the new zero, the readings become `3 V` for A and `0 V` for B, but the difference between A and B does not change. A common mistake is treating `GND` as a physical absolute zero or confusing it with a mandatory earth ground connection; always name both measurement points.[^aac-voltage-current-resistance]

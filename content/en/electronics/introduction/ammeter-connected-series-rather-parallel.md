---
id: emb-elintro-0106
title: "Why is an ammeter connected in series rather than in parallel?"
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
  - source_id: aac-ammeter-usage
    title: "All About Circuits: Intro Lab - How to Use an Ammeter to Measure Current"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-2/ammeter-usage/
---

## Short answer

An ammeter is connected in series so that the branch current also passes through the measuring instrument. Its resistance must be small to alter the circuit current minimally. Connecting an ammeter in parallel with a source creates a path with very low resistance and can cause high current, damage the instrument, or blow a fuse.[^aac-ammeter-usage]

## Detailed explanation

An ammeter measures current by passing it through an internal measurement path. Therefore, to measure current in a branch, the circuit is broken in that branch and the instrument is inserted into the break: in a series circuit, that same current passes through each element. An ideal ammeter would have zero resistance, but a real one has a small shunt, a fuse, contacts, and wire resistance. Because of this, the measurement slightly alters the circuit; in a low-resistance or sensitive circuit, this can be noticeable.[^aac-ammeter-usage]

In current measurement mode, there is low resistance between the ammeter probes. If you touch them across two points of a source in parallel, the instrument effectively creates a short path, bypassing the load. Current is then limited primarily by the resistance of the source, wires, and instrument protection rather than the normal load; overheating, damage, or a blown fuse are possible. This is not merely an incorrect schematic placement, but a different electrical regime with dangerous current.[^aac-ammeter-usage]

Before connecting, check the probe jack, mode, and allowable range of the specific multimeter. Break only the required branch, connect the instrument in series, and start from the higher range if it is selected manually. For the current of the entire circuit, place the ammeter in the shared section before or after branching; for the current of an individual branch, into the branch itself. A clamp ammeter is a separate measurement method: it is clamped around a single conductor rather than connected with probes into a break.[^aac-ammeter-usage]

Example: if 12 mA flows through a resistor in a series circuit, approximately 12 mA must also flow in a properly functioning, series-inserted ammeter. If that same instrument is mistakenly placed in parallel with the resistor, its low resistance can shunt the resistor and cause fault current. A common mistake is transferring the voltmeter connection method to ammeter mode: a voltmeter is connected in parallel because it has high input resistance, whereas an ammeter is connected in series.[^aac-ammeter-usage]

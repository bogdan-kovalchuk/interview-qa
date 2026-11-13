---
id: emb-elee-0008
title: "How do you find the common (COM) contact of an SPDT switch with a multimeter?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: fluke-continuity
    title: "Fluke: A Guide to Continuity Testing with a Multimeter"
    url: https://www.fluke.com/en-gb/learn/blog/digital-multimeters/how-to-test-for-continuity
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
---

## Short answer

De-energize and disconnect the switch from the circuit, then test continuity across each terminal pair in both toggle positions: COM is the only terminal that shows continuity alternately with each of the other two terminals. In a closed pair, the multimeter indicates low resistance or beeps, whereas an open pair reads OL or remains silent; exact readings depend on the instrument and contact condition.[^fluke-continuity]

## Detailed explanation

COM in an SPDT switch is the movable common contact: the switch connects it to one of two alternative contacts, and in the opposite position, to the other. On a fixed package, terminals can be arranged in various ways, so the package shape or middle terminal row cannot be assumed to reliably identify COM. Identify the terminal using the manufacturer diagram or by measurement.[^aratas-switch-basics]

Before testing, disconnect power and isolate the switch from parallel paths in the circuit. Continuity mode supplies its own small test current; it cannot be used to measure an energized circuit. Select continuity or resistance mode, touch the probes to two terminals, and check both mechanical toggle positions. Across a COM–throw pair, the state should transition from conductive to open or vice versa. The beeper signal merely indicates that resistance is below the threshold of that specific instrument, not necessarily exactly zero ohms.[^fluke-continuity]

For three terminals, test all three pairs in both switch positions. For a working standard SPDT switch, one terminal will show continuity to the first of the remaining two in one position and to the second in the other position; that terminal is COM. Between the two throw terminals, there is typically no direct connection. If the switch has multiple poles, an indicator, or another special circuit, the number of physical pins will be greater, and one must first review the schematic of the specific device.[^aratas-switch-basics] [^fluke-continuity]

Example: label the terminals A, B, and C. If A–B is closed in the first position and A–C in the second, A is COM, and B and C are the two throws. There is no basis to call B "NO" until the normal state and specific mechanical construction are defined: NC/NO designations depend on the unactuated state of the actuator.[^aratas-switch-basics]

**Common mistakes:** performing a continuity test on an energized board or identifying COM solely by its physical placement. De-energizing the circuit and testing all pairs in every position distinguishes actual switch contacts from paths in the surrounding circuit.[^fluke-continuity]

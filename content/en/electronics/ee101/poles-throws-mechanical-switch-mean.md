---
id: emb-elee-0004
title: "What do poles and throws of a mechanical switch mean?"
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
  - source_id: te-switch-poles-throws
    title: "TE Connectivity: Understanding Switch Pole and Switch Throw"
    url: https://www.te.com/en/products/switches/intersection/global-switch-attributes.html
---

## Short answer

A pole describes a separate circuit or common terminal of a switch, while a throw is the number of positions or terminals to which that pole can connect. For example, an SPDT switch has one pole and two selectable output terminals; the designation alone does not define momentary action or the pinout of a specific part.[^te-switch-poles-throws]

## Detailed explanation

Poles and throws define the contact configuration of a switch. A pole corresponds to the number of separate circuits or common terminals controlled by the mechanism. A throw indicates how many switched contact paths each pole can connect to. This notation clarifies basic contact topology, but it does not specify all electrical ratings of the component.[^te-switch-poles-throws]

In an SPST switch, a single pole controls one path: a typical example is opening or closing a simple circuit. In an SPDT switch, one common terminal toggles between two alternative contacts, allowing selection between two circuits. In a DPDT switch, there are two poles, each with two throws; a single actuator toggles both poles simultaneously. Therefore, "two poles" does not imply two independent user controls: they are linked by a shared mechanical actuator.[^te-switch-poles-throws]

**Designation reading example:**

If a schematic indicates `SPDT`, identify the common terminal and the two alternative switched terminals, and then use the schematic symbol to determine which contact is closed in each switch position. The label `SPDT` on its own does not specify whether there is a center-off position, whether the action is momentary or latching, or whether switching is break-before-make or make-before-break. These characteristics must be verified in the contact timing diagram and datasheet of the specific part.[^te-switch-poles-throws]

Do not confuse the number of mechanical actuator positions with the number of poles: they are distinct properties. Likewise, a pole does not always imply a separately controlled load; in a multi-pole switch, contacts generally toggle in unison. When wiring a physical switch, rely on its actual pinout rather than solely on the generic acronym.[^te-switch-poles-throws]

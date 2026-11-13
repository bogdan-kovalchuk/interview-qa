---
id: emb-elee-0005
title: "What do SPST, SPDT, DPST, and DPDT mean, and how many contacts does each have?"
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
  - source_id: aratas-switch-basics
    title: "ARATAS (formerly Omron): What is an Electrical Switch?"
    url: https://www.aratas.com/sg-en/products/basic-knowledge/switches/basics
---

## Short answer

**SPST** has one pole and one contact path, while **SPDT** has one pole with two selectable outputs. DPST and DPDT control two single-throw circuits and two changeover circuits simultaneously; typical terminal configurations have 2, 3, 4, and 6 terminals, respectively.[^aratas-switch-basics]

## Detailed explanation

The designation describes the electrical contact configuration. A pole is the number of independent circuits the switch controls with a single action; a throw is the number of contact paths to which each pole can connect. Therefore, SPST designates one pole and one path: the contact either closes the circuit or opens it. In an SPDT switch, one common contact toggles between two other contacts, so the basic model requires three terminals.[^aratas-switch-basics]

The letter D denotes two poles linked by a single actuator. A DPST switch simultaneously makes or breaks two circuits, while a DPDT switch simultaneously toggles both poles between pairs of outputs. That is why the common nominal terminal counts are 2, 3, 4, and 6. This is not a universal count of all metal pins on the package: illumination, auxiliary poles, duplicate contacts, or a separate indicator terminal can increase the total pin count.[^aratas-switch-basics]

The practical significance of the designation lies in function rather than package geometry. An SPDT switch can be used to route a single conductor between two lines; a DPDT switch acts like two synchronized SPDT switches, for example to switch both load conductors simultaneously. The designation alone does not specify which terminals are adjacent, where COM is located on the package, whether there is a center-OFF position, or what current is safe to switch. For a physical component, always consult the manufacturer contact diagram and ratings.[^aratas-switch-basics]

Example: to switch a single wire between two signals, look for an SPDT switch and identify COM and both outputs from the schematic. To switch two conductors simultaneously, a DPDT switch is needed, but the current rating of each pole must still match the load.

**Common mistake:** counting all package pins based solely on the lettering and assuming that the terminal count always strictly equals that of the basic circuit. SPST/SPDT/DPST/DPDT designate the contact configuration rather than the exact pinout or power handling capacity.[^aratas-switch-basics]

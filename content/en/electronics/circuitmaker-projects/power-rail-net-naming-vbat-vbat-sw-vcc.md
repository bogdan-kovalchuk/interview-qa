---
id: emb-elcmproj-0039
title: "Why are battery circuit power nets assigned distinct names like VBAT, VBAT_SW, and VCC?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ti-power-distribution
    title: "Texas Instruments Application Report SLVA637: PCB Layout Guidelines for Power Management"
    url: https://www.ti.com/lit/an/slva637/slva637.pdf
  - source_id: altium-design-rules
    title: "Altium Designer Documentation: Design Rules and Constraints in PCB Design"
    url: https://www.altium.com/documentation/altium-designer/design-rules
---

## Short answer

Assigning distinct net names prevents different power segments from merging accidentally into a single continuous net in the netlist. The label `VBAT` identifies raw battery terminals, `VBAT_SW` designates switched power after the power switch, and `VCC` marks the regulated output rail. This keeps power stages distinct and ensures proper layout and routing.[^udemy-electronics-course]

## Detailed explanation

TODO

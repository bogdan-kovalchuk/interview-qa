---
id: emb-elcmproj-0028
title: "How is the outer diameter of a via calculated from drill hole size and annular ring width?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: ipc-a-600
    title: "IPC-A-600: Acceptability of Printed Boards"
    url: https://www.ipc.org/
  - source_id: ipc-6012
    title: "IPC-6012: Qualification and Performance Specification for Rigid Printed Boards"
    url: https://www.ipc.org/
  - source_id: eurocircuits-pcb-guidelines
    title: "Eurocircuits: PCB Design Guidelines - Drill Hole and Annular Ring Tolerances"
    url: https://www.eurocircuits.com/pcb-design-guidelines/
  - source_id: horowitz-hill-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: circuitmaker-docs
    title: "Altium CircuitMaker Documentation: Managing Components and Libraries"
    url: https://www.altium.com/documentation/altium-circuitmaker
---

## Short answer

The outer pad diameter of a via is calculated as the sum of the finished drill hole diameter and twice the annular ring width: `D_via = d_hole + 2 * b`. The copper annular ring compensates for CNC drilling positional tolerances and board misregistration during fabrication. An adequate ring width prevents drill breakout beyond the pad metallization.[^udemy-electronics-course]

## Detailed explanation

TODO

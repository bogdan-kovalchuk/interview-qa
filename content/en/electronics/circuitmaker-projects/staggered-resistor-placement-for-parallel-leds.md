---
id: emb-elcmproj-0025
title: "Why are current-limiting resistors arranged in a staggered pattern next to an LED array?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: horowitz-hill-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: vishay-led-resistors
    title: "Vishay: Current Limiting Resistors for LEDs in Automotive and Industrial Applications"
    url: https://www.vishay.com/docs/49216/anleds.pdf
---

## Short answer

Dense spacing of an LED array leaves insufficient room to place parallel axial resistors in a single straight row. Staggering the resistors shifts their through-hole pads along the board. This prevents solder bridging between adjacent pads and opens clear corridors for routing signal traces.[^udemy-electronics-course][^ipc-2221b]

## Detailed explanation

TODO

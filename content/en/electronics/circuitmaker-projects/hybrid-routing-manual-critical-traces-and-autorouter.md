---
id: emb-elcmproj-0030
title: "How is hybrid board routing organized using manual routing and an autorouter?"
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
---

## Short answer

The engineer manually routes critical power nets, clock oscillators, and sensitive analog traces, locking them against changes. An autorouter is then run to route remaining non-critical digital lines rapidly. The process concludes with mandatory manual cleanup: removing acute trace angles, eliminating stubs and redundant vias, and optimizing clearances.[^udemy-electronics-course][^ipc-2221b]

## Detailed explanation

TODO

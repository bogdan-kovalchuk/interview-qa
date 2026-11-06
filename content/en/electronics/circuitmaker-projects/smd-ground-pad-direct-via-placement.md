---
id: emb-elcmproj-0065
title: "Why should an SMD component ground pad have its own immediately adjacent via?"
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
  - source_id: ipc-7351b
    title: "IPC-7351B: Generic Requirements for Surface Mount Design and Land Pattern Standard"
    url: https://www.ipc.org/
  - source_id: ti-scba017-pdn-design
    title: "Texas Instruments: High-Speed Layout Guidelines (Application Report SPRAAR7)"
    url: https://www.ti.com/lit/an/spraar7h/spraar7h.pdf
---

## Short answer

A long trace leading to a distant grounding point introduces distributed parasitic inductance. At high switching speeds, this causes transient inductive voltage spikes and localized ground bounce under the component. Placing a dedicated via immediately adjacent to the pad routes return currents along the shortest path directly into the ground plane.[^udemy-electronics-course][^ipc-2221b]

## Detailed explanation

TODO

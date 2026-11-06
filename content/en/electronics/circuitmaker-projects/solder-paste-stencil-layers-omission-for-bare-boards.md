---
id: emb-elcmproj-0068
title: "Why are solder paste stencil layers excluded when ordering bare unpopulated PCB fabrication?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ipc-7525b
    title: "IPC-7525B: Stencil Design Guidelines"
    url: https://www.ipc.org/
  - source_id: ucamco-gerber-specification
    title: "Ucamco: The Gerber Layer Format Specification"
    url: https://www.ucamco.com/en/gerber/specification
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
---

## Short answer

Paste mask layers are intended exclusively for laser-cutting apertures in stainless steel solder paste stencils during component assembly. During bare-board fabrication, exposed copper pads receive a protective surface finish and do not involve solder paste. Submitting unnecessary paste layers confuses CAM engineers and risks order delays or fabrication holds.[^udemy-electronics-course][^ipc-7525b]

## Detailed explanation

TODO

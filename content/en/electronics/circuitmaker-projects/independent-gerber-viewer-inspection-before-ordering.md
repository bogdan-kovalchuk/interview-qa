---
id: emb-elcmproj-0070
title: "Why must Gerber files be inspected in an independent viewer before submitting them for manufacturing?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), картки курсу"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: ucamco-gerber-spec
    title: "Ucamco: The Gerber Format Specification (Revision 2023.03)"
    url: https://www.ucamco.com/en/gerber
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
---

## Short answer

An internal EDA viewer often renders the native design database directly, masking export glitches. A standalone viewer (such as Gerbv or ViewMate) parses the exact raw vectors and aperture commands that manufacturing equipment will execute. This allows designers to catch misaligned layers, corrupted aperture definitions, or missing copper pours prior to costly board fabrication.[^udemy-electronics-course][^ucamco-gerber-spec]

## Detailed explanation

TODO

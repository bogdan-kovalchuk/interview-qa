---
id: emb-elcmproj-0071
title: "What manufacturing consequences occur if the board outline layer is missing from a Gerber export package?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: ucamco-gerber-spec
    title: "Ucamco: The Gerber Layer Format Specification (Revision 2023.03)"
    url: https://www.ucamco.com/en/gerber/downloads
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
---

## Short answer

Without an explicit board outline layer, CNC routing machines cannot determine the intended physical boundary or profile of the board. The fabrication facility either halts production pending clarification or routs the PCB using arbitrary copper pour extents. This results in mechanical enclosure fit failures and costly project delivery delays.[^udemy-electronics-course]

## Detailed explanation

TODO

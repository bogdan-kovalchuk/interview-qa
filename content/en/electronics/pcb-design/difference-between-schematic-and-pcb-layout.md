---
id: emb-elpcb-0001
title: "What is the difference between the schematic and the PCB layout in a design project?"
track: electronics
section: pcb-design
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: circuitmaker-docs
    title: "CircuitMaker documentation"
    url: https://www.altium.com/documentation/altium-circuitmaker
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose: EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://www.wiley.com/en-us/EMC+and+the+Printed+Circuit+Board%3A+Design%2C+Theory%2C+and+Layout+Made+Simple-p-9780780347038
  - source_id: ipc-2221
    title: "IPC-2221B: Generic Standard on Printed Board Design, IPC"
    url: https://www.ipc.org/ipc-2221
---

## Short answer

A schematic abstractly defines electrical connectivity: component symbols and their logical connections, without any physical geometry. A PCB layout represents the physical board: outline, component footprints, copper traces across layers, and drilled holes. In CircuitMaker, these are managed as two separate documents of one project, `.SchDoc` and `.PcbDoc`.[^montrose-emc-pcb]

## Detailed explanation

TODO

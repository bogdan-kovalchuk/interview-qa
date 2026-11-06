---
id: emb-elcmproj-0066
title: "How does flipping small SMD components to the bottom layer optimize PCB layout?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: montrose-emc-pcb
    title: "Montrose M. Printed Circuit Board Design Techniques for EMC Compliance. IEEE Press, 2000"
    url: https://ieeexplore.ieee.org/book/5264350
  - source_id: altium-layer-stack
    title: "Altium Documentation: Flipping Components and Layer Stack Management"
    url: https://www.altium.com/documentation/altium-designer/pcb-obj-componentcomponent-properties
---

## Short answer

The top layer is dedicated to bulky interface components: buttons, LEDs, speakers, and external connectors. Placing tiny SMD passives on the bottom layer allows decoupling capacitors and termination resistors to sit directly beneath IC pins. This substantially shrinks board surface area and shortens high-speed signal routing.[^montrose-emc-pcb]

## Detailed explanation

TODO

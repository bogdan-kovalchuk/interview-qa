---
id: emb-elcmproj-0045
title: "Why must copper traces and silkscreen legends maintain a clearance of at least 20–40 mil from the board edge?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: ipc-a-600
    title: "IPC-A-600: Acceptability of Printed Boards"
    url: https://www.ipc.org/
  - source_id: altium-keepout-rules
    title: "Altium Documentation: Board Edge Clearance Rule"
    url: https://www.altium.com/documentation/altium-designer/board-outline-clearance-pcb-rule
---

## Short answer

During board outline depaneling with router bits or V-scoring saws, mechanical machine tolerances apply. Placing copper too close to the board edge risks torn copper tracks, fiberglass delamination, and accidental electrical shorts to metallic chassis walls or mounting standoffs. A standard 20–40 mil keepout protects circuitry from perimeter machining damage.[^ipc-2221b]

## Detailed explanation

TODO

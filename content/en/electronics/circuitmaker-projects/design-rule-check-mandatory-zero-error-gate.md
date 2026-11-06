---
id: emb-elcmproj-0032
title: "Which critical Design Rule Check parameters must strictly equal zero before sign-off?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: altium-drc-guide
    title: "Altium Documentation: Design Rule Checking (DRC)"
    url: https://www.altium.com/documentation/altium-designer/design-rule-checking
  - source_id: ipc-a-600
    title: "IPC-A-600: Acceptability of Printed Boards"
    url: https://www.ipc.org/
---

## Short answer

The final DRC report must show zero violations for short circuits, clearance constraints, and unrouted nets. Even a single unrouted net produces an open circuit in the manufactured board. Ordering PCB fabrication is permissible only after resolving every reported DRC violation.[^ipc-2221b]

## Detailed explanation

TODO

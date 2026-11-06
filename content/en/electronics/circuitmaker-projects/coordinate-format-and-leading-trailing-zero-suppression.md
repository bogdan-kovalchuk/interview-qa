---
id: emb-elcmproj-0069
title: "What do coordinate format and zero suppression specify in Gerber and NC Drill files?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ucamco-gerber-spec
    title: "The Gerber Layer Format Specification (Revision 2023.08)"
    url: https://www.ucamco.com/files/downloads/file_en/456/gerber-layer-format-specification-revision-2023-08_en.pdf
  - source_id: ipc-nc-349
    title: "IPC-NC-349: Computer Numerical Control Formatting for Drillers and Routers"
    url: https://www.ipc.org/
  - source_id: altium-gerber-output
    title: "Altium Documentation: Gerber and NC Drill Output Options"
    url: https://www.altium.com/documentation/altium-designer/gerber-output-options
---

## Short answer

The coordinate format (such as 2:4 or 2:5 in inches) sets the number of integer and decimal digits, defining positioning resolution down to 0.1 or 0.01 mil. Leading or trailing zero suppression reduces file size by omitting non-significant zeros from coordinate strings. A mismatch in these settings between EDA export and the manufacturer CAM station causes tenfold coordinate scaling errors or severe drill-to-copper misalignment.[^ucamco-gerber-spec]

## Detailed explanation

TODO

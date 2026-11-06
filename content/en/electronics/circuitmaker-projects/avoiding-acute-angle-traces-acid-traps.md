---
id: emb-elcmproj-0031
title: "Why must acute trace angles of less than 90 degrees be strictly avoided during PCB routing?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ipc-2221
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/ipc-2221
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose: EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://ieeexplore.ieee.org/book/5265261
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

Liquid etchant accumulates in sharp, wedge-like trace corners during PCB etching and resists washing out. These acid traps cause localized over-etching of the copper, leading to microfractures or open circuits during operation. In addition, sharp bends create local characteristic impedance discontinuities and increase electromagnetic radiation at high frequencies.[^ipc-2221]

## Detailed explanation

TODO

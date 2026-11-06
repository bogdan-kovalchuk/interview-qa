---
id: emb-elpcb-0022
title: "What is the principle of orthogonal routing on a two-layer printed circuit board?"
track: electronics
section: pcb-design
sources:
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose. EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://ieeexplore.ieee.org/book/5265261
  - source_id: ipc-2221
    title: "IPC-2221: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/ipc-2221
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

Orthogonal routing places traces predominantly horizontally on one layer and vertically on the other. This prevents a long uninterrupted trace on one layer from partitioning the board and blocking cross-routing. It also minimizes mutual parallel trace length across layers, reducing capacitive crosstalk and facilitating 100% routing completion.[^montrose-emc-pcb]

## Detailed explanation

TODO

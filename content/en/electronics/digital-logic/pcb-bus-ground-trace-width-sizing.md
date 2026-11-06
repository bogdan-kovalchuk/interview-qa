---
id: emb-eldig-0038
title: "Why does a shared multi-bit bus ground trace require significantly greater width than signal lines?"
track: electronics
section: digital-logic
sources:
  - source_id: ipc-2152
    title: "IPC-2152: Standard for Determining Additional Current-Carrying Capacity in Printed Board Design"
    url: https://www.ipc.org/ipc-2152
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose. EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://ieeexplore.ieee.org/book/5265261
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

A shared ground return trace carries the simultaneous combined return current of all active bus lines. For example, if eight lines each sink `100 mA`, the ground return must conduct a total current of `800 mA`. A narrow `10 mil` trace with `0.5 oz` copper is rated for only about `0.5 A` and will overheat, so designers widen it to `25 mil` or use a continuous ground plane.[^ipc-2152]

## Detailed explanation

TODO

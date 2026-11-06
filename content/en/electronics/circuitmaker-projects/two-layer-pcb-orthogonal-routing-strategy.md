---
id: emb-elcmproj-0029
title: "What is the orthogonal routing strategy on a two-layer printed circuit board?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ipc-2221
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/ipc-2221
  - source_id: montrose-emc-pcb
    title: "Mark I. Montrose: EMC and the Printed Circuit Board: Design, Theory, and Layout Made Simple, IEEE Press / Wiley"
    url: https://ieeexplore.ieee.org/book/5265261
  - source_id: ott-emc
    title: "Henry W. Ott: Electromagnetic Compatibility Engineering, John Wiley & Sons"
    url: https://www.hottconsultants.com/emc_book.html
  - source_id: bogatin-signal-integrity
    title: "Eric Bogatin: Signal and Power Integrity - Simplified (3rd Edition), Prentice Hall"
    url: https://www.pearson.com/en-us/subject-catalog/p/signal-and-power-integrity---simplified/P200000003233
---

## Short answer

The orthogonal routing strategy dedicates one layer primarily to horizontal traces and the other layer to vertical traces. Maintaining mutual orthogonality between layers prevents routing channels from being blocked and simplifies complex interconnects. On two-layer boards, this approach must be used with caution to avoid fragmenting ground copper pours and disrupting current return paths.[^ipc-2221]

## Detailed explanation

TODO

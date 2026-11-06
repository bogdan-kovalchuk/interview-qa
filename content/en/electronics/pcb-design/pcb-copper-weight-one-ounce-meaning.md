---
id: emb-elpcb-0007
title: "What does a 1 oz copper thickness mean on a PCB?"
track: electronics
section: pcb-design
sources:
  - source_id: ipc-2152
    title: "IPC-2152: Standard for Determining Current-Carrying Capacity in Printed Board Design"
    url: https://www.ipc.org/
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: coombs-pcb-handbook
    title: "Clyde F. Coombs, Happy T. Holden. Printed Circuits Handbook (7th Edition)"
    url: https://www.accessengineeringlibrary.com/content/book/9780071833950
---

## Short answer

Copper weight represents mass per unit area: `1 oz/ft²` corresponds to a thickness of approximately `35 µm` (`1.37 mil`). This relationship is linear, so `2 oz` is roughly `70 µm`, and `0.5 oz` is `17.5 µm`. Thicker copper handles higher current and dissipates heat better, whereas thinner copper allows etching finer trace widths and tighter clearances.[^ipc-2152]

## Detailed explanation

TODO

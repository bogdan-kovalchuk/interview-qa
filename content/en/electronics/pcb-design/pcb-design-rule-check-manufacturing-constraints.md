---
id: emb-elpcb-0016
title: "What is the purpose of design rule checking (DRC) in PCB design?"
track: electronics
section: pcb-design
sources:
  - source_id: ipc-2221b
    title: "IPC-2221B: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/
  - source_id: ipc-a-600k
    title: "IPC-A-600K: Acceptability of Printed Boards"
    url: https://www.ipc.org/
  - source_id: coombs-pcb-handbook
    title: "Clyde F. Coombs, Happy T. Holden. Printed Circuits Handbook (7th Edition)"
    url: https://www.accessengineeringlibrary.com/content/book/9780071833950
---

## Short answer

DRC automatically verifies PCB topology against the manufacturing constraints of a specific fab house and the electrical requirements of the schematic. The tool checks minimum trace widths, clearances between copper elements, minimum hole sizes, annular ring widths, and solder mask bridges. This prevents short circuits, broken nets, and yield loss during board fabrication and assembly.[^ipc-2221b]

## Detailed explanation

TODO

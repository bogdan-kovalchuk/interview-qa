---
id: emb-elpcb-0025
title: "Why must component stock and lifecycle status be verified before starting PCB layout?"
track: electronics
section: pcb-design
sources:
  - source_id: ipc-2221
    title: "IPC-2221: Generic Standard on Printed Board Design"
    url: https://www.ipc.org/ipc-2221
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
---

## Short answer

Designing without checking stock leads to fabricated boards that cannot be assembled because of end-of-life (EOL) obsolescence or prohibitive lead times. Substituting a chip in a different footprint requires redesigning the board layout, updating footprints, and paying for another fabrication run. Therefore, designers verify distributor inventory beforehand, ensuring adequate stock depth and multiple second sources.[^ipc-2221]

## Detailed explanation

TODO

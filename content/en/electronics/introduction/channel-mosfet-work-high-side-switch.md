---
id: emb-elintro-0254
title: "How does a P-channel MOSFET work as a high-side switch?"
track: electronics
section: introduction
sources:
  - source_id: ti-pmos-high-side
    title: "Texas Instruments: P-channel controllers simplify high-side gate drive"
    url: https://www.ti.com/document-viewer/lit/html/SSZT975/GUID-2E43C966-E5BD-4918-9B79-18A6DD85D045
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

The source of the P-channel MOSFET connects to `+V`, and the drain connects to the load. To turn it on, the gate is pulled below the source, establishing a negative `V_GS`; to turn it off, the gate is pulled up to the source so that `V_GS` approaches zero. The maximum rated `V_GS` must never be exceeded.[^ti-pmos-high-side]

## Detailed explanation

TODO

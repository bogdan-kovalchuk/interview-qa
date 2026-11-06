---
id: emb-elintro-0255
title: "Why is a P-channel MOSFET often used for a high-side switch?"
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

A P-channel MOSFET allows switching the positive rail directly with its gate driven relative to the source near `+V`, often eliminating bootstrap or charge-pump driver circuitry. This simplifies design, though it does not make P-channel universally superior: N-channel high-side switches are commonly chosen when lower conduction losses and smaller silicon area justify a specialized gate driver.[^ti-pmos-high-side]

## Detailed explanation

TODO

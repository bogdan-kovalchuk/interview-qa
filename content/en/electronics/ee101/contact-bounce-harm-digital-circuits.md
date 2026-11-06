---
id: emb-elee-0007
title: "What is contact bounce and why does it harm digital circuits?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-switch-debounce
    title: "Texas Instruments: Debounce a Switch, SCEA094"
    url: https://www.ti.com/document-viewer/lit/html/SCEA094
---

## Short answer

During transition, mechanical switch contacts can rapidly make and break connection multiple times, creating several electrical edges instead of a single transition. A fast digital input can register these transitions as multiple events, requiring hardware or software debouncing; bounce duration depends on the specific component.[^ti-switch-debounce]

## Detailed explanation

TODO

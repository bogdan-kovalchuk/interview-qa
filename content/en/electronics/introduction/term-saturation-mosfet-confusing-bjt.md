---
id: emb-elintro-0242
title: "Why can the term `saturation` in a MOSFET be confusing after the BJT?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: toshiba-mosfet-drive
    title: "Toshiba: MOSFET Gate Drive Circuit, Application Note"
    url: https://toshiba.semicon-storage.com/info/TPH4R50ANH1_application_note_en_20180726_AKX00068.pdf?did=59460&prodName=TPH4R50ANH1
---

## Short answer

In a BJT, `saturation` means that both junctions are forward-biased and the switching transistor exhibits a low `V_CE`; it is not simply a synonym for being fully on. In a MOSFET, `saturation` means channel pinch-off near the drain and typically corresponds to the amplification region. An on-state MOSFET switch operates in the `linear/triode` region with low `R_DS(on)`.[^aac-semiconductors] [^toshiba-mosfet-drive]

## Detailed explanation

TODO

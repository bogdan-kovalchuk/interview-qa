---
id: emb-elintro-0243
title: "What is R_DS(on) and why does it matter?"
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

`R_DS(on)` is the channel resistance between drain and source of an on-state MOSFET under specified conditions, particularly `V_GS` and junction temperature. For continuous current, conduction losses are approximately `P = I²*R_DS(on)`, so lower resistance directly reduces these losses; it does not account for switching, gate drive, or other loss mechanisms.[^toshiba-mosfet-drive]

## Detailed explanation

TODO

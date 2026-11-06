---
id: emb-elintro-0244
title: "Why is a MOSFET efficient at high currents?"
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

With sufficient gate voltage, a power MOSFET can achieve a low `R_DS(on)`, resulting in small conduction losses even at substantial currents. For example, an idealized 5 A through 25 mΩ yields `P = I²*R = 0.625 W`; this figure excludes switching losses, gate driver losses, and temperature rises that increase resistance.[^toshiba-mosfet-drive]

## Detailed explanation

TODO

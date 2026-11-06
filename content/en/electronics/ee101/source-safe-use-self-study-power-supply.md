---
id: emb-elee-0177
title: "Which AC source is safe to use for self-study power supply exercises?"
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
  - source_id: hammond-catalog
    title: "Hammond Manufacturing: Transformers & Inductors catalog (Line Transformer Selection Guide; Class 2 Energy Limiting, BP series)"
    url: https://www.hammfg.com/files/literature/5c.pdf
  - source_id: busboard-bb170
    title: "BusBoard Prototype Systems: BB170 plug-in solderless breadboard (datasheet)"
    url: https://www.busboard.com/documents/datasheets/BPS-DAT-(BB170)-Datasheet.pdf
---

## Short answer

The best choice is a commercial, enclosed AC wall adapter with an isolated low-voltage AC output, manufactured and certified for this purpose.[^hammond-catalog] The exposed mains (primary) section must never be assembled on a solderless breadboard: such breadboards are rated only for tens of volts, such as 36 V and 2 A for the BusBoard BB170.[^busboard-bb170] An autotransformer is not a substitute for an isolation transformer because its output is not galvanically isolated from the mains.[^hammond-catalog]

## Detailed explanation

TODO

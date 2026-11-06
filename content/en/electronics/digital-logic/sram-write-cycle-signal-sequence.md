---
id: emb-eldig-0020
title: "What signal sequence is required for a valid write cycle in a static RAM (SRAM) chip?"
track: electronics
section: digital-logic
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-digital
    title: "All About Circuits textbook, Volume IV: Digital"
    url: https://www.allaboutcircuits.com/textbook/digital/
  - source_id: issi-is61wv5128bll
    title: "ISSI: IS61WV5128BLL 512K x 8 High-Speed Asynchronous Static RAM Datasheet"
    url: https://www.issi.com/WW/pdf/61-64WV5128BLL.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
---

## Short answer

First, a stable address is asserted onto the address bus. Next, chip enable `/CE` (`/CS`) and write enable `/WE` are asserted, and data is driven onto the bidirectional data bus. The data must remain stable for the specified setup time prior to the trailing edge of `/WE`, after which the write strobe is deasserted.[^issi-is61wv5128bll] [^floyd-digital]

## Detailed explanation

TODO

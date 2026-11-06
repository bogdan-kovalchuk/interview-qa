---
id: emb-elintro-0217
title: "`PNP` high-side switch: which signal turns it on, `HIGH` or `LOW`?"
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
---

## Short answer

A `PNP` high-side switch turns on when the base is lower than the emitter, so in a typical common-ground circuit this is often `LOW`. The junction forward voltage depends on current and device characteristics, so a fixed `0.7 V` is not an exact universal threshold; a GPIO level is suitable only when supply voltages are compatible.[^aac-semiconductors]

## Detailed explanation

TODO

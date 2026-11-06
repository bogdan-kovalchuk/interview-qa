---
id: emb-elintro-0218
title: "Why drive `I_B` 5–10 times higher than the minimum calculated value (overdrive)?"
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

Overdrive means supplying base current with a margin so that the switch reliably enters saturation at a given collector current. The "5–10 times" rule is only a rule of thumb, not a guarantee: current is determined by `V_CE(sat)` conditions in the transistor datasheet; excessive overdrive can increase turn-off time due to stored charge.[^aac-semiconductors]

## Detailed explanation

TODO

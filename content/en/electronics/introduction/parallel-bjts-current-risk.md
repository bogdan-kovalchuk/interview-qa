---
id: emb-elintro-0233
title: "How do you parallel BJTs for more current, and what is the risk?"
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
  - source_id: aac-bjt-basics
    title: "All About Circuits: Introduction to Bipolar Junction Transistors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-4/bipolar-junction-transistors-bjt/
---

## Short answer

BJTs can be connected in parallel to increase total current, but current does not necessarily split equally: parameter spread can cause one transistor to carry excessive load. Dedicated emitter ballast resistors provide local negative feedback to help balance currents; matched thermal mounting and adequate heat sinking are also required.[^aac-bjt-basics]

## Detailed explanation

TODO

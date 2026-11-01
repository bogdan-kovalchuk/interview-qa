---
id: emb-elintro-0104
title: "What is the \"trench\" in the middle of a breadboard for?"
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
  - source_id: adafruit-breadboards
    title: "Adafruit Learning System: Breadboards for Beginners"
    url: https://learn.adafruit.com/breadboards-for-beginners?view=all
---

## Short answer

The central trench separates the contact groups of the two sides of the breadboard so that the pins of a DIP IC can enter different groups and not connect to each other. In a typical board, five holes of a single row on each side are connected together, but across the trench these groups are isolated.[^adafruit-breadboards]

## Detailed explanation

The central trench separates the two contact fields of a breadboard so that the pins of a DIP package can be positioned on different sides of it without electrical contact between opposite pins. Inside a typical solderless breadboard, metal spring contacts join groups of holes: usually five holes in a transverse row on one side belong to one node, while the five opposite belong to another. The trench keeps these groups separated.[^adafruit-breadboards]

Such an arrangement makes it possible to insert a DIP IC so that the two rows of its pins end up in separate contact groups. If both sides of a row were connected, the pins opposite each other would be shorted, and the IC circuit would not operate properly. The trench also facilitates extracting the IC with a thin tool, but its primary electrical role is isolating the halves of the contact field.[^adafruit-breadboards]

**Common mistakes:**
- Do not assume that all holes on a single horizontal line are connected: the central gap divides it into left and right groups.
- Do not transfer the contact pattern of one breadboard to another without checking: mini boards and specific models can have a different pattern.
- If in doubt, test adjacent nodes with a multimeter in continuity mode.[^adafruit-breadboards]

---
id: emb-elee-0133
title: "How does a shunt regulator with a Zener diode work?"
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

A series resistor R connects `V_in` to the output, the Zener diode connects cathode to output and anode to ground, and the load sits in parallel. Current through R splits between load and Zener: `I_R = (V_in - V_Z)/R = I_load + I_Z`.[^fiore-rectification] The output stays near `V_Z` only while the Zener remains in breakdown with at least its minimum operating current; if the load takes almost all resistor current, the Zener turns off, regulation is lost, and R and the load form a simple divider.[^nexperia-an90031]

## Detailed explanation

TODO

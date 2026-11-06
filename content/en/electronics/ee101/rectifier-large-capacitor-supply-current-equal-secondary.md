---
id: emb-elee-0175
title: "Can a rectifier with a large capacitor supply a DC current equal to the secondary's rated RMS current?"
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
  - source_id: hammond-rectifier-guide
    title: "Hammond Manufacturing: Design Guide for Rectifier Use"
    url: https://www.hammfg.com/pdf/5c007.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

No. A capacitor filter forces the diodes to conduct only in short charging current pulses near the peaks, so the secondary RMS current is higher than the average DC load current.[^fiore-rectification] For a bridge rectifier with a capacitor input filter, transformer manufacturer guidelines suggest approximately `I_DC ≈ 0.62*I_RMS` of the secondary.[^hammond-rectifier-guide]

## Detailed explanation

TODO

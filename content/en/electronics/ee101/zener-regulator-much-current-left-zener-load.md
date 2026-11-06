---
id: emb-elee-0142
title: "Zener regulator 9 V / 5.1 V / 390 Ω: how much current is left for the Zener with a 10 kΩ and a 1 kΩ load?"
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
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification
---

## Short answer

With the Zener in breakdown (`V_out ≈ V_Z = 5.1 V`), resistor current is `I_R = (9 - 5.1)/390 = 10 mA`, splitting between load and Zener.[^fiore-rectification] At 10 kΩ, the load draws `5.1/10000 = 0.51 mA`, leaving ≈ 9.49 mA for the Zener. At 1 kΩ, the load takes 5.1 mA, leaving ≈ 4.9 mA. These are nominal values: for a BZX84-C5V1, `V_Z` tolerance (4.8–5.4 V at 5 mA) allows residual current at 1 kΩ to range from about 3.8 to 6.0 mA.[^nexperia-bzx84]

## Detailed explanation

TODO

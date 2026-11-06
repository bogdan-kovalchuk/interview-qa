---
id: emb-elee-0134
title: "Regulator: `V_in` = 9 V, `V_Z` ≈ 5.1 V, R = 390 Ω. What are the currents and powers?"
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

Resistor current is `I_R = (9 - 5.1)/390 = 10 mA`. With a 5 mA load, approximately 5 mA remains for the Zener. Without load, the entire current flows through the Zener: `P_Z = 5.1*0.01 ≈ 51 mW`, while the resistor dissipates `P_R = 3.9²/390 ≈ 39 mW`. These values assume nominal `V_Z = 5.1 V`: real `V_Z` has manufacturing tolerance and varies with current.[^nexperia-an90031]

## Detailed explanation

TODO

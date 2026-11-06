---
id: emb-elee-0242
title: "Why can connecting the next gate or an LED change the high output level of a transistor gate?"
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
  - source_id: ti-slaa067
    title: "TI: Understanding Basic Analog – Circuit Equations (SLAA067)"
    url: https://www.ti.com/lit/pdf/slaa067
  - source_id: fiore-bjt-switching
    title: "Fiore: Semiconductor Devices, 4.7 BJT Switching and Driver Applications (LibreTexts)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04%3A_Bipolar_Junction_Transistors_(BJTs)/4.7%3A_BJT_Switching_and_Driver_Applications
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

When current is drawn from a passive pull-up output, the HIGH level drops by `I*R` to `V_CC - I*R`.[^ti-slaa067] Because LED indicator current and downstream base drive both flow through the pull-up resistor, LED brightness alone does not verify valid logic voltage levels.

## Detailed explanation

TODO

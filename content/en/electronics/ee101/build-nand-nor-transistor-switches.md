---
id: emb-elee-0237
title: "How do you build NAND, NOR, AND and OR from transistor switches?"
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
  - source_id: montana-eele414-cmos
    title: "Montana State University EELE 414: CMOS combinational logic, module 6 lecture notes"
    url: https://www.montana.edu/aolson/eele414/lecture_notes/eele414_module_06_logic.pdf
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines
---

## Short answer

Two NPN switches in series to ground with a pull-up resistor pull the output LOW only when both inputs are HIGH, creating a NAND gate.[^montana-eele414-cmos] Connecting two switches in parallel pulls the output LOW whenever either input is HIGH, forming a NOR gate. Adding an output inverter turns NAND into AND and NOR into OR.

## Detailed explanation

TODO

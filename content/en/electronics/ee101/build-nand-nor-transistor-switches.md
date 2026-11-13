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

An output with a pull-up resistor to the supply has only two states: if the network from the output to ground conducts, the output is LOW; otherwise, the pull-up resistor pulls it HIGH. Therefore, the output equals the inversion of the conduction condition: `Y = NOT(f)`, where `f` is the condition under which the network conducts. Transistors in series yield `f = A * B`, while parallel transistors yield `f = A + B`. In CMOS notes, the same rule applies: series means AND, parallel means OR.[^montana-eele414-cmos]

Example of a two-NPN NAND gate. When `A = 0`, the upper transistor is in cutoff, the path is broken, and the output is pulled HIGH through the resistor. When `A = B = 1`, both transistors are saturated (given sufficient base drive), and the output drops to the sum of their `V_CE,sat`. If each `V_CE,sat` ≈ 0.1 V, the LOW level is ≈ 0.2 V; if each is ≈ 0.15 V (the value in Fiore's example at 10 mA), it is ≈ 0.3 V.[^fiore-bjt-dc-load-line] Consequently, the LOW voltage level increases with the number of series-connected transistors, which must be considered in logic design.

A NOR gate is built in parallel: the output drops LOW if either of the two transistors is turned on, that is, `Y = NOT(A + B)`. To obtain AND or OR, an inverter is added at the output of the NAND or NOR gate (such as a single-transistor stage with a pull-up resistor): `NOT(NOT(A * B)) = A * B` and `NOT(NOT(A + B)) = A + B`. Without such an inverter, the pull-down network produces only NAND or NOR.

**Common mistakes:**

- Confusing series and parallel connections: series yields the condition "all inputs HIGH", while parallel yields "any input HIGH".[^montana-eele414-cmos]
- Believing that a two-NPN NAND gate yields AND without an inverter: the NAND output is inverted.
- Leaving an unused input floating: a base without a defined potential causes an undefined transistor state.

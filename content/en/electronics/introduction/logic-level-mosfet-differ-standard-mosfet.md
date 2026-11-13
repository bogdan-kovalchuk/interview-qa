---
id: emb-elintro-0249
title: "How does a `logic-level MOSFET` differ from a standard MOSFET?"
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
  - source_id: infineon-logic-level-mosfet
    title: "Infineon: OptiMOS logic level MOSFETs"
    url: https://www.infineon.com/products/power/mosfet/n-channel/optimos-strongirfet/optimos-ir-mosfet-logic-level?page=2
---

## Short answer

A logic-level MOSFET is engineered to achieve its rated `R_DS(on)` at a lower gate-to-source voltage `V_GS`.[^infineon-logic-level-mosfet] Usable drive voltage and on-resistance must always be verified under specific datasheet test conditions rather than assumed from a marketing label.[^infineon-logic-level-mosfet]

## Detailed explanation

The term `logic-level` describes a device whose characteristics are tailored to the lower control voltages common in digital logic circuits and microcontrollers. Unlike a standard MOSFET where a low `R_DS(on)` is guaranteed only at higher gate voltages, a logic-level part provides a specified `R_DS(on)` at a lower `V_GS`. This does not mean that any such transistor will fully enhance from any arbitrary GPIO: always verify the specific test voltage in the electrical characteristics table.[^infineon-logic-level-mosfet]

Datasheets specify `R_DS(on)` alongside defined test conditions, particularly `V_GS`, drain current, and frequently junction temperature. This parameter enables calculating conduction losses, such as `P = I_D²*R_DS(on)`, whereas the marketing label `logic-level` on its own defines neither an exact on-resistance nor a maximum current limit. Additionally, check the absolute maximum gate-to-source voltage rating to avoid damaging the gate oxide.[^infineon-logic-level-mosfet]

The designation `standard` is not a self-contained specification and does not imply a universal `10 V` standard. While 10 V is a widespread test condition for many power MOSFETs, other parts may specify ratings for 4.5 V, 2.5 V, or other voltage levels. When evaluating candidates, use the `R_DS(on)` guaranteed at your circuit's actual gate-to-source voltage, taking into account driver drop and power supply variations.[^infineon-logic-level-mosfet]

**Common mistake:** equating a low `V_GS(th)` with logic-level drive capability. Threshold indicates only the onset of slight conduction at a small test current; achieving low on-resistance at the target operating point is an entirely separate requirement.

Example: for a `3.3 V` GPIO, look for a datasheet row with a guaranteed `R_DS(on)` at a `V_GS` equal to or below the available voltage, allowing for margin. If the table specifies resistance only at `10 V`, that component is not rated for direct 3.3 V operation without a dedicated gate driver.[^infineon-logic-level-mosfet]

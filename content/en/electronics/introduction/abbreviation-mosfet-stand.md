---
id: emb-elintro-0235
title: "What does the abbreviation `MOSFET` stand for?"
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
  - source_id: adi-mosfet-basics
    title: "Analog Devices University: Transistors, Chapter 8"
    url: https://wiki.analog.com/university/courses/electronics/text/chapter-8
---

## Short answer

`Metal-Oxide-Semiconductor Field-Effect Transistor` is a field-effect transistor with a gate separated from the semiconductor by an insulating oxide layer. Gate voltage modulates the channel between source and drain via an electric field; in steady state, an idealized insulated gate draws no DC current, though real gates exhibit capacitance and specified leakage current.[^adi-mosfet-basics]

## Detailed explanation

The abbreviation `MOSFET` stands for `Metal-Oxide-Semiconductor Field-Effect Transistor`. The name describes its construction and physical principle: the classic structure consists of a gate, an oxide-based insulating layer, and a semiconductor in which a controllable conducting channel is formed. In modern components, gate stack materials may differ from elemental metal and silicon dioxide, but the historical designation has been preserved.[^adi-mosfet-basics]

In a MOSFET, control voltage is applied between gate and source (`V_GS`). An electric field modulates carrier concentration beneath the insulator, thereby altering channel conductivity between drain and source. This explains the term "field-effect": the control terminal influences the channel through an electric field without forming a conducting junction to it in normal operation.[^adi-mosfet-basics]

In a simplified circuit model, gate current after charging device capacitances is negligible. However, the gate does not behave as an infinite impedance under all conditions: during switching transitions, the driver must deliver or remove charge, and exceeding the maximum gate-to-source voltage can permanently damage the thin insulating dielectric. For fast switching, gate charge and driver impedance are critical factors rather than the simplistic assertion that "gate current is zero."[^adi-mosfet-basics]

**Common mistake:** correctly spelling out MOSFET but concluding that it draws zero drive current under all conditions. In steady state, current is minimal, but during state transitions the gate must be charged and discharged. Also, do not confuse threshold voltage `V_GS(th)` with the gate drive voltage at which a power MOSFET is guaranteed to achieve its specified `R_DS(on)` – the latter must be checked in the datasheet for the actual operating conditions.[^adi-mosfet-basics]

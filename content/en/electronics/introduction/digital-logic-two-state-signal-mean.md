---
id: emb-elintro-0016
title: What does "digital logic is a two-state signal" mean?
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
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
---

## Short answer

Two-state digital logic interprets a signal as LOW or HIGH, conventionally representing 0 or 1 in positive logic. These states are voltage ranges defined by input thresholds, not necessarily exact 0 V and supply voltage. Intermediate voltages may have no guaranteed logical interpretation. [^ti-hc00]

## Detailed explanation

A binary state is an interpretation of the input voltage by a receiver. Real outputs may sit above ground for LOW or below the supply for HIGH, especially under load. What matters is that the output levels meet the receiving device’s specified input limits. Different logic families can have different limits. [^ti-hc00]

For the TI SN74HC00 at `V_CC = 4.5 V`, section 6.3 specifies `V_IL(max) = 1.35 V` and `V_IH(min) = 3.15 V`. Within the specified input-voltage range, a level at or below 1.35 V is accepted as LOW and at or above 3.15 V as HIGH. The interval between them is not guaranteed as either. These numbers belong to this device and supply condition. [^ti-hc00]

Thus 1 V and 4 V can encode the two states in this example without being ideal rail voltages. Logic-level compatibility requires comparing transmitter output specifications with receiver input thresholds. A supply label such as 3.3 V is not sufficient on its own.

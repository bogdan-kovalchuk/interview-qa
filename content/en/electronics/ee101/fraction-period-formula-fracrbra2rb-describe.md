---
id: emb-elee-0258
title: "Which fraction of the period does the formula R_B / (R_A + 2*R_B) describe for the 555, and can R_A be 0?"
track: electronics
section: ee101
sources:
  - source_id: ti-ne555-datasheet
    title: "Texas Instruments: NE555 Precision Timers Datasheet (SLRS022)"
    url: https://www.ti.com/lit/ds/symlink/ne555.pdf
  - source_id: fiore-555-timer
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 9.6 The 555 Timer"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09:_Specialized_Linear_Circuits/9.6:_The_555_Timer
  - source_id: aac-555-circuits
    title: "All About Circuits: 555 Timer Circuits"
    url: https://www.allaboutcircuits.com/textbook/experiments/chpt-8/555-timer-circuits/
---

## Short answer

This formula describes the LOW output fraction `t_LOW / T`, not the HIGH fraction. In a standard astable 555 circuit, the HIGH duty cycle is always strictly greater than 50%. Reducing `R_A` to zero is strictly forbidden, because during the discharge phase pin 7 is tied to ground by the internal switch, creating a direct short circuit across the power supply that destroys the IC.[^ti-ne555-datasheet]

## Detailed explanation

TODO

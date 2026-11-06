---
id: emb-eldig-0013
title: "Why are a tri-state buffer and a Hi-Z state needed in digital circuits?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: ti-74hc244-datasheet
    title: "Texas Instruments. SN74HC244 Octal Buffers and Line Drivers with 3-State Outputs"
    url: https://www.ti.com/lit/gpn/sn74hc244
---

## Short answer

Directly connecting standard push-pull outputs causes a short circuit whenever one driver asserts HIGH and another drives LOW. A tri-state buffer includes an enable input (typically active-low `/OE`), which disconnects the output into a high-impedance Hi-Z state when disabled. In the Hi-Z state, output impedance reaches megohms, allowing multiple devices to safely share a common multiplexed data bus without bus contention.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

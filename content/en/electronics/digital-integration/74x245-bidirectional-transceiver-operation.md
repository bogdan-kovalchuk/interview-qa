---
id: emb-elinteg-0039
title: "How are bus direction and state controlled in the 74x245 bidirectional transceiver?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74hc245-datasheet
    title: "Texas Instruments: SN74HC245 Octal Bus Transceivers With 3-State Outputs datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc245.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
---

## Short answer

The 74x245 contains eight back-to-back pairs of three-state buffers for bidirectional data transmission. Direction pin `DIR` sets data flow: when `DIR = 1`, data flows from port `A` to port `B`, and when `DIR = 0`, data flows from `B` to `A`. When output enable `/OE` is `HIGH`, both ports enter the high-impedance (Hi-Z) state, isolating the transceiver from the buses.[^ti-sn74hc245-datasheet]

## Detailed explanation

TODO

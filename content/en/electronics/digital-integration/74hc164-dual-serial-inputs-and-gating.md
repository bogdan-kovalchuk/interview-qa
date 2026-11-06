---
id: emb-elinteg-0029
title: "How are the serial inputs organized in the 74HC164 IC and how are they used for data gating?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-74hc164
    title: "Texas Instruments: SNx4HC164 8-Bit Parallel-Out Serial Shift Registers Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc164.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
---

## Short answer

The 74HC164 features two serial inputs, `DSA` and `DSB`, which are internally connected through a two-input `AND` gate. This allows one pin to carry serial data while the other acts as an active-high data enable or gating strobe. Holding the control pin `LOW` inhibits data entry and shifts only logic zeros into the register.[^ti-74hc164]

## Detailed explanation

TODO

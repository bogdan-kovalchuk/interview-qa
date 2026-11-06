---
id: emb-elinteg-0060
title: "How does an asynchronous cross-coupled NOR SR latch operate and why is the S = 1, R = 1 state forbidden?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: ti-sn74hc02-datasheet
    title: "Texas Instruments: SNx4HC02 Quadruple 2-Input Positive-NOR Gates Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc02.pdf
---

## Short answer

Two cross-coupled `NOR` gates store one bit through feedback: asserting `S = 1` sets `Q = 1`, asserting `R = 1` resets `Q = 0`, and `S = R = 0` retains the current state. When `S = 1` and `R = 1` are applied simultaneously, both `Q` and `~Q` are forced to `0`, violating the complementary output rule. Deasserting both inputs at once to `00` triggers a race condition, leaving the latch in an unpredictable state.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

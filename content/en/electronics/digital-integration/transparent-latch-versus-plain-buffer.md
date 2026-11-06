---
id: emb-elinteg-0038
title: "How does the 74x373 transparent latch differ from a standard 74x244 bus buffer?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-74hc373
    title: "Texas Instruments: SNx4HC373 Octal Transparent D-Type Latches With 3-State Outputs Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc373.pdf
  - source_id: ti-sn74hc244
    title: "Texas Instruments: SN74HC244 Octal Buffers and Line Drivers With 3-State Outputs Datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc244.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

The 74x244 is a purely combinational buffer that only drives input states onto its outputs with current amplification. In contrast, the 74x373 contains internal memory elements: while latch enable `LE` is `1`, outputs track inputs transparently, but when `LE` drops to `0`, the data is latched. This storage capability allows multiplexed processor buses to be freed for subsequent transfers.[^ti-74hc373]

## Detailed explanation

TODO

---
id: emb-elinteg-0041
title: "How are 74x85 comparators cascaded for wider words and how is the first stage configured?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74hc85-datasheet
    title: "Texas Instruments: SN74HC85 4-Bit Magnitude Comparators datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc85.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

To expand word width, outputs `A > B`, `A < B`, and `A = B` of the lower-order stage connect to the matching expansion inputs of the next stage. For a standalone device or the least-significant first stage, expansion input `A = B` must be tied to logic `1` (`V_CC`), while `A > B` and `A < B` are tied to `GND`. Omitting this bias yields incorrect outputs when all compared bits are equal.[^ti-sn74hc85-datasheet]

## Detailed explanation

TODO

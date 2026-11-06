---
id: emb-elinteg-0046
title: "How are 74LS83 4-bit adders cascaded for wide binary addition?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74ls83a-datasheet
    title: "Texas Instruments: SN74LS83A 4-Bit Binary Full Adders with Fast Carry datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls83a.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

Building an 8-bit adder requires two 74LS83 (or 74LS283) ICs, connecting carry-out `C4` of the lower-order stage to carry-in `C0` of the higher-order stage. Carry-in `C0` of the first stage is tied to ground (`GND`) for normal addition. The combined 8-bit sum is taken from outputs `Σ1–Σ4` of both ICs, with `C4` of the upper stage indicating carry overflow.[^ti-sn74ls83a-datasheet]

## Detailed explanation

TODO

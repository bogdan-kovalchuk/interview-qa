---
id: emb-elinteg-0004
title: "Why does the 74x138 decoder have three enable inputs of different polarities?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-74ls138-datasheet
    title: "Texas Instruments. SN74LS138, SN74S138 3-Line to 8-Line Decoders/Demultiplexers Data Sheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls138.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003296
---

## Short answer

The 74x138 features two active-low enable inputs `/G2A` and `/G2B` (or `/E1`, `/E2`) and one active-high enable input `G1` (or `E3`). The decoder outputs are enabled only when `G1 = 1`, `/G2A = 0`, and `/G2B = 0` simultaneously. This mix of polarities allows cascading multiple decoders to expand address decoding or connecting directly to memory address buses without external logic gates.[^ti-74ls138-datasheet]

## Detailed explanation

TODO

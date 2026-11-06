---
id: emb-elinteg-0040
title: "What functions does the 74x85 magnitude comparator perform and what signals does it output?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74hc85-datasheet
    title: "Texas Instruments: SN74HC85 4-Bit Magnitude Comparators datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc85.pdf
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
---

## Short answer

The 74x85 compares two 4-bit unsigned binary words, `A3–A0` and `B3–B0`. It provides three mutually exclusive active-high outputs: `A > B`, `A < B`, and `A = B`, asserting exactly one depending on the magnitude comparison result. The comparator consists of purely combinational asynchronous logic and requires no external clock.[^ti-sn74hc85-datasheet]

## Detailed explanation

TODO

---
id: emb-elinteg-0015
title: "What is a multiplexer (data selector) and how does its function differ from a decoder?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: ti-sn74hc151-datasheet
    title: "Texas Instruments: SNx4HC151 8-Line to 1-Line Data Selectors/Multiplexers Datasheet (SCLS110)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc151.pdf
---

## Short answer

A decoder activates one of multiple output lines based on an input address code. In contrast, a multiplexer has `n` data inputs, one common output, and `k = log2(n)` select lines. Depending on the binary address applied to the select lines, the multiplexer routes the logic state of exactly one chosen data input to the output.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

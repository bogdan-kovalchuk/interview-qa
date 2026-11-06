---
id: emb-elinteg-0016
title: "What Boolean equation describes the logic of a 4-to-1 digital multiplexer?"
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

The output of a 4-to-1 multiplexer is expressed as a sum of products of data inputs `D0–D3` and select lines `S1, S0`: `Y = ~S1 * ~S0 * D0 + ~S1 * S0 * D1 + S1 * ~S0 * D2 + S1 * S0 * D3`. Each select code enables exactly one three-input `AND` gate while blocking the others. The outputs of these gates are combined through a common `OR` gate to drive the output `Y`.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

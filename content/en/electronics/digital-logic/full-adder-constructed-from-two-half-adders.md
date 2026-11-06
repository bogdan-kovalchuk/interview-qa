---
id: emb-eldig-0030
title: "How is a full adder constructed from two half adders and an additional gate?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003264
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003260
---

## Short answer

The first half adder adds input bits `A` and `B`, generating an intermediate sum and a first carry. The second half adder adds this intermediate sum to the carry-in bit `C_in`, producing the final sum `S = A ^ B ^ C_in`. The carry outputs of both half adders are combined through a two-input `OR` gate to form the overall carry-out `C_out = C_1 | C_2`.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

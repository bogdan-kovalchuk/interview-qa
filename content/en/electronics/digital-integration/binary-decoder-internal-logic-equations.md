---
id: emb-elinteg-0003
title: "How does a 2-to-4 binary decoder work and what logic equations describe its outputs?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003296
  - source_id: ti-74hc139-datasheet
    title: "Texas Instruments. SN74HC139 Dual 2-Line to 4-Line Decoders/Demultiplexers Data Sheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc139.pdf
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
---

## Short answer

A binary decoder converts an `n`-bit input code into an active signal on one of `2^n` outputs. For two address inputs `A1` and `A0`, the four active-high output minterms are `Y_0 = /A1 * /A0`, `Y_1 = /A1 * A0`, `Y_2 = A1 * /A0`, and `Y_3 = A1 * A0`. Exactly one output is asserted at any time, uniquely identifying the applied binary input value.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

---
id: emb-elinteg-0005
title: "How can an arbitrary logic function be implemented using a 74x138 decoder and a single NAND gate?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003296
  - source_id: ti-74ls138-datasheet
    title: "Texas Instruments. SN74LS138, SN74S138 3-Line to 8-Line Decoders/Demultiplexers Data Sheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls138.pdf
---

## Short answer

The outputs of the 74x138 represent active-low minterms of the input variables. By De Morgan's laws, a `NAND` gate fed by active-low inputs is logically equivalent to an `OR` gate operating on active-high minterms. Implementing any Boolean function therefore requires only routing the corresponding decoder outputs into the inputs of a single multi-input `NAND` gate.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

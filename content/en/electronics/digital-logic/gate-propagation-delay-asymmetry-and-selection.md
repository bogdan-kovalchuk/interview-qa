---
id: emb-eldig-0009
title: "Why do gate delays t_PLH and t_PHL differ and how does this affect logic selection?"
track: electronics
section: digital-logic
sources:
  - source_id: ti-74ls-logic-databook
    title: "Texas Instruments. The TTL Data Book for Design Engineers"
    url: https://www.ti.com/lit/gpn/sn74ls08
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
  - source_id: harris-digital-design
    title: "Sarah L. Harris, David Money Harris. Digital Design and Computer Architecture, ARM Edition"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture-arm-edition/harris/978-0-12-800056-4
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
---

## Short answer

Low-to-high (`t_PLH`) and high-to-low (`t_PHL`) transitions are governed by different internal pull-up and pull-down transistor paths with unequal drive strengths and parasitic capacitances. In the 74LS series, a 74LS32 (OR) gate typically exhibits lower or comparable propagation delay relative to a 74LS08 (AND). When a critical timing path fails its timing budget, transforming logic equations to use faster gate types optimizes total circuit speed.[^ti-74ls-logic-databook]

## Detailed explanation

TODO

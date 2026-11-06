---
id: emb-eldig-0011
title: "How is the fanout of a TTL IC output calculated?"
track: electronics
section: digital-logic
sources:
  - source_id: ti-74ls-logic-databook
    title: "Texas Instruments. The TTL Data Book for Design Engineers"
    url: https://www.ti.com/lit/gpn/sn74ls04
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
---

## Short answer

Fanout is calculated separately for HIGH as `|I_OH| / I_IH` and for LOW as `I_OL / |I_IL|`. The overall fanout is the lesser of the two resulting values. For a 74LS04 inverter under standard datasheet currents, this calculation yields a fanout of 20 for both logic states.[^ti-74ls-logic-databook]

## Detailed explanation

TODO

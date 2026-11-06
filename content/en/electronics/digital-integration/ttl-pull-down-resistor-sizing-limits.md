---
id: emb-elinteg-0043
title: "Why does a 10 kΩ pull-down resistor fail to provide a logic low on 74LS inputs?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-74ls-logic-databook
    title: "Texas Instruments: The TTL Data Book for Design Engineers"
    url: https://www.ti.com/lit/gpn/sn74ls04
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
---

## Short answer

Bipolar TTL inputs (including the 74LS family) source current when pulled low, delivering an input current `I_IL` of up to `0.4 mA`. Flowing through a `10 kΩ` pull-down resistor, this current develops a voltage drop of `0.4 mA * 10 kΩ = 4.0 V`, which acts as a logic high instead of low. To ensure `V_IL <= 0.4–0.8 V`, pull-down resistance must not exceed `470–1000 Ω` for 74LS (and `250 Ω` for standard TTL).[^ti-74ls-logic-databook]

## Detailed explanation

TODO

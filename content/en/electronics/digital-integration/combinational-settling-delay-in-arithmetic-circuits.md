---
id: emb-elinteg-0042
title: "Why must system clock frequency be limited to account for combinational comparator delay?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003254
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: ti-74hc-logic-family
    title: "Texas Instruments: High-Speed CMOS Logic Data Book"
    url: https://www.ti.com/lit/ug/scla011/scla011.pdf
---

## Short answer

A magnitude comparator is a combinational circuit whose outputs stabilize only after transitions ripple through multiple internal gate levels. Propagation delay `t_pd` for 74HC devices is approximately `15–25 ns` per IC and accumulates further when stages are cascaded. If clock frequency is too high and results are latched before settling completes, registers capture transient glitches or enter metastability.[^floyd-digital]

## Detailed explanation

TODO

---
id: emb-eldig-0012
title: "Why is CMOS fanout limited by capacitance rather than DC current?"
track: electronics
section: digital-logic
sources:
  - source_id: sedra-smith-microelectronic-circuits
    title: "Adel S. Sedra, Kenneth C. Smith. Microelectronic Circuits, 7th Edition"
    url: https://global.oup.com/ushe/product/microelectronic-circuits-9780199339143
  - source_id: ti-74hc-logic-family
    title: "Texas Instruments. High-Speed CMOS Logic Data Book"
    url: https://www.ti.com/lit/ug/scla011/scla011.pdf
  - source_id: harris-digital-design
    title: "Sarah L. Harris, David Money Harris. Digital Design and Computer Architecture, ARM Edition"
    url: https://www.elsevier.com/books/digital-design-and-computer-architecture-arm-edition/harris/978-0-12-800056-4
---

## Short answer

CMOS transistor inputs have extremely high input impedance and negligible static leakage currents. However, each driven input introduces a parasitic capacitance `C_I ≈ 1–10 pF` that loads the driver output. Maximum fanout is governed by `C_L / C_I`; exceeding the rated load capacitance `C_L` degrades transition rise/fall times and violates circuit timing specifications.[^ti-74hc-logic-family]

## Detailed explanation

TODO

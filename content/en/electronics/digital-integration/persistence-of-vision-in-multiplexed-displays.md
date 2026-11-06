---
id: emb-elinteg-0033
title: "How is persistence of vision leveraged in dynamic display multiplexing and scanning?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
---

## Short answer

The human eye cannot distinguish discrete light pulses when flash rates exceed approximately `30–50 Hz`, integrating them into a continuous visual perception. In multiplexed LED displays, individual digits or rows are activated sequentially at high speed. This technique substantially reduces the number of driver pins and routing traces required to control multi-digit panels.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

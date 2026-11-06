---
id: emb-elinteg-0055
title: "Why does simultaneous pressing of two push buttons in an OR-gate encoder necessitate a priority encoder?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74hc148-datasheet
    title: "Texas Instruments: SN74HC148 8-Line to 3-Line Priority Encoders datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc148.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition. Pearson, 2017"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003303
---

## Short answer

`OR` gates perform bitwise logical addition of input signals. If a user presses two buttons simultaneously, the circuit generates a merged bitwise code, causing an unintended operation. To resolve this contention, a priority encoder (such as the 74x148) is used; it selects only the highest-priority input and ignores lower-priority active inputs.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

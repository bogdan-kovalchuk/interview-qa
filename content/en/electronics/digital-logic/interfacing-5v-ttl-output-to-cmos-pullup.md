---
id: emb-eldig-0033
title: "Why does interfacing a 5 V TTL output to a 5 V CMOS input require a pull-up resistor?"
track: electronics
section: digital-logic
sources:
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: ti-scba004
    title: "Texas Instruments Application Report SCBA004: Implications of Slow or Floating CMOS Inputs"
    url: https://www.ti.com/lit/an/scba004d/scba004d.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

A standard TTL output guarantees a high level of only `V_OH >= 2.4 V`, whereas a 5 V CMOS input requires at least `V_IH = 3.5 V` (`0.7 * V_CC`). Without level shifting, the TTL voltage falls into the CMOS indeterminate region, causing shoot-through supply currents and logic faults. A `1–10 kΩ` pull-up resistor to `+5 V` pulls the TTL output up to the full supply rail `V_CC`.[^ti-sdya009]

## Detailed explanation

TODO

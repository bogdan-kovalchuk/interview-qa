---
id: emb-eldig-0032
title: "Why can a 5 V CMOS output directly drive a 5 V TTL input?"
track: electronics
section: digital-logic
sources:
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003264
---

## Short answer

A 5 V CMOS output (such as 74HC) provides `V_OH >= 4.4 V`, which comfortably exceeds the input threshold `V_IH = 2.0 V` of a TTL IC (74LS). The output low level `V_OL <= 0.33 V` is also well below the TTL input threshold `V_IL = 0.8 V`. With excellent noise margins, the connection operates directly as long as the CMOS output can sink the low-level current `I_IL` sourced by the TTL input stage.[^ti-sdya009]

## Detailed explanation

TODO

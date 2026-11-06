---
id: emb-eldig-0031
title: "Which two voltage level conditions are required for direct logic family compatibility?"
track: electronics
section: digital-logic
sources:
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003264
---

## Short answer

To transmit a logic `1`, the minimum output high voltage of the driver must exceed the input high threshold of the receiver: `V_OH >= V_IH`. For logic `0`, the maximum output low voltage of the driver must remain below the input low threshold of the receiver: `V_OL <= V_IL`. In addition to voltage levels, the driver must supply the required load current in both states without violating voltage limits.[^horowitz-art-of-electronics]

## Detailed explanation

TODO

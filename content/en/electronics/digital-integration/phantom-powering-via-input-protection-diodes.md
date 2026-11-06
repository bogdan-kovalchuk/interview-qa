---
id: emb-elinteg-0032
title: "What is phantom powering via input ESD protection diodes and why is it hazardous?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-slyt527
    title: "Texas Instruments SLYT527: Input and output characteristics of digital logic devices"
    url: https://www.ti.com/lit/an/slyt527/slyt527.pdf
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
---

## Short answer

Digital IC inputs contain internal ESD protection diodes with cathodes tied to the `V_CC` rail. Driving an input pin while the device power rail is off conducts current through the upper clamping diode onto `V_CC`, partially powering the circuit. This unintended state can trap logic in undefined configurations, prevent proper power-on reset, and exceed diode current limits, causing damage.[^ti-slyt527]

## Detailed explanation

TODO

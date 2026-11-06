---
id: emb-elinteg-0031
title: "Why must a shift register output and a manual data button not be combined by direct electrical wiring?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
---

## Short answer

Wiring two push-pull outputs directly together creates a short circuit whenever one driver outputs logic `1` (`V_CC`) while the other drives logic `0` (`GND`). The resulting bus contention draws excessive currents, degrades logic levels, and risks thermal damage to the IC. Safely combining feedback signals or manual inputs requires a gating logic element such as an `OR` gate.[^ti-sdya009]

## Detailed explanation

TODO

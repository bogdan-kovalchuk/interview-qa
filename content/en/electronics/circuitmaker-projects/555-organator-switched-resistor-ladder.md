---
id: emb-elcmproj-0036
title: "How does switching resistor values in a 555 astable circuit generate a musical keyboard scale?"
track: electronics
section: circuitmaker-projects
sources:
  - source_id: ti-lm555-datasheet
    title: "Texas Instruments: LM555 Timer Datasheet"
    url: https://www.ti.com/lit/ds/symlink/lm555.pdf
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill. The Art of Electronics, 3rd Edition, Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-electronic-devices
    title: "Thomas L. Floyd: Electronic Devices (Conventional Current Version), 10th Edition. Pearson, 2017"
    url: https://www.pearson.com/en-us/subject-catalog/p/electronic-devices-conventional-current-version/P200000003290
---

## Short answer

In a 555 timer astable circuit, oscillation frequency depends inversely on timing resistance: `f ≈ 1.44 / ((R_A + 2 * R_B) * C)`. Each key button connects a dedicated precision resistor or resistor ladder tap, altering the charge and discharge RC time constant. Pressing multiple keys simultaneously in parallel topologies lowers the net timing resistance, raising the output audio pitch.[^ti-lm555-datasheet]

## Detailed explanation

TODO

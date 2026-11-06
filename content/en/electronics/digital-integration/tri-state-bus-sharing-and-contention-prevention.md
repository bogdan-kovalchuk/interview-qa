---
id: emb-elinteg-0036
title: "What is the high-impedance state (Hi-Z) and why is bus contention a hazardous condition?"
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

In the high-impedance (Hi-Z) state, both output transistors are turned off, presenting an open circuit that electrically disconnects the pin from the bus line. Bus contention occurs when two or more drivers simultaneously drive conflicting logic levels onto a shared line. This condition creates large shoot-through currents, drops supply rails, and can permanently damage the drivers through thermal breakdown.[^ti-sdya009]

## Detailed explanation

TODO

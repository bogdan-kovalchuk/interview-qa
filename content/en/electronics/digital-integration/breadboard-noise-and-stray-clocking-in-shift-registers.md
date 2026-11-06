---
id: emb-elinteg-0034
title: "Why do spurious triggers and unwanted extra bits occur in shift registers on solderless breadboards?"
track: electronics
section: digital-integration
sources:
  - source_id: horowitz-art-of-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: ti-sdya009
    title: "Texas Instruments Application Report SDYA009C: Designing With Logic"
    url: https://www.ti.com/lit/an/sdya009c/sdya009c.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
---

## Short answer

Solderless breadboards and long jumper wires introduce significant parasitic capacitance (up to `2–5 pF` per tie point) and lead inductance. Fast switching edges from LED loads induce voltage spikes across supply and ground rails that couple into high-impedance clock inputs. The shift register interprets these transient glitches as extra clock pulses, shifting in erroneous bits.[^horowitz-art-of-electronics]

## Detailed explanation

TODO

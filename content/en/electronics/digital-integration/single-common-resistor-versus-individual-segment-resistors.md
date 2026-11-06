---
id: emb-elinteg-0012
title: "Why should seven-segment display current not be limited with a single common anode resistor?"
track: electronics
section: digital-integration
sources:
  - source_id: horowitz-hill-art-electronics
    title: "Paul Horowitz, Winfield Hill: The Art of Electronics (3rd Edition), Cambridge University Press"
    url: https://artofelectronics.net/
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: ti-sn74ls47-datasheet
    title: "Texas Instruments: SN5446A, '47A, '48, SN54LS47, 'LS48, SN7446A, '47A, SN74LS47, 'LS48 BCD-to-Seven-Segment Decoders/Drivers Datasheet (SDLS111)"
    url: https://www.ti.com/lit/ds/symlink/sn74ls47.pdf
---

## Short answer

A single common-anode resistor forces all illuminated segments to share the total available current. When displaying the digit `1`, current divides between two segments, but displaying `8` splits that same current among seven segments, making the `8` noticeably dim. Proper circuit design requires a dedicated current-limiting resistor for each individual segment.[^horowitz-hill-art-electronics]

## Detailed explanation

TODO

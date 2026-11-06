---
id: emb-elinteg-0052
title: "Which basic operations and status flags are supported by the simplified 4-bit 74F382 ALU?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74f382-datasheet
    title: "Texas Instruments: SN74F382 4-Bit Arithmetic Logic Unit datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74f382.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
  - source_id: mano-logic-computer-design
    title: "M. Morris Mano, Charles R. Kime: Logic and Computer Design Fundamentals, 4th Edition. Pearson, 2008"
    url: https://www.pearson.com/en-us/subject-catalog/p/logic-and-computer-design-fundamentals/P200000003308
---

## Short answer

The 74F382 IC features three select inputs `S2–S0` that encode eight operations: clear (`0`), subtraction `B - A`, subtraction `A - B`, addition `A + B`, bitwise `XOR`, `OR`, `AND`, and preset all ones. In addition to the `F3–F0` result outputs, the device generates carry-out `Cn+4` and two's complement arithmetic overflow `OVR` flags.[^ti-sn74f382-datasheet]

## Detailed explanation

TODO

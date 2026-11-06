---
id: emb-elinteg-0049
title: "How are logic and arithmetic functions selected in the 74x181 ALU?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74ls181-datasheet
    title: "Texas Instruments: SN54LS181, SN54S181, SN74LS181, SN74S181 Arithmetic Logic Units/Function Generators datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls181.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
  - source_id: mano-logic-computer-design
    title: "M. Morris Mano, Charles R. Kime: Logic and Computer Design Fundamentals, 4th Edition. Pearson, 2008"
    url: https://www.pearson.com/en-us/subject-catalog/p/logic-and-computer-design-fundamentals/P200000003308
---

## Short answer

Operating mode in the 74x181 is determined by mode control input `M`: when `M = 1` (`HIGH`), the ALU performs one of 16 bitwise logic functions with internal carry disabled. When `M = 0` (`LOW`), the device executes one of 16 arithmetic operations with full carry propagation. The specific operation within the selected mode is defined by a 4-bit code on select inputs `S3–S0`.[^ti-sn74ls181-datasheet]

## Detailed explanation

TODO

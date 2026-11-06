---
id: emb-elinteg-0057
title: "How is a negative subtraction result interpreted and why is it distorted on a decimal display in a 4-bit ALU?"
track: electronics
section: digital-integration
sources:
  - source_id: ti-sn74ls47-datasheet
    title: "Texas Instruments: SN54LS47, SN74LS47 BCD-to-Seven-Segment Decoders/Drivers datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls47.pdf
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications, 12th Edition. Pearson, 2017"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003303
---

## Short answer

When subtracting a larger number from a smaller one, the result is produced in 4-bit two's complement (for example, `5 - 9 = -4` is encoded as `1100`). An unsigned BCD decoder like the 7447 interprets `1100` as decimal `12`. Because the 7447 does not support negative signs or hexadecimal glyphs, it renders a distorted non-standard pattern on the seven-segment display.[^ti-sn74ls47-datasheet]

## Detailed explanation

TODO

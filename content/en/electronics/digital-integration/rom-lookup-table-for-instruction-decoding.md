---
id: emb-elinteg-0054
title: "How is a ROM or EEPROM chip used as a lookup table (LUT) for ALU control?"
track: electronics
section: digital-integration
sources:
  - source_id: patterson-hennessy-cod
    title: "David A. Patterson, John L. Hennessy: Computer Organization and Design: The Hardware/Software Interface, 5th Edition. Morgan Kaufmann, 2014"
    url: https://www.elsevier.com/books/computer-organization-and-design/patterson/978-0-12-407726-3
  - source_id: mano-logic-computer-design
    title: "M. Morris Mano, Charles R. Kime: Logic and Computer Design Fundamentals, 4th Edition. Pearson, 2008"
    url: https://www.pearson.com/en-us/subject-catalog/p/logic-and-computer-design-fundamentals/P200000003308
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
---

## Short answer

Instead of building a complex combinational encoder from discrete gates, push buttons or an instruction bus are wired to the address lines of a ROM or flash memory IC. Predefined binary ALU operation codes are stored at memory addresses corresponding to single-bit inputs (such as 1, 2, 4, 8, and 16). The memory functions as a flexible lookup table (LUT), allowing control logic remapping without rewiring discrete gates.[^patterson-hennessy-cod]

## Detailed explanation

TODO

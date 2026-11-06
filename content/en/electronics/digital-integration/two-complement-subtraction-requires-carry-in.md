---
id: emb-elinteg-0056
title: "Why does two's complement subtraction in an ALU require an active carry-in?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals, 11th Edition. Pearson, 2015"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003294
  - source_id: mano-logic-computer-design
    title: "M. Morris Mano, Charles R. Kime: Logic and Computer Design Fundamentals, 4th Edition. Pearson, 2008"
    url: https://www.pearson.com/en-us/subject-catalog/p/logic-and-computer-design-fundamentals/P200000003308
  - source_id: patterson-hennessy-cod
    title: "David A. Patterson, John L. Hennessy: Computer Organization and Design: The Hardware/Software Interface, 5th Edition. Morgan Kaufmann, 2014"
    url: https://www.elsevier.com/books/computer-organization-and-design/patterson/978-0-12-407726-3
---

## Short answer

Hardware subtraction is implemented via two's complement addition: `B - A = B + NOT(A) + 1`. Inverting the operand as `NOT(A)` produces only the one's complement. Converting it into a true two's complement requires adding one via carry-in `Cn = 1`, otherwise the resulting difference is off by one.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

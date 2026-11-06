---
id: emb-elinteg-0068
title: "What are the ordering rules for Karnaugh maps and how does cell grouping simplify Boolean functions?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss: Digital Systems: Principles and Applications (12th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti: Digital Design: With an Introduction to the Verilog HDL, 5th Edition. Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design-with-an-introduction-to-the-verilog-hdl/P200000003296
---

## Short answer

Rows and columns of a Karnaugh map are ordered using Gray code (`00, 01, 11, 10`) so adjacent cells differ by exactly one bit. Adjacent ones are grouped into rectangular blocks of `2^k` cells (such as 1, 2, 4, 8, or 16), wrapping around map edges. When grouping cells, any variable that appears as both `0` and `1` across the group is eliminated from the resulting product term.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

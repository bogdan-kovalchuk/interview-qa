---
id: emb-eldig-0008
title: "What is the difference between sum of products (SOP) and product of sums (POS) forms in logic circuits?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003297
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti. Digital Design: With an Introduction to the Verilog HDL, 5th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design-with-an-introduction-to-the-verilog-hdl/P200000003296
---

## Short answer

Sum of Products (SOP) is an OR expression over multiple AND product terms, analogous to `if ((a && b) || (c && d))`. Product of Sums (POS) is an AND expression over multiple OR sum terms. Converting between SOP and POS using De Morgan's laws allows logic implementation with available gate types and minimizes silicon or board area.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

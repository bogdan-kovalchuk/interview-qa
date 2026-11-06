---
id: emb-elinteg-0002
title: "What is a minterm in Boolean algebra and how are logic functions synthesized from minterms?"
track: electronics
section: digital-integration
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd. Digital Fundamentals, 11th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003295
  - source_id: tocci-digital-systems
    title: "Ronald J. Tocci, Neal S. Widmer, Gregory L. Moss. Digital Systems: Principles and Applications, 12th Edition"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-systems-principles-and-applications/P200000003296
---

## Short answer

A minterm is a Boolean product (`AND`) of all circuit variables, where each variable appears once in either its complemented or uncomplemented form. Each minterm evaluates to logic `1` for exactly one specific combination of input values. Any Boolean function can be uniquely expressed as a canonical sum of products (`OR` across minterms) corresponding to the truth table rows that yield `1`.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

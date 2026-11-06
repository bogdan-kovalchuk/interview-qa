---
id: emb-eldig-0004
title: "Why are the complement identities X·/X = 0 and X + /X = 1 important for logic optimization?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti: Digital Design (6th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design/P200000003292
  - source_id: aac-boolean-rules
    title: "All About Circuits textbook, Volume IV: Digital, Chapter 7: Boolean Rules for Simplification"
    url: https://www.allaboutcircuits.com/textbook/digital/chpt-7/boolean-rules-for-simplification/
---

## Short answer

A Boolean variable and its complement always take mutually opposite truth values of 0 and 1. Because a logical AND with 0 is always 0, the conjunction yields `X * /X = 0`. Because a logical OR with 1 is always 1, the disjunction yields `X + /X = 1`. These complement identities form the cornerstone of Boolean logic minimization, allowing redundant terms and logic gates to be eliminated.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

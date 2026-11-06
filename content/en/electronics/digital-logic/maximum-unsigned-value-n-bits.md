---
id: emb-eldig-0003
title: "What is the maximum unsigned value that can be represented with n bits, and how many states does it encode?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003290
  - source_id: mano-digital-design
    title: "M. Morris Mano, Michael D. Ciletti: Digital Design (6th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-design/P200000003292
  - source_id: aac-binary-arithmetic
    title: "All About Circuits textbook, Volume IV: Digital, Chapter 1: Binary Arithmetic"
    url: https://www.allaboutcircuits.com/textbook/digital/chpt-1/binary-arithmetic/
---

## Short answer

A group of n bits represents exactly `2^n` unique states or combinations. Because unsigned binary counting begins at zero, the maximum representable value is `2^n - 1`. For instance, 8 bits encode 256 states spanning values from 0 to 255 inclusive (`0xFF` in hexadecimal).[^floyd-digital-fundamentals]

## Detailed explanation

TODO

---
id: emb-eldig-0027
title: "How is a negative number formed in two's complement, and what is the 8-bit value range?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003264
  - source_id: aac-binary-arithmetic
    title: "All About Circuits: Binary Arithmetic – Two's Complement"
    url: https://www.allaboutcircuits.com/textbook/digital/chpt-2/binary-arithmetic/
---

## Short answer

To form a negative number in two's complement, invert all bits of the positive number and add 1 to the result. For `n` bits, the representable value range spans `-2^(n-1)` to `2^(n-1) - 1`. In an 8-bit system, this covers -128 to +127, where a 1 in the most significant bit (MSB) indicates a negative sign.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

---
id: emb-eldig-0028
title: "Why does two's complement allow subtraction to be implemented purely through addition?"
track: electronics
section: digital-logic
sources:
  - source_id: floyd-digital-fundamentals
    title: "Thomas L. Floyd: Digital Fundamentals (11th Edition), Pearson"
    url: https://www.pearson.com/en-us/subject-catalog/p/digital-fundamentals/P200000003264
  - source_id: aac-subtraction-twos-complement
    title: "All About Circuits: Two's Complement Subtraction"
    url: https://www.allaboutcircuits.com/textbook/digital/chpt-2/binary-arithmetic/
---

## Short answer

Subtracting `A - B` is mathematically equivalent to adding the negation `A + (-B)`. Because the negative value is formed as `~B + 1`, the processor executes subtraction using the exact same hardware adder circuit. Any carry-out generated beyond the register bit width during two's complement subtraction is simply discarded.[^floyd-digital-fundamentals]

## Detailed explanation

TODO

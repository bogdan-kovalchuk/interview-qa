---
id: emb-elee-0026
title: "Why does a series connection of 10 µF and 1 µF give about 0.91 µF rather than about 11 µF?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-capacitors-series-parallel
    title: "All About Circuits textbook: Series and Parallel Capacitors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-13/series-and-parallel-capacitors/
---

## Short answer

In a series circuit, reciprocal capacitances sum together, so for 10 µF and 1 µF, `C_total = 10*1/(10+1) ≈ 0.91 µF` rather than 11 µF. Capacitances add directly in parallel connections; a series equivalent is always smaller than the smallest individual capacitance.[^aac-capacitors-series-parallel]

## Detailed explanation

A series connection of 10 µF and 1 µF has an equivalent capacitance of approximately 0.91 µF rather than 11 µF.[^aac-capacitors-series-parallel]

The mistake typically arises from applying the rule for parallel capacitors to a series string. In a parallel configuration, both elements share the same voltage, and their charges add together, so the capacitances add. In a series configuration, identical charge passes through each element, and the total voltage equals the sum of the voltage drops. Because `V = Q/C`, the smaller capacitor accounts for the larger portion of the voltage, so the entire string has a smaller capacitance than any of its individual capacitors.[^aac-capacitors-series-parallel]

For two capacitors, the product of their capacitances is divided by their sum. Substituting yields `10*1/(10+1) = 10/11`, or about 0.91 µF. The result is smaller than 1 µF – the smallest capacitance in the pair – which serves as a useful sanity check. Rounding to two significant figures is sufficient for this example; the actual nominal rating and measured value also depend on component tolerances.[^aac-capacitors-series-parallel]

**Common mistake:** seeing two values and immediately adding them together. First determine the topology: two shared nodes indicate a parallel connection, while a single shared intermediate node in a string indicates a series connection. Then check the bound: the series result cannot exceed the smallest capacitor.[^aac-capacitors-series-parallel] The confusion often manifests as an implausible 11 µF in a series-string problem; a quick boundary check before writing down the answer helps avoid it.

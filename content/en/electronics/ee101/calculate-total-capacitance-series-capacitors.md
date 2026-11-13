---
id: emb-elee-0025
title: "How do you calculate the total capacitance of series capacitors?"
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

For a series connection, reciprocal capacitances sum together: `1/C_total = 1/C_1 + 1/C_2 + ...`; for two capacitors, this simplifies to `C_total = C_1*C_2/(C_1+C_2)`. For example, 10 µF and 22 µF yield `220/32 = 6.875 µF`, or approximately 6.88 µF. For `n` identical capacitors, the total equals the capacitance of one divided by `n`.[^aac-capacitors-series-parallel]

## Detailed explanation

The equivalent capacitance of a series string is determined by the sum of the reciprocal capacitances of its capacitors.[^aac-capacitors-series-parallel]

In a series circuit, an identical magnitude of charge flows through all elements. For each capacitor, the relation `Q = C*V` holds, so for equal charge, a smaller capacitance requires a higher voltage. If the entire string is replaced by a single equivalent element, that same charge must produce the same total voltage; hence the rule of summing reciprocal capacitances. This does not mean that voltages across individual real capacitors always divide stably according to their nominal ratings alone: in prolonged operation, tolerance, leakage, and external balancing play a role.[^aac-capacitors-series-parallel]

For two elements, the formula can be rearranged into the product divided by the sum. This is convenient for manual calculation, but the units must match: if both values are given in µF, the result will also be in µF. The series equivalent is always smaller than the smallest individual capacitance; in a parallel connection, by contrast, capacitances add directly.[^aac-capacitors-series-parallel]

Calculation example:

```text
C_total = 1 / (1/10 + 1/22) µF
C_total = (10*22)/(10+22) µF
C_total = 220/32 µF = 6.875 µF ≈ 6.88 µF
```

**Common mistake:** mechanically adding values together as if for a parallel connection. Verifying the result is straightforward: the answer must be smaller than 10 µF; otherwise, the configuration or formula was mistaken.

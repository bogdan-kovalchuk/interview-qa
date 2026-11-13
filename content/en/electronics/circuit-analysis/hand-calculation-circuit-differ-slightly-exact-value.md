---
id: emb-elcirc-0023
title: "Why does a hand calculation of a circuit differ slightly from the exact value?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: vishay-resistor-tolerance
    title: "Vishay: Resistors – General Information"
    url: https://www.vishay.com/docs/49873/49873_sg2113.pdf
---

## Short answer

Discrepancies between manual calculations and exact solver outputs typically arise from rounding intermediate values, such as rounding `92.307... Ω` to `92.3 Ω`. This arithmetic rounding must not be confused with physical component tolerance, which specifies manufacturing variance and does not justify computational errors.[^aac-direct-current] [^vishay-resistor-tolerance]

## Detailed explanation

A slight difference between manual calculations and calculator results typically arises because one result retains more digits than the other. When an intermediate value is rounded and reused in subsequent operations, rounding error can accumulate; it is best to maintain sufficient significant figures throughout intermediate steps and round only the final answer according to the precision of the input data.[^aac-direct-current]

For example, two parallel resistors of `1.2 kΩ` and `100 Ω` yield approximately `92.3077 Ω`. Writing `92.3 Ω` differs only due to display precision and represents correct rounding to tenths of an ohm. However, if a manual result differs by several percent, verify the formula, units, and input values rather than assuming the discrepancy is automatically acceptable.

The precision of a mathematical model and the actual resistance of a physical component are distinct matters. Resistor tolerance indicates the permissible deviation of its actual resistance from nominal value; the specific value depends on the component. Temperature coefficient, self-heating, and aging can also alter resistance, so physical measurements of a real circuit may not match calculations based on nominal ratings.[^vishay-resistor-tolerance]

**Common mistakes:**

- Rounding each step to a single digit and carrying that error into subsequent operations.
- Confusing computational rounding with physical component tolerance.
- Assuming that all resistors have a tolerance of `±5–10%`; verify the datasheet specification for the specific chosen component.[^vishay-resistor-tolerance]

During manual verification, keep intermediate values with multiple significant digits and round only the final result. The number of digits in an answer does not create physical accuracy: if input nominals have only two significant figures, an excessively long decimal result creates a false impression of precision.

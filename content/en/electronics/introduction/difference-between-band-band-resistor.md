---
id: emb-elintro-0127
title: "What is the difference between a 4-band and a 5-band resistor?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: vishay-resistor-color-code
    title: "Vishay: Color Code and Standard Resistance Series"
    url: https://www.vishay.com/doc/?20143=
---

## Short answer

In a four-band code, the first two bands specify digits, the third is the multiplier, and the fourth is the tolerance; in a five-band code, the first three specify digits, while the fourth and fifth are the multiplier and tolerance.[^vishay-resistor-color-code] The five-band format adds a significant digit, but the number of bands alone does not guarantee precision: tolerance is read from the last band and the component documentation.[^vishay-resistor-color-code]

## Detailed explanation

The number of bands determines how many digits are used for the nominal value and where the multiplier and tolerance are located. In a typical four-band code, the first two bands are significant digits, the third is the multiplier, and the fourth is the tolerance. In a five-band code, there are three significant digits: the fourth band is the multiplier, and the fifth is the tolerance.[^vishay-resistor-color-code]

The extra digit allows writing the nominal value with more significant figures. However, you should not determine tolerance solely from the number of bands. In the manufacturer's chart, gold corresponds to ±5%, silver to ±10%, and other colors have different values; check the specific combination against the appropriate marking scheme and component documentation.[^vishay-resistor-color-code]

For example, in a five-band code, brown, red, and violet bands can represent the digits 1, 2, and 7; the next sets the multiplier, and the last is the tolerance. For four bands, brown, red, orange, gold means `12*1000 Ω` with a ±5% tolerance. This explains the role of the positions, but a real component must be read by its actual colors.[^vishay-resistor-color-code]

**Common mistakes:**

- Assuming that all five-band resistors have a tolerance of ±1% or better.
- Applying the sequence for four bands to a five-band component.
- Mistaking the fourth band of a five-band resistor for the tolerance when it is the multiplier.[^vishay-resistor-color-code]

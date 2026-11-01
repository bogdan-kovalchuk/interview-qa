---
id: emb-elintro-0126
title: "What resistance does a resistor with brown, red, orange, and gold bands have?"
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

B1 and B2 set digits 1 and 2, B3 sets multiplier ×1000, and gold B4 sets the tolerance of ±5%.[^vishay-resistor-color-code] The nominal value is `12*1000 = 12 000 Ω`, that is, 12 kΩ. With this tolerance, the actual resistance can be from 11.4 kΩ to 12.6 kΩ.[^vishay-resistor-color-code]

## Detailed explanation

This is a four-band marking: the first two bands encode significant digits, the third is the multiplier power, and the fourth, typically spaced from the others, sets tolerance. In the code table, brown corresponds to 1, red to 2, orange to the multiplier `10^3`, and gold to the tolerance ±5%.[^vishay-resistor-color-code]

Thus, the first two bands form the number 12, after which the multiplier gives `12*1000 = 12 000 Ω`. The gold tolerance denotes a five percent deviation from the nominal value, rather than an additional digit. The limits for this nominal value are 11 400 Ω and 12 600 Ω; the calculation shows a range rather than guaranteeing that the measured value will be exactly in the middle.[^vishay-resistor-color-code]

Worked example:

```text
12 000 Ω * 0.05 = 600 Ω
12 000 Ω - 600 Ω = 11 400 Ω
12 000 Ω + 600 Ω = 12 600 Ω
```

When reading, start from the side where the first bands are grouped closer together; the tolerance band is often separated by a gap. If the direction or color is difficult to distinguish, verify the resistance with a multimeter on a de-energized circuit, preferably isolating one lead: parallel components can affect the reading. Measurement verifies the component under specific conditions, whereas the color code specifies nominal value and tolerance.[^vishay-resistor-color-code]

**Common mistakes:**

- Reading the bands in reverse order and getting a different nominal value.
- Treating the gold band as a digit, even though here it designates tolerance.
- Assuming that any given sample is exactly 12 kΩ and interpreting a value within tolerance as a defect.[^vishay-resistor-color-code]

---
id: emb-elintro-0125
title: "What is the formula for reading a 4-band resistor?"
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
---

## Short answer

For a 4-band resistor, the first two bands set digits, the third sets the multiplier, and the fourth sets the tolerance. A gold band as a multiplier means `×0.1`, and as the fourth band typically means a tolerance of `±5%`; its role is determined by position and reading direction.[^aac-direct-current]

## Detailed explanation

In the standard 4-band code, the first and second bands are significant digits of resistance, the third is the multiplier, and the fourth is the tolerance. Thus, the nominal value is calculated as a two-digit number multiplied by the power of ten determined by the third band.[^aac-direct-current]

A gold band has two possible values depending on position: in the third position it is a multiplier `×0.1`, while in the fourth it typically designates a tolerance of `±5%`. The fourth band is often spaced further from the others, which helps determine reading direction, but for questionable markings it is advisable to verify by measurement.[^aac-direct-current]

Example: red, violet, yellow, gold bands give digits 2 and 7, multiplier `10^4`, and tolerance `±5%`. Therefore, `R = 27*10^4 Ω = 270 kΩ ±5%`. The actual resistance within tolerance may differ from the nominal value; ohmmeter measurement also depends on meter accuracy and whether the resistor is isolated from parallel paths in the circuit.[^aac-direct-current]

**Common mistake:** reading the bands from the tolerance side or always interpreting gold as tolerance. First find the spaced band, then apply the color value according to its position.[^aac-direct-current]

Band values come from the color code table; the same color has a different function depending on the band number. For example, a red first band means digit 2, but a red third band specifies multiplier `10^2`. This is positional coding rather than four digits of a number. Make sure the component is indeed four-band: in a 5-band code, the first three rings are significant digits, so applying the 4-band rule will give an erroneous result.[^aac-direct-current]

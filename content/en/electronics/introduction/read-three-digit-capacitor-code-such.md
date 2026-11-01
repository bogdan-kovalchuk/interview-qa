---
id: emb-elintro-0133
title: "How do you read a three-digit capacitor code such as `104`?"
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
  - source_id: kemet-capacitor-picofarad-code
    title: "KEMET, Ceramic Molded/Axial & Radial – MIL-PRF-20 datasheet"
    url: https://content.kemet.com/datasheets/F3101_MIL-PRF-20.pdf
---

## Short answer

In the common three-digit code, the first two digits specify the significant figures in picofarads, and the third is the number of zeros following them. Therefore, `104` means `10*10^4 pF` = `100000 pF` = `100 nF` = `0.1 µF`.[^kemet-capacitor-picofarad-code]

## Detailed explanation

The three-digit code is an abbreviated representation of nominal capacitance, typically in picofarads. The first two positions form a number, and the third specifies the power of ten by which this number is multiplied. For example, in `104`, the significant digits are `10`, and the suffix `4` means four zeros: yielding `100000 pF`.[^kemet-capacitor-picofarad-code]

To convert to a more convenient unit, remember that `1000 pF = 1 nF`, and `1000 nF = 1 µF`. Therefore, `100000 pF` equals `100 nF`, or `0.1 µF`. This is the nominal capacitance, not the tolerance, voltage rating, or date of manufacture; other adjacent characters on the package may encode separate parameters.[^kemet-capacitor-picofarad-code]

For such a code, the digit `9` has a special meaning: it specifies division by ten, not nine zeros. That is why decoding must be tied to a specific marking system rather than treating any group of three characters as this format. In manufacturer tables, verify the code and nominal value against the part series.[^kemet-capacitor-picofarad-code]

Example for `472`: the significant part is `47`, the third digit specifies two zeros, so you obtain `4700 pF`, or `4.7 nF`. The reverse check is straightforward: the expressions in pF and nF must differ by a factor of one thousand.

**Common mistake:** reading `104` as `10 nF`, forgetting that the code counts in pF. You should also not infer the voltage rating from this code – it is marked separately or found from the full component part number in the datasheet.[^kemet-capacitor-picofarad-code]

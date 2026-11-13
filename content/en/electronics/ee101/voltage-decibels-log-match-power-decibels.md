---
id: emb-elee-0098
title: "When do voltage decibels (20 log) match power decibels?"
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
  - source_id: rs-decibel-guide
    title: "Rohde & Schwarz: Radar and electronic warfare eGuide"
    url: https://www.allaboutcircuits.com/uploads/articles/Radar-and-electronic-warfare_eGuide-REVISED.pdf
---

## Short answer

The voltage formula `20*log10(|V_out/V_in|)` gives the same value as the power ratio formula only when both voltages appear across equal resistances. If the resistances differ, calculate the powers separately and compare them using `10*log10(P_out/P_in)`.[^rs-decibel-guide]

## Detailed explanation

The voltage formula `20*log10(|V_out/V_in|)` is equivalent to the power formula `10*log10(P_out/P_in)` only when both measurements are taken across equal resistances. The reason stems from the relationship `P = V^2/R`: when `R` is identical, it cancels out in the power ratio, and the squared voltage ratio pulls a factor of 2 outside the logarithm. This is how the multiplier 20 arises instead of 10.[^rs-decibel-guide]

If the resistances differ, the same voltages produce different powers. For instance, doubling the voltage across a resistance four times larger yields a power ratio of `2^2/4 = 1`, or 0 dB, even though the voltage ratio itself is 2 (which the voltage formula would evaluate as approximately 6.02 dB). This is not a contradiction: the numbers describe different ratios. For complex AC loads, real power depends on the real part of the impedance and phase angles, so comparing voltage magnitudes alone may be insufficient.[^rs-decibel-guide]

**How to avoid the mistake:** First determine what needs to be compared – voltage or power. For voltages, use RMS values and the multiplier 20 only when the resistances are identical. For differing loads, calculate the power in each of them and use the multiplier 10. Do not apply the formula for equal resistances to an arbitrary amplifier or measurement signal chain without verifying the conditions.[^rs-decibel-guide]

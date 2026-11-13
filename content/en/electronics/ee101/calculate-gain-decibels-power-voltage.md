---
id: emb-elee-0097
title: "How do you calculate gain in decibels for power and for voltage?"
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

Power gain in decibels is calculated as `G_P = 10*log10(P_out/P_in)` dB. For voltage, `G_V = 20*log10(|V_out/V_in|)` applies only when input and output impedances are equal; otherwise, actual powers must be computed. A positive value indicates gain, a negative value indicates attenuation, and 0 dB represents a 1:1 ratio.[^rs-decibel-guide]

## Detailed explanation

The decibel is a logarithmic representation of the ratio between two quantities, not an independent unit of absolute power. For power, the output is compared to the input: `G_P = 10*log10(P_out/P_in)`. When voltages are known, the ratio can be expressed in dB as `G_V = 20*log10(|V_out/V_in|)`, provided both measurements correspond to the exact same resistance. This follows from `P = V^2/R`: with equal values of `R`, the squared voltage ratio becomes the power ratio, turning the multiplier 10 in front of the logarithm into 20.[^rs-decibel-guide]

Voltage magnitudes can be compared using this formula if both are RMS voltages for AC signals and the resistances are identical. For differing resistances, an identical voltage ratio does not represent an identical power ratio. In that case, first calculate the actual power at each port based on its load, and then apply the formula for `P_out/P_in`. Example: doubling the voltage across the same resistor increases power fourfold, yielding approximately `10*log10(4) ≈ 6.02 dB`, rather than 3 dB.[^rs-decibel-guide]

Signs are interpreted relative to the numerator: a positive value indicates that the output quantity exceeds the input quantity under the chosen definition; a negative value indicates that it is smaller. Zero dB indicates equality of the quantities. The inverse calculation for voltage yields `|V_out/V_in| = 10^(G_V/20)`, and for power, `P_out/P_in = 10^(G_P/10)`. Thus, 20 dB corresponds to a tenfold voltage ratio, but a hundredfold power ratio across equal impedances.[^rs-decibel-guide]

**Example:** An input of `0.2 V RMS` and an output of `0.4 V RMS` across equal resistive loads form a 2:1 voltage ratio, giving `G_V = 20*log10(2) ≈ 6.02 dB`. If the resistances differ, this figure does not automatically represent the power gain.

**Common mistakes:**

- Using `10*log10` for voltage ratios without converting to power.
- Using `20*log10` for voltages without verifying that the resistances are equal.
- Referring to dB as an absolute level without specifying a reference quantity.[^rs-decibel-guide]

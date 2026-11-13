---
id: emb-elee-0106
title: "How does the cutoff frequency of an RC low-pass filter change if 100 nF is replaced with 1 µF at R = 1 kΩ?"
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
  - source_id: aac-rc-low-pass-cutoff
    title: "All About Circuits: Introduction to Analog Filters"
    url: https://www.allaboutcircuits.com/TEXTBOOK/designing-analog-chips/filters/introduction-to-analog-filters/
---

## Short answer

For an unchanged effective R, the cutoff frequency drops tenfold, from approximately 1.59 kHz to 159 Hz, because `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-cutoff] This represents an ideal calculation without additional loading.

## Detailed explanation

The cutoff frequency of a single-pole RC low-pass filter is the frequency at which the output amplitude is approximately 0.707 of the input amplitude, or 3 dB below the passband level. For an ideal unloaded stage, it is calculated as `f_c = 1/(2*pi*R*C)`.[^aac-rc-low-pass-cutoff]

If R remains constant, a tenfold increase in C increases the product `R*C` tenfold, so the cutoff frequency decreases by a factor of ten. This does not mean that the filter simply "becomes slower" in every sense: the shape of the normalized first-order response does not change, but the entire frequency scale shifts downward.

For the given `R = 1 kΩ` and `C = 100 nF`, we obtain approximately `1591.5 Hz`; for `C = 1 µF`, it is approximately `159.2 Hz`. These values are rounded rather than exact frequencies for real components with tolerances. It is assumed that the resistor has precisely the specified nominal value, the capacitor has its nominal capacitance, and the source and load resistances do not alter the effective R.

**Common mistakes:**
- Multiplying the frequency by ten along with the capacitance, even though frequency is inversely proportional to `C`.
- Applying the formula to a loaded circuit without checking the effective resistance seen by the capacitor.

If a subsequent stage with finite input resistance is connected to the output, or if the generator has noticeable output resistance, one must first find the equivalent resistance network. Otherwise, a simple calculation using only the nominal component values may fail to predict the measured cutoff frequency.

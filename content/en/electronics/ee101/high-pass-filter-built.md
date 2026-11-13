---
id: emb-elee-0118
title: "How is an RL high-pass filter built?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-high-pass-filters
    title: "All About Circuits: High-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/high-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

A resistor is connected in series with the source, the inductor is placed from the output node to common ground, and the output is taken across the inductor. At DC, the impedance of an ideal inductor is zero, but as frequency rises, its impedance increases so that the output approaches the input.[^aac-high-pass-filters]

## Detailed explanation

An RL high-pass filter can be built from a resistor connected in series with the source and an inductor connected from the output node to common ground; the output is taken from the node, meaning across the inductor. At low frequencies, the impedance of L is small, so the inductor shunts the signal to common ground. At high frequencies, its impedance is larger, so the output approaches the input voltage.[^aac-high-pass-filters]

If the load is solely the input of the next stage and its effect can be neglected, the ideal transfer function is `H(jω) = jωL/(R + jωL)`. The magnitude increases from zero at DC to unity at high frequencies; at the frequency `f_c = R/(2π*L)`, it equals approximately 0.707 of the high-frequency level. A real load in parallel with the inductor changes the equivalent resistance and the response, so the formula with a single R is not universal for every connection.[^aac-high-pass-filters]

Example: if `R = 1 kΩ` and `L = 2.2 mH`, then `f_c ≈ 72.3 kHz`. Below cutoff, the amplitude increases approximately in proportion to frequency, and well above cutoff, the output approaches the input. Do not confuse this circuit with an RL low-pass filter: there the inductor is in series in the signal path, and the output is taken across the resistor. In a real inductor, winding resistance and parasitic parameters alter the low-frequency transfer ratio and the upper limit of the useful frequency range.[^aac-high-pass-filters]

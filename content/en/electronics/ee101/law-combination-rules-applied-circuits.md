---
id: emb-elee-0059
title: "How are Ohm's law and the combination rules applied in AC circuits?"
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
  - source_id: aac-ac-series-parallel-laws
    title: "All About Circuits: Series-parallel R, L, and C"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-5/series-parallel-r-l-and-c/
---

## Short answer

In sinusoidal steady state at a common frequency, Ohm's law for phasors takes the form `V = I*Z`, where `V`, `I`, and `Z` are complex quantities. Series impedances add as `Z_total = ΣZ`, while parallel impedances combine as `1/Z_total = Σ(1/Z)`. All calculations are carried out in complex form to preserve phase information.[^aac-ac-series-parallel-laws]

## Detailed explanation

The rules of AC circuit analysis preserve their familiar structure when voltages and currents are expressed as phasors and each component is replaced by its impedance at the relevant frequency. Ohm's law is then written as `V = I*Z`, and Kirchhoff's laws are applied to complex quantities. This approach holds for linear circuits in sinusoidal steady state where all quantities share the same frequency.[^aac-ac-series-parallel-laws]

For a series connection, current is common and impedances add via complex addition. For a parallel connection, voltage is common and branch currents add; the equivalent impedance can be found using the reciprocal sum of impedances. These relationships resemble the rules for resistors, but the numbers contain real and imaginary parts, so phase angles cannot be discarded during calculation.[^aac-ac-series-parallel-laws]

Example: suppose a source has the phasor `V = 10∠0° V`, and two series components have `Z_1 = 3 + j*4 Ω` and `Z_2 = 2 - j*1 Ω`. Then `Z_total = 5 + j*3 Ω`, and `I = V/Z_total`. For division, it is convenient to convert to polar form: `|Z_total| ≈ 5.83 Ω`, `∠Z_total ≈ 31.0°`, whence `I ≈ 1.72∠-31.0° A`. Simply adding the magnitudes would produce a different, incorrect result because the reactive parts partially cancel.[^aac-ac-series-parallel-laws]

After calculating, it is useful to check consistency: the sum of voltage drops in a series loop must equal the source voltage, and the sum of parallel branch currents must equal the current entering the node. If the result has an unexpected angle, check the chosen phasor reference direction, the sign of capacitive reactance, and the degree or radian mode of the calculator. For a signal containing multiple frequencies, the analysis is repeated separately for each frequency component.[^aac-ac-series-parallel-laws]

**Common mistakes:**

- Combining impedances by their magnitudes as if they were ordinary resistances.
- Mixing phasors of different frequencies in a single simplified reduction.
- Applying series formulas to parallel topologies or vice versa.[^aac-ac-series-parallel-laws]

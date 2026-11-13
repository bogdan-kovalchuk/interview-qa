---
id: emb-elee-0116
title: "Why is RC chosen more often than RL for simple low-frequency filters?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-low-pass-filters
    title: "All About Circuits: Low-pass Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
---

## Short answer

For an ideal RL low-pass filter with a 1 kHz cutoff and R = 1 kΩ, an inductance of L ≈ 159 mH is required. In many low-power signal circuits, an RC filter is simpler and more compact because an inductor of that value can have large physical dimensions, high cost, and significant winding resistance. This is a practical preference rather than a strict ban on RL filters: inductors are advantageous when low series resistance and high current capability are essential.[^aac-low-pass-filters]

## Detailed explanation

For an ideal RL low-pass filter, `f_c = R/(2π*L)`, so for a fixed resistance and desired cutoff frequency, the required inductance increases inversely with frequency. At low frequencies, this can require an inductor with a large number of turns or a larger core. Copper wire has resistance, the core exhibits losses, and stray magnetic fields can couple the inductor to neighboring nodes; these effects introduce dissipation and complicate predicting circuit behavior. For many simple signal filters, a resistor and capacitor are therefore cheaper and more compact.[^aac-low-pass-filters]

Calculation example:

```text
f_c = 1000 Hz
R = 1000 Ω
L = R/(2π*f_c) = 1000/(2π*1000) ≈ 0.159 H = 159 mH
```

This does not mean that RL is always inferior. In a power supply or power stage, series resistance causes undesirable voltage drop and heating, so a choke can be preferable to a resistive element. The choice depends on current, allowable losses, size, cost, frequency range, and source requirements; one must also account for load resistance, which affects the actual cutoff. A convenient rule of thumb for initial selection: RC for an inexpensive low-power filter, and RL when inductance is already needed or when adding series resistance is unacceptable. The final decision is verified against expected nominal values and loading.[^aac-low-pass-filters]

---
id: emb-elee-0115
title: "What is the transfer function and cutoff frequency of an RL low-pass filter?"
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

For a series RL low-pass filter with output across R, the transfer function is `H(jω) = R/(R + jωL)`, the cutoff frequency is `f_c = R/(2π*L)`, and the time constant is `τ = L/R`. For R = 1 kΩ and L = 330 µH, we obtain `f_c ≈ 482 kHz`. With R kept constant, doubling L cuts the cutoff frequency in half.[^aac-low-pass-filters]

## Detailed explanation

An RL low-pass filter is formed by a series inductance and load resistance, with the output voltage measured across the resistance. The inductor impedance `jωL` increases with frequency, so at low frequencies most of the input voltage drops across R, and at high frequencies across L. This is a voltage divider with complex impedances, so the result also depends on where the output is taken.[^aac-low-pass-filters]

For an ideal source and unloaded output, the magnitude of the transfer function is `|H| = R/sqrt(R² + (2π*f*L)²)`. At the cutoff frequency, the reactance of L equals R, and the output is `1/sqrt(2)` of the low-frequency level, or approximately 70.7 %. The angular cutoff frequency is `ω_c = R/L`; dividing by `2π` converts it from radians per second to hertz. The time constant `τ = L/R` describes the transient response of that same RL circuit, and `f_c = 1/(2π*τ)`.[^aac-low-pass-filters]

Calculation example:

```text
R = 1000 Ω
L = 330 µH = 0.000330 H
f_c = R/(2π*L) = 1000/(2π*0.000330) ≈ 482 kHz
```

This value assumes no additional loading and no winding losses. In a real circuit, winding resistance, the input of the next stage, and parasitic parameters alter the transfer function and the cutoff frequency; therefore, the nominal formula should be applied to the equivalent circuit, not merely to the inductor's label. A common mistake is considering `f_c` a property of L alone: it depends on both the effective R and L. If R remains unchanged, doubling L cuts `f_c` in half.[^aac-low-pass-filters]

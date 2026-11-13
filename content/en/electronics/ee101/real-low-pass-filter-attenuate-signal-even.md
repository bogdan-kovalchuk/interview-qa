---
id: emb-elee-0117
title: "Why does a real RL low-pass filter attenuate the signal even at DC?"
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

Winding resistance `r_L` in series with R reduces the transfer ratio even at DC: `H(0) = R/(R + r_L)`. For R = 100 Ω and `r_L` = 20 Ω, this ratio is `100/120 ≈ 0.833`. In this model, the pole is located at `f_p = (R + r_L)/(2π*L)`, and the 3 dB cutoff frequency is defined relative to the actual low-frequency plateau.[^aac-low-pass-filters]

## Detailed explanation

A real RL low-pass filter with output taken across resistor R has an inductor winding resistance `r_L` connected in series with its inductance and the load. At DC, an ideal inductor is a short circuit, but the copper winding wire remains resistive. Therefore, a voltage divider between R and `r_L` is formed, and the output is lower than the input even after the transient has settled.[^aac-low-pass-filters]

For an ideal source and resistive load, the transfer function is `H(jω) = R/(R + r_L + jωL)`. At zero frequency, its magnitude is `R/(R + r_L)`. Thus, the frequency response cannot be interpreted as starting from unity gain: the passband level is lower. The pole frequency in this model equals `(R + r_L)/(2π*L)`. If the cutoff is defined by a 3 dB drop from the low-frequency plateau, that frequency corresponds to the boundary; measuring relative to the input level would yield a different value due to the insertion loss.[^aac-low-pass-filters]

Calculation example:

```text
R = 100 Ω
r_L = 20 Ω
|H(0)| = R/(R + r_L) = 100/120 ≈ 0.833
```

**Common mistake:** measuring the output only far below the pole, observing a constant attenuation, and calling it a frequency-dependent inductor loss. This is resistive voltage division that exists at DC as well; the frequency-dependent reactive impedance adds further roll-off as frequency increases. To verify the model, measure the input and output at a very low frequency, measure the winding resistance with a multimeter while the circuit is unpowered, and then evaluate the 3 dB drop relative specifically to the low-frequency plateau. A connected instrument or subsequent stage also loads the output, so for an accurate assessment, include it in the equivalent circuit.[^aac-low-pass-filters]

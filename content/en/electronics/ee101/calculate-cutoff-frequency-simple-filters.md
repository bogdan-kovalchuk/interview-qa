---
id: emb-elee-0046
title: "How do you calculate the cutoff frequency of simple RC and RL filters?"
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
  - source_id: filter-cutoff
    title: "Low-pass Filters | Filters"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-8/low-pass-filters/
---

## Short answer

For a simple first-order RC filter, `f_c = 1/(2*π*R*C)`, while for a simple RL filter, `f_c = R/(2*π*L)`. These formulas assume the basic canonical topologies without external loading that would shift the cutoff frequency.[^filter-cutoff]

## Detailed explanation

The cutoff frequency of a single-pole filter is the frequency where the amplitude drops to `1/√2`, or approximately 70.7% of the passband level. In a simple RC circuit, `τ = R*C`, whence `f_c = 1/(2*π*τ)`. In a simple RL circuit, `τ = L/R`, so `f_c = 1/(2*π*τ) = R/(2*π*L)`. The unit of both expressions for `f_c` is `1/s`, that is, hertz.[^filter-cutoff]

Topology matters: for an RC low-pass filter, the resistor is in series and the capacitor is connected to the output node; for an RL low-pass filter, a series inductor operates with the load resistance. Adding source or load resistance alters the resistance seen by the reactive element, so the simple formula with the value of a single resistor may no longer describe the actual pole.[^filter-cutoff]

Calculation example for an unloaded RC low-pass filter:
```text
R = 1 kΩ, C = 100 nF
f_c = 1/(2*π*R*C)
f_c = 1/(2*π*1000*100e-9) ≈ 1592 Hz
```
That is, the estimate is `1.59 kHz`. Real components also have tolerances and parasitic parameters, and an inductor has winding resistance. For a more complex circuit, one must derive the transfer function or verify the frequency response through simulation and measurement.[^filter-cutoff]

**Common mistake:** substituting component values without clarifying where the output is taken and whether a load is connected. First fix the circuit topology, then verify dimensional consistency and compare the calculation with a frequency sweep.

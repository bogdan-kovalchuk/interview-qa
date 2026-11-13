---
id: emb-elee-0045
title: "How do you correctly write the exponent and time constant of an RL circuit?"
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
  - source_id: rl-time-constant
    title: "Why L/R and not LR? | RC and L/R Time Constants"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/why-l-r-and-not-lr/
  - source_id: rl-transient
    title: "Voltage and Current Calculations | RC and L/R Time Constants"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/voltage-current-calculations/
---

## Short answer

For natural current decay in an RL circuit, the exponent is `-t*R/L`, and the time constant `τ = L/R` is measured in seconds. Writing `e^(-t*L/R)` or claiming `τ = R/L` inverts the relationship: `R/L` has units of `1/s` and represents the reciprocal time constant.[^rl-time-constant]

## Detailed explanation

In a series RL circuit after disconnecting the source, Kirchhoff's voltage law yields `L*di/dt + R*i = 0`. The solution to this equation is `i(t) = I0*e^(-t*R/L)`, where `I0` is the current at the beginning of the decay. It is also written as `i(t) = I0*e^(-t/τ)` when `τ = L/R`; both notations are identical because `1/τ = R/L`.[^rl-transient]

Dimensional analysis quickly catches the error: a henry equals `Ω*s`, so `L/R` has units of seconds, as required for a time constant. In contrast, `R/L` has units of `1/s`; it can multiply time in the exponent, but it is not a time. The minus sign signifies decay. For a current rising from zero to steady state, the factor `1 - e^(-t/τ)` appears.[^rl-transient]

After one time constant, the decaying current is approximately 36.8% of its initial value, because `e^-1 ≈ 0.368`. This is the model of an ideal inductor and a constant series resistance. For a more complex linear circuit, one first finds the Thevenin equivalent resistance seen from the inductor terminals; one should not automatically take the resistance of only a single resistor.[^rl-transient]

Calculation example:
```text
L = 20 mH, R = 10 Ω
τ = L/R = 0.020/10 = 0.002 s = 2 ms
i(2 ms)/I0 = e^-1 ≈ 0.368
```
Thus, after `2 ms`, about 36.8% of the initial current remains. A common mistake is transferring the `RC` formula to an inductor; substituting units or a single value of `τ` shows that the correct time constant is `L/R`.

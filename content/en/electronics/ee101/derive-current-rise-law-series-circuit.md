---
id: emb-elee-0044
title: "How do you derive the current rise law in a series RL circuit?"
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
---

## Short answer

For an ideal series RL circuit, Kirchhoff's voltage law yields `V_0 = I*R + L*dI/dt`. Under constant applied voltage `V_0` and initial condition `I(0) = 0`, the differential equation solution is `I(t) = (V_0/R)*(1 - e^(-t/τ))`, where `τ = L/R`.[^aac-alternating-current]

## Detailed explanation

The current rise law in a series RL circuit is derived from Kirchhoff's voltage law and the inductor terminal relation `v_L = L*dI/dt`. Consider an ideal `R` and `L` connected to a constant voltage `V_0` at time `t = 0`; prior to switching, the current is zero.[^aac-alternating-current]

The voltage drop across the resistor is `I*R`, so the sum of voltages across the resistor and inductor equals the source voltage: `V_0 = I*R + L*dI/dt`. Rearranging terms and separating variables, integration from the initial state to time `t` yields an exponential transition from zero to steady-state current `V_0/R`; the time constant `τ = L/R` defines the characteristic time scale of the transient.[^aac-alternating-current]

Derivation example for these initial conditions:

```text
L*dI/dt = V_0 - I*R
dI/(V_0 - I*R) = dt/L
I(t) = (V_0/R)*(1 - e^(-R*t/L))
τ = L/R
```

At `t = τ`, current reaches approximately 63.2% of its final value, and at `t = 5τ`, approximately 99.3%. This is an asymptotic approach to the limit rather than exact completion in finite time. For a non-zero initial current, the general solution takes the form `I(t) = I_final + (I(0) - I_final)*e^(-t/τ)`, where `I_final = V_0/R`.[^aac-alternating-current]

**Common mistakes:**

- Substituting `R*L` instead of `L/R` for the time constant. Checking units confirms `H/Ω = s`.
- Using this expression without acknowledging the assumptions of constant voltage and linear inductance.
- Overlooking the initial condition or failing to include source and winding resistances explicitly: in a real circuit, all series resistances contribute to the total `R`.[^aac-alternating-current]

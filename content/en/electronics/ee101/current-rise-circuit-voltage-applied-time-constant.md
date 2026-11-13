---
id: emb-elee-0041
title: "How does current rise in an RL circuit after voltage is applied, and what is its time constant?"
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

For an ideal series RL circuit with constant voltage source `V_0` and zero initial current, `I(t) = (V_0/R)*(1 - e^(-t/τ))`, where `τ = L/R`. After `5τ`, the current reaches approximately 99.3% of `V_0/R`; this estimate assumes constant `R` and `L` values.[^aac-alternating-current]

## Detailed explanation

In a series RL circuit following the application of a constant voltage, current does not jump instantaneously to the value dictated by the resistor. The change in current induces a voltage across the inductor proportional to the rate of change of current, so initially most of the source voltage falls across the inductor.[^aac-alternating-current]

For an ideal inductor and resistor, Kirchhoff's voltage law yields `V_0 = I*R + L*dI/dt`. After connecting the source with initial condition `I(0) = 0`, the solution tends toward the steady-state value `I_final = V_0/R`. The time constant `τ = L/R` dictates the rate of transition: after one `τ`, current completes approximately 63.2% of the step between its initial and final values, and after five time constants, approximately 99.3%.[^aac-alternating-current]

Example: let `L = 10 mH`, `R = 100 Ω`, and `V_0 = 5 V`. Then `τ = 0.01/100 = 0.0001 s = 0.1 ms`, and the final current is `5/100 = 0.05 A`. At `0.5 ms`, or `5τ`, the current is approximately `0.05*(1 - e^(-5)) ≈ 0.0497 A`. This calculation assumes a constant voltage and a linear model; source and winding resistances must be added to `R` if significant.[^aac-alternating-current]

**Common mistakes:**

- Confusing the RL time constant `L/R` with the RC time constant `R*C`.
- Assuming that after `5τ` the current mathematically reaches its exact final value; the exponential curve merely approaches it.
- Neglecting the initial current. A different `I(0)` alters the amplitude of the exponential transient component.[^aac-alternating-current]

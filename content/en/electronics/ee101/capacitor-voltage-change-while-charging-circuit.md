---
id: emb-elee-0031
title: "How does the capacitor voltage change while charging in an RC circuit?"
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
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
---

## Short answer

For an uncharged capacitor connected to a constant voltage `V_s` through a resistor, `V_C(t) = V_s*(1 - e^(-t/τ))`, where `τ = R*C`. The voltage increases exponentially toward `V_s`, though in an ideal mathematical model it never reaches it in finite time.[^gatech-rc-charging-discharging]

## Detailed explanation

Consider a series circuit with a constant source voltage `V_s`, a resistor `R`, and an initially uncharged capacitor `C`. Initially, the capacitor voltage is zero, so nearly the entire source voltage appears across the resistor and current is at its maximum. As charge accumulates on the plates, the capacitor voltage rises and opposes the source; the voltage across the resistor and the current gradually decrease.[^gatech-rc-charging-discharging]

For such an ideal circuit, the voltage equation is `V_C(t) = V_s*(1 - e^(-t/(R*C)))`. The product `R*C` defines the time scale of the transient. The exponential describes non-linear growth: the curve is steep initially, and its slope gradually flattens as the difference between the source voltage and the capacitor voltage diminishes. After a long time, the current approaches zero, and the capacitor voltage approaches `V_s`.[^gatech-rc-charging-discharging]

This formula assumes a single constant source, one resistor, and a capacitor of constant capacitance, without significant leakage or additional circuit elements. For a different initial voltage, the step from the initial state to the new steady-state level must be calculated, rather than assuming the capacitor always starts from zero. In a more complex network, the resistance seen by the capacitor in the corresponding transient state is used to determine `τ`.[^gatech-rc-charging-discharging]

Example: for `V_s = 5 V`, `R = 10 kΩ`, and `C = 10 µF`, we have `τ = 0.1 s`. At `t = τ`, the voltage reaches approximately 63.2% of the final 5 V, or about 3.16 V. This does not mean that after one τ the capacitor has "charged by 63.2% of its current value": the percentage is measured relative to the total step from the initial level to the final level.[^gatech-rc-charging-discharging]

**Common mistakes:**

- Drawing a linear ramp or asserting that the capacitor reaches its final voltage in exactly `τ`.
- Applying the formula to a non-zero initial voltage without accounting for the initial condition.
- Confusing the capacitor voltage with the resistor voltage: during charging, the former rises while the latter decays.

---
id: emb-elee-0034
title: "How does the capacitor voltage change while discharging through a resistor?"
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

When a charged capacitor discharges through a resistor, its voltage decays according to `V_C(t) = V_0*e^(-t/τ)`, where `τ = R*C` for a simple RC loop. After `1τ`, `3τ`, and `5τ`, approximately 36.8%, 5.0%, and 0.7% of the initial voltage remains, respectively.[^gatech-rc-charging-discharging]

## Detailed explanation

Consider a capacitor initially charged to a voltage `V_0` and connected to a resistor in a closed loop without any voltage source. The capacitor voltage drives a current through the resistor. As charge leaves the plates, the voltage decreases, and consequently the current decreases as well; this interaction produces an exponential rather than a linear decay.[^gatech-rc-charging-discharging]

For an ideal resistor `R` and capacitor `C`, the voltage is `V_C(t) = V_0*e^(-t/(R*C))`. The time constant `τ = R*C` dictates the rate of decay. After each τ, the voltage drops to approximately 36.8% of its value at the beginning of that interval: after the first τ, 36.8% of `V_0` remains; after the second, 36.8% of that remainder is left, or about 13.5% of `V_0`.[^gatech-rc-charging-discharging]

In an ideal mathematical model, the voltage approaches zero asymptotically. Thus, stating that a capacitor has "discharged" typically means that its voltage has dropped below a specified threshold, not that it has reached mathematical zero. In a physical device, other leakage paths, loads, or protective components may also be present, so the time constant is governed by the actual resistance seen by the capacitor in the discharge path.[^gatech-rc-charging-discharging]

Example: a capacitor with `V_0 = 10 V`, `R = 100 kΩ`, and `C = 10 µF` has `τ = 1 s`. After 3 s, the voltage is `10 V*e^(-3)`, or approximately 0.50 V, which is roughly 5% of the initial voltage. This calculation assumes constant `R` and `C` and no additional leakage currents.[^gatech-rc-charging-discharging]

**Common mistakes:**

- Using the charging expression with a minus sign in the exponent instead of the simple exponential decay from the initial voltage.
- Stating that after `τ` the voltage has fallen by 36.8%; in reality, it has fallen by approximately 63.2%, retaining 36.8%.
- Confusing the direction of the discharge current with the reference direction of the charging current.

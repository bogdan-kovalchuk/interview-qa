---
id: emb-elee-0035
title: "Why is the charging current of an RC circuit highest at the start and why does it fall to zero?"
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
  - source_id: aac-capacitor-transient
    title: "All About Circuits: Capacitor transient response"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-16/capacitor-transient-response/
---

## Short answer

For an ideal constant voltage source `V_0`, series resistor `R`, and initially discharged capacitor `C`, the initial current is `V_0/R`. As the capacitor charges, the resistor voltage and charging current decay exponentially with time constant `τ = R*C`; in steady state, the current approaches zero.[^aac-capacitor-transient]

## Detailed explanation

In a series RC circuit driven by an ideal voltage source `V_0`, Kirchhoff's voltage law yields `V_0 = V_R + V_C`. Immediately before the switch closes, the capacitor is discharged, so its voltage is zero. Because the voltage across a capacitor cannot change instantaneously, the entire source voltage is initially dropped across the resistor; by Ohm's law, the initial current is `I(0) = V_0/R`.[^aac-capacitor-transient]

The current through the capacitor is proportional to the rate of change of its voltage, while in the resistor it depends on the instantaneous voltage across it. As charge accumulates, `V_C` rises, `V_R = V_0 - V_C` decreases, and the current decays accordingly. For this simple circuit, the solution is exponential with time constant `τ = R*C`: after one `τ`, the capacitor voltage has covered approximately 63.2% of the way to its final value, while the current has fallen to approximately 36.8% of its initial value.[^aac-capacitor-transient]

This does not mean that the capacitor blocks the current instantaneously. The current gradually decreases throughout the transient process; mathematically it approaches zero, and in practice, after a finite duration, it simply falls below the measurement threshold. If the capacitor is initially charged or the source follows a different profile, the initial current and the overall transient are determined by the initial voltage and the complete circuit, rather than by the formula for an uncharged `C`.[^aac-capacitor-transient]

Example: for `V_0 = 5 V` and `R = 1 kΩ`, the initial current is `I(0) = 5 V / 1 kΩ = 5 mA`. Increasing `C` lengthens the transient duration, but does not alter this initial current value for the same ideal `V_0` and `R`.[^aac-capacitor-transient]

**Common mistake:** referring to `V_0/R` as the current throughout the entire process. That is merely the initial value; subsequently, current decays as the voltage drop across the resistor decreases.

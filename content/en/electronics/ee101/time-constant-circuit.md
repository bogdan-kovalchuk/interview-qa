---
id: emb-elee-0032
title: "What is the time constant `τ` of an RC circuit?"
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

The time constant of a simple RC circuit equals `τ = R*C` and is measured in seconds, because `Ω*F = s`. In one `τ`, charging voltage covers 63.2% of the total step toward its steady-state value; during discharging, 36.8% of the initial voltage remains.[^gatech-rc-charging-discharging]

## Detailed explanation

The time constant `τ` characterizes the time scale of the transient response in a simple circuit containing a resistor and a capacitor. In the simplest series circuit, it equals `R*C`: a larger resistance limits the current more severely, while a larger capacitance requires more charge for the same voltage change, so either increase slows the circuit response. The units are consistent: `Ω*F = s`.[^gatech-rc-charging-discharging]

In one τ, charging from zero toward a constant source voltage reaches approximately 63.2% of the final voltage. This is a direct consequence of the exponential law: after each subsequent τ, the same fraction of the remaining step toward the final value is traversed. In a discharging circuit, approximately 36.8% of the initial voltage remains after one τ. Therefore, τ is not the time required for complete charging or discharging; the exponential curve asymptotically approaches the limit.[^gatech-rc-charging-discharging]

In a circuit with multiple resistors, one cannot simply substitute an arbitrary single resistor into `τ = R*C`. For a first-order circuit with a single capacitor, the Thévenin equivalent resistance seen from its terminals is used, with independent ideal sources deactivated according to standard analysis methods. If a network contains multiple energy storage elements, it may possess multiple time scales, and a single τ no longer fully describes the entire response.[^gatech-rc-charging-discharging]

Calculation example:

```text
R = 10 kΩ = 10,000 Ω
C = 10 µF = 0.000010 F
τ = R*C = 10,000*0.000010 = 0.1 s = 100 ms
```

This value indicates that after 100 ms, the ideal charging voltage has completed 63.2% of its total step. It does not state that charging finishes at that point; practical settling to the final value depends on the allowable error tolerance.[^gatech-rc-charging-discharging]

**Common mistakes:**

- Referring to τ as the time for full charge; in practice, multiple τ intervals provide increasingly close approximations.
- Failing to convert microfarads and kilohms into compatible base units, leading to incorrect scaling of the result.
- Ignoring the resistance of the remainder of the circuit seen by the capacitor.

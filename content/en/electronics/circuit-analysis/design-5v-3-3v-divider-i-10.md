---
id: emb-elcirc-0030
title: "Design an unloaded 5 V to 3.3 V divider drawing 10 mA."
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ti-slaa067
    title: "Texas Instruments: Understanding Basic Analog – Circuit Equations"
    url: https://www.ti.com/lit/pdf/slaa067
---

## Short answer

For an unloaded divider, exact resistor values are `R_1 = 170 Ω` and `R_2 = 330 Ω`, which draw 10 mA from a 5 V supply and output 3.3 V. Using standard E24 values of `180 Ω` and `330 Ω` yields approximately 3.24 V and 9.8 mA rather than the exact nominal 10 mA target.[^ti-slaa067]

## Detailed explanation

For an unloaded divider between 5 V and ground that must provide 3.3 V and draw 10 mA, exact nominal values with an ideal supply voltage are `R_1 = 170 Ω` and `R_2 = 330 Ω`. The 10 mA current passes sequentially through both series resistors. The lower resistor must drop 3.3 V, while the upper drops the remaining 1.7 V; Ohm's law determines the required resistances.[^ti-slaa067]

First calculate total resistance as `R_total = V_in/I = 5 V / 0.01 A = 500 Ω`. For the lower resistor, `R_2 = V_out/I = 3.3 V / 0.01 A = 330 Ω`. The remaining resistance belongs to the upper resistor: `R_1 = R_total - R_2 = 170 Ω`. Verifying with the unloaded divider formula returns `V_out = 5 V * 330 / (170 + 330) = 3.3 V`.[^ti-slaa067]

In the standard E24 series, a 170 Ω value is not available, so one can choose the closest standard value of 180 Ω while retaining 330 Ω for the lower branch. Then `V_out = 5 V * 330 / (180 + 330) ≈ 3.24 V`, and current equals `5 V / 510 Ω ≈ 9.8 mA`. This represents a practical trade-off with an approximate output rather than exact satisfaction of initial design targets. Resistor tolerances and actual supply voltage will introduce further deviations.[^ti-slaa067]

**Common mistakes:**

- Applying 10 mA to only one resistor, even though in an unloaded circuit this identical current passes through both.
- Labeling the 180 Ω and 330 Ω pair as exact: its output is approximately 3.24 V and its current is approximately 9.8 mA.
- Failing to state that the calculation assumes an unloaded output; connecting a load alters the effective resistance of the lower branch.

In a real device, a divider continuously drawing 10 mA dissipates `P = V_in*I = 50 mW` in total. One must also verify the power dissipation rating of each resistor, component tolerances of available values, and the operating load current range. If the output must power a load, that current must be factored into the design or a buffer added; otherwise, the target 3.3 V is not guaranteed.[^ti-slaa067]

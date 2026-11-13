---
id: emb-elcirc-0028
title: "What is the voltage divider \"stiffness\" rule – what is the minimum acceptable load?"
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

As a rule of thumb, maintaining `R_load >= 10*R_2` limits loaded output voltage sag to approximately 9.1% or less compared to the unloaded divider. Because `R_load` is connected in parallel with the lower resistor `R_2`, the exact output voltage must be calculated using the parallel combination `R_2 || R_load`.[^ti-slaa067]

## Detailed explanation

Voltage divider "stiffness" describes how little its output voltage changes when a load is connected across its output. In a basic divider, `R_1` connects to the supply source, `R_2` connects to ground, and `V_out` is taken from the node between them. Without a load, output voltage is a fraction of `V_in` determined by the resistance ratio.[^ti-slaa067]

A connected load with resistance `R_load` appears in parallel with the lower resistor. Therefore, the calculation must use `R_2 || R_load` in place of `R_2`; the lower equivalent resistance reduces the output voltage. The condition `R_load >= 10*R_2` is a rule of thumb, not a universal error bound for every definition of error. Under this condition, voltage sag relative to the unloaded `V_out` does not exceed approximately 9.1%; if tighter precision is required, output voltage should be calculated for specific nominal values.[^ti-slaa067]

Example: if `R_1 = R_2`, the unloaded output equals half the input voltage. With `R_load = 10*R_2`, the parallel combination is approximately `0.909*R_2`, and the output becomes approximately `0.476*V_in` instead of `0.5*V_in`, a drop of approximately 4.8%. The upper bound of 9.1% occurs in the limiting case where `R_1` is much larger than `R_2`.[^ti-slaa067]

**Common mistakes:**

- Comparing load resistance against the sum `R_1 + R_2`, whereas it is the parallel load across the lower branch that alters the divider.
- Treating the 10:1 rule as a guarantee of arbitrary precision without substituting actual values into the formula.
- Increasing both resistors to reduce power consumption without recognizing that output impedance and load sensitivity increase accordingly.

If a divider must supply substantial load current or maintain a stable voltage, a purely passive resistive circuit may be unsuitable. A buffer or voltage regulator with sufficient current capability isolates the divider from the load; the selection also depends on resistor tolerances and the input bias current of the subsequent stage.[^ti-slaa067]

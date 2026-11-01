---
id: emb-elintro-0187
title: "What is a regulator's line regulation?"
track: electronics
section: introduction
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: ti-regulator-regulation
    title: "TI: Identify the Most Accurate Linear Voltage Regulator"
    url: https://www.ti.com/document-viewer/lit/html/SSZTCA7/GUID-C15E9A5E-C4B2-4C77-98A3-C375536EE8EF
  - source_id: aac-zener-regulator
    title: "All About Circuits: What Are Zener Diodes?"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/chpt-3/zener-diodes/
---

## Short answer

Line regulation describes the change in a regulator's output voltage when `V_in` varies at a fixed load, and is often specified as `ΔV_out/ΔV_in` or in percent per volt.[^ti-regulator-regulation] For a simple Zener regulator, it cannot be generalized to a fixed 5% or the condition `V_in ≥ V_Z + 3 V`: the limit depends on `R_s`, the load current, and the minimum Zener diode current.[^aac-zener-regulator]

## Detailed explanation

Line regulation is a measure of how much the output voltage changes when the input voltage varies while keeping the load constant. It is measured over a specified input range and under specified conditions; for linear regulators, the manufacturer may specify `ΔV_out/ΔV_in` or a relative change per volt. A smaller value means that input variation is less coupled to the output in this operating mode.[^ti-regulator-regulation]

In a simple circuit with a Zener diode, the input voltage determines the current through `R_s`. With an approximately constant output, increasing `V_in` increases this current, and under a constant load, the additional portion mostly flows through the Zener diode. Changes in its current slightly alter the voltage due to non-zero dynamic resistance, so the output is not mathematically constant. If the input drops so much that the current is no longer sufficient for the load and the minimum Zener diode current, the regulator leaves the regulation mode; this is a headroom limit, not a percentage line regulation characteristic.[^aac-zener-regulator]

Example: if under an unchanged load `V_out = 5.08 V` is measured at `V_in = 9 V` and `V_out = 5.12 V` at `V_in = 12 V`, then the output change is `40 mV` for an input change of `3 V`. The ratio `ΔV_out/ΔV_in` is approximately `13.3 mV/V` over this interval. This is merely the result of a specific measurement, not a typical standard for all regulators.

**Common mistakes:**

- Confusing line regulation with load regulation: here the input changes, while the load is fixed.
- Calling "5%" a universal limit or considering `V_Z + 3 V` an exact condition: the required headroom depends on currents, the resistor, and component parameters.[^aac-zener-regulator]

---
id: emb-elcirc-0025
title: "What is the power in each component and how do you check it?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-power-calculations
    title: "All About Circuits: How to Calculate Power in a Series and Parallel Circuit"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/power-calculations/
---

## Short answer

For a resistor, power dissipation can be computed as `P = V*I`, `P = I²*R`, or `P = V²/R` using consistent voltage, current, and resistance values for that component. Verify conservation of power across the entire circuit: total power absorbed by passive loads must equal total power delivered by active sources, where a delivering source has negative power under the passive sign convention.[^aac-power-calculations]

## Detailed explanation

Electrical power indicates the rate of energy transfer or conversion. For a resistor, it can be obtained from measured or calculated voltage and current: `P = V*I`. If resistance is known, Ohm's law provides the equivalent formulations `P = I²*R` and `P = V²/R`; select whichever form uses the available quantities.[^aac-power-calculations]

Before calculating, clarify which specific voltage and current belong to the component. For a series resistor, the current is shared, but its voltage is solely its individual drop; for a parallel branch, the voltage is shared, but the current is branch-specific. Substituting total circuit voltage or current instead of local values yields an erroneous power value. Also verify units: volts, amperes, and ohms yield power in watts.[^aac-power-calculations]

To verify an entire circuit, use power balance, accounting for both loads and sources. Under the passive sign convention, current entering the terminal labeled `+` indicates positive absorbed power. If current enters the negative terminal and a source delivers energy, the calculation carries a negative sign. In that case, the algebraic sum of powers across all circuit elements equals zero; the equality between the sum of resistor powers and source power magnitude is a special case for circuits containing only that single source and purely resistive loads.[^aac-power-calculations]

**Example:**

A voltage drop of `5 V` is measured across a `100 Ω` resistor. The current is `5 V / 100 Ω = 0.05 A`, and power is `5 V * 0.05 A = 0.25 W`. If the rated power dissipation of the resistor is lower than this value, this operating condition is unacceptable; in practical design, also factor in cooling conditions and thermal derating.

**Common mistakes:**

- Applying a local component formula using total circuit parameters.
- Comparing positive resistor powers against a signed negative source power without clarifying the sign convention.
- Checking only resistors when the circuit may contain other elements that store or transfer energy.[^aac-power-calculations]

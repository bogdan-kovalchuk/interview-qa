---
id: emb-elintro-0073
title: "How do you estimate the balancing current between two parallel batteries?"
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
---

## Short answer

Estimate the initial current as `I = ΔV/(R_int1 + R_int2 + R_wires)`, where `ΔV` is the open-circuit voltage difference, and `R_wires` includes wires and contacts. For example, with `ΔV = 0.5 V` and a total resistance of `0.1 Ω`, a simple resistive model yields `5 A`; this is an approximation, not an exact prediction of battery behavior.[^aac-direct-current]

## Detailed explanation

A balancing current is the current that flows from the battery with higher open-circuit voltage to the battery with lower voltage after a parallel connection. For a first estimate, batteries are modeled as ideal voltage sources with series internal resistances. The current loop passes through the resistance of both batteries and the connecting wires, so the total resistance in the denominator is the sum of these components.[^aac-direct-current]

Worked example for a simplified model:

```text
ΔV = 12.8 V - 12.3 V = 0.5 V
R_total = 0.04 Ω + 0.05 Ω + 0.01 Ω = 0.10 Ω
I ≈ ΔV/R_total = 0.5 V/0.10 Ω = 5 A
```

Thus, the estimated initial current is `5 A`. The internal resistance value is not a constant characteristic for all conditions: measurements depend on state of charge, temperature, frequency or pulse duration, and test method. Electrochemical polarization also makes a battery more complex than an ideal source with a single resistor, so the current changes over time. Protection design requires manufacturer data or measurements for the specific battery, not just this formula.[^aac-direct-current]

**Common mistake:** dividing the voltage difference by the resistance of only one battery or neglecting wire and contact resistance. This yields an incorrect current estimate, so you must account for the entire loop and keep in mind the limitations of a simple resistive model.[^aac-direct-current]

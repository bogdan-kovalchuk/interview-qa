---
id: emb-elcirc-0015
title: "Which three basic laws are used to analyze a linear resistive DC circuit?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-network-theorems-intro
    title: "All About Circuits: Introduction to Network Theorems for Circuit Analysis"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-10/introduction-network-theorems/
---

## Short answer

Analyzing a linear resistive DC circuit relies on Ohm's law (`V = I*R`), Kirchhoff's Current Law (the algebraic sum of currents at a node is zero), and Kirchhoff's Voltage Law (the algebraic sum of voltages around a closed loop is zero). Complete analysis also requires knowing the circuit topology and element ratings; asserting these laws alone solve any arbitrary circuit without component models is overly broad.[^aac-network-theorems-intro]

## Detailed explanation

For a linear resistive DC circuit, the three fundamental relationships are Ohm's law, KCL, and KVL. Ohm's law relates the voltage across a resistive element to the current through it and its resistance. KCL describes the balance of currents at nodes, while KVL describes the balance of voltages along a closed path. Together, they provide the equations to solve for unknown voltages and currents.[^aac-network-theorems-intro]

These are not three single equations written once for an entire circuit. KCL is written for the required nodes, KVL for independent loops, and the element relationship is applied to each resistor. Current directions and voltage polarities can initially be assumed; negative results indicate the opposite physical direction. Known sources impose boundary conditions, and the actual number of independent equations depends on network topology.[^aac-network-theorems-intro]

**Example:**

A `9 V` source is connected in series with `1 kΩ` and `2 kΩ`. Ohm's law for the equivalent resistance gives `I = 9 V/(1 kΩ + 2 kΩ) = 3 mA`. Ohm's law separately determines the voltage drops: `V_1 = 3 V` and `V_2 = 6 V`. A KVL check gives `9 V - 3 V - 6 V = 0`; at every node along the series path, KCL confirms the exact same current before and after each component.[^aac-network-theorems-intro]

**Scope of the claim:**

Calling these rules a complete set for "any" electrical circuit without specifying the component model is inappropriate. Realistic analysis requires the constitutive relationships of each element: a diode, transistor, capacitor, or inductor is not described by `V = I*R` as a linear resistor is. Depending on the problem, non-linear or time-domain models, initial conditions, and other constraints are required. Furthermore, in networks with mutual inductance or time-varying magnetic flux, the simple form of KVL requires refinement. For a purely resistive linear DC model, the Ohm/KCL/KVL triad serves as a valid foundation applied across elements, nodes, and loops, rather than a universal list of three ready-made equations.[^aac-network-theorems-intro]

**Common mistake:**

- Assuming that KCL and KVL by themselves define component characteristics or that `V = I*R` describes every element. First determine the model of each element and the applicability limits of the equations.[^aac-network-theorems-intro]

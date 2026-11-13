---
id: emb-elcirc-0046
title: "What is the minimal checklist before trusting a SPICE result?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: aac-spice-series-parallel
    title: "All About Circuits: SPICE Simulation of Series and Parallel Circuits"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-5/spice-simulation-of-series-and-parallel-circuits/
  - source_id: aac-spice-model-quality
    title: "All About Circuits: Just How Accurate Is a SPICE Model?"
    url: https://www.allaboutcircuits.com/textbook/designing-analog-chips/simulation/how-accurate-is-a-spice-model/
---

## Short answer

Verify units and prefixes, ground node 0 reference, node connectivity, and source polarities; confirm that component models and analysis types match the measured target. Then compare the result with hand calculations for a simplified case: discrepancies can indicate schematic errors, simulator setup issues, or model limitations.[^aac-spice-series-parallel] [^aac-spice-model-quality]

## Detailed explanation

SPICE evaluates a mathematical model of a circuit described by a netlist or generated from a schematic editor. The result reflects this specific model and chosen analysis type rather than automatically representing a physical device. Therefore, verification starts by confirming that the schematic description matches the design intent: nodes, component ratings, source polarities, and assigned models must all be correct.[^aac-spice-series-parallel] [^aac-spice-model-quality]

In SPICE, node `0` serves as the reference potential for measuring node voltages; it is not necessarily a physical chassis ground or earth ground. Confirm that points intended to be electrically common are genuinely connected in the netlist rather than merely drawn adjacent to one another. Polarity dictates the sign of voltages and currents, and source definitions establish reference measurement directions.[^aac-spice-series-parallel]

Choose an analysis type that directly addresses the design question. Operating point or DC sweep describes steady-state bias, AC analysis evaluates small-signal frequency response, and transient analysis computes time-domain evolution. Selecting the right analysis directive does not in itself guarantee that initial conditions, time steps, or frequency spans match the physical problem. Review simulator error and warning messages, as well as axis scales and units of reported quantities.[^aac-spice-series-parallel]

A component model has defined boundaries of accuracy and validity. For example, a simplified transistor model might not reproduce saturation behavior accurately; suitability of a model for a specific part and operating regime must be confirmed against documentation or experimental measurements.[^aac-spice-model-quality]

**Verification example:**

For a 9 V source connected to series resistors of 3 kΩ, 10 kΩ, and 5 kΩ, hand calculation yields `I = 9 V / 18 kΩ = 0.5 mA`. If simulation yields a significantly different value, check node ordering, component values, current measurement direction, and the chosen analysis mode; in the All About Circuits example, the SPICE result matches Ohm's law calculations directly.[^aac-spice-series-parallel]

Such agreement confirms the consistency of this simple baseline example, but it does not serve as generalized proof of accuracy for complex circuitry. For an analog design, consider model capabilities, temperature coefficients, and component tolerances; for critical decisions, cross-check simulations against datasheets, independent analytical calculations, or prototype measurements.[^aac-spice-model-quality]

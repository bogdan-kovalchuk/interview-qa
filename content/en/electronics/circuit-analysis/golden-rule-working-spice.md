---
id: emb-elcirc-0044
title: "What is the golden rule of working with SPICE?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-manual-models
    title: "ngspice User's Manual: Device Models and Analyses"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

Use SPICE to verify hypotheses within explicitly defined circuit schematics and models, confirming key assumptions through analytical calculations or prototype measurements. Simulation does not guarantee matching hardware behavior: results depend on model accuracy, component parameters, and the chosen analysis type.[^ngspice-manual-models]

## Detailed explanation

A useful rule when working with SPICE is to treat the output as a verification of the model rather than as a measurement of an assembled hardware device. The simulator reads the netlist, constructs mathematical representations of the components, and solves the corresponding equations. If a node is miswired in the description, a required model is missing, or incorrect initial conditions are applied, the resulting plot may look neat, but it will reflect that faulty description.[^ngspice-manual-models]

Therefore, before launching a simulation, articulate what the analysis is intended to verify, and check whether necessary parameters are represented in the model. After running it, evaluate the order of magnitude, polarity, operating point, and boundary conditions. For critical conclusions, compare the simulation with an independent calculation or benchmark measurement; discrepancies often reveal a circuit error, an overlooked physical effect, or component limitations.

For example, before testing an amplifier, verify that the transistor model matches the component type, sources have correct values, and the operating point does not clamp the output against a supply rail. Then compare simulated amplitude against a prototype measurement under identical test conditions. Discrepancies should not be automatically dismissed as a "SPICE error": first inspect comparison conditions and model fidelity.

**Common mistakes:**

- Assuming that the simulator verified physical tolerances, thermal dissipation, or parasitic coupling when none were specified.
- Trusting a single waveform plot without performing a sanity check using Ohm's law, energy conservation, and component operating ratings.

---
id: emb-elcirc-0042
title: "What does SPICE not account for by default?"
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

SPICE calculates the behavior of specified models and operating conditions rather than automatically accounting for all real-board effects. Parasitic parameters, tolerances, temperature dependencies, and cross-coupling between traces appear in results only when represented by appropriate models or analysis directives; the available feature set depends on the simulator and netlist.[^ngspice-manual-models]

## Detailed explanation

A SPICE simulator solves equations formulated from the circuit description, component models, and selected analysis type. It does not automatically "see" the physical board: trace geometry, parasitic capacitances and inductances, thermal dissipation, and cross-coupling with adjacent nodes do not materialize simply because components are drawn on a schematic.[^ngspice-manual-models]

This does not mean that SPICE can never account for these phenomena. They can be approximated with supplemental elements, model parameters, or specialized subcircuits if the chosen simulator supports them. Similarly, a resistor tolerance does not automatically result in random variations during a single run: nominal model values remain exact until the user configures tolerances, parameter sweeps, or Monte Carlo runs.

Consider a simple RC filter. Ideal component values yield the calculated behavior of an ideal circuit; adding equivalent series resistance to a capacitor or board parasitic capacitance will alter that response only if those parameters are explicitly included. Comparing simulation results with laboratory measurements helps identify which effects the model lacks, but doing so also requires accounting for component tolerances, test conditions, and measurement instrument loading.

**Common mistakes:**

- Claiming that the simulator always ignores thermal effects or parasitics. Check the model, simulation directives, and documentation for the chosen tool.
- Attributing any discrepancy between simulation and physical measurement to a "SPICE bug". First check the schematic, component values, initial conditions, and what physical effects are absent from the model.

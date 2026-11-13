---
id: emb-elcirc-0045
title: "When should you use `.op`, `.tran`, and `.ac` in SPICE?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-analysis-types
    title: "ngspice User's Manual: OP, TRAN, and AC Analyses"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

`.op` finds the DC operating point; `.tran` displays the time-domain response to specified stimuli; `.ac` computes the small-signal frequency response linearized around the operating point. An `.ac` analysis requires an AC source excitation, whereas large-signal nonlinear behavior is typically examined using `.tran`.[^ngspice-analysis-types]

## Detailed explanation

Each analysis command answers a specific question regarding the circuit model. `.op` computes the DC operating point: steady-state node voltages and branch currents under DC conditions. This bias point is essential for non-linear components, as a transistor or diode behaves differently depending on its operating bias. In many workflows, the simulator also calculates this operating point prior to other analyses to establish initial conditions or a linearized small-signal model.[^ngspice-analysis-types]

`.tran` calculates time-domain response. It is suited for power-up transients, switching, pulse excitation, and large-signal non-linear behavior. A duration and a sufficiently fine maximum time step must be specified: an excessively coarse step can skip a fast edge or short pulse. Initial conditions also strongly influence the early portion of the transient response.[^ngspice-analysis-types]

`.ac` analyzes small-signal frequency-domain behavior around the DC operating point. It provides gain and phase as a function of frequency, but it is not a direct time-domain sweep of a large sinusoidal signal: non-linear device models are linearized, and independent sources must specify an AC excitation value.[^ngspice-analysis-types]

Example: for an RC filter, `.op` reveals steady-state DC levels, `.tran` shows capacitor charging following an input step, and `.ac` displays gain and phase variations over frequency. If evaluating diode switching waveforms, `.ac` cannot substitute for transient time-domain analysis.

**Common mistakes:**

- Selecting `.ac` for large-signal or non-linear transient behavior; use `.tran` instead.
- Forgetting to specify the source AC amplitude, resulting in uninformative frequency-response results.
- Configuring the time step without regard for the fastest event in the circuit.

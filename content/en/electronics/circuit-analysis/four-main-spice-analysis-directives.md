---
id: emb-elcirc-0038
title: "What are the four main SPICE analysis directives?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: ngspice-analysis-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

`.op` finds the DC operating point, `.tran` calculates time-domain transient response, `.ac` determines small-signal frequency response, and `.dc` sweeps a DC parameter or source to compute the operating point for each value.[^ngspice-analysis-manual] These names and directives follow ngspice; feature support and syntax of a specific simulator should be verified in its documentation.[^ngspice-analysis-manual]

## Detailed explanation

In ngspice, four common analyses answer distinct questions about the same circuit: operating point, time-domain behavior, small-signal frequency response, or reaction to sweeping a DC value.[^ngspice-analysis-manual]

`.op` calculates the DC operating point: steady-state node voltages and branch currents. This is useful for checking bias in a transistor stage; capacitors are treated as open circuits and inductors as short circuits in standard operating point calculations.[^ngspice-analysis-manual]

`.tran` solves the circuit at sequential time points to show how the output evolves following a pulse, power-up, or other time-domain stimulus. It requires a time interval and step parameters; excessively coarse time steps can miss rapid transitions, while non-linearities and circuit complexity can increase computation time.[^ngspice-analysis-manual]

`.ac` performs small-signal analysis in the frequency domain. The simulator first solves for the DC operating point, linearizes non-linear models around it, and then calculates the complex response to an AC excitation across specified frequencies. This yields magnitude and phase, but it is not a large-signal time-domain simulation.[^ngspice-analysis-manual]

`.dc` sweeps a selected source or parameter over a specified range and repeatedly recalculates the DC state. This allows plotting transfer characteristics, such as output voltage versus input DC level. Unlike `.tran`, the sequence of values here does not represent the progression of time.[^ngspice-analysis-manual]

**Common mistake:** Labeling any output waveform plot as an "AC analysis". The choice depends on the question: steady-state conditions require `.op`, time waveforms require `.tran`, small-signal frequency dependence requires `.ac`, and static parameter sweeps require `.dc`.[^ngspice-analysis-manual]

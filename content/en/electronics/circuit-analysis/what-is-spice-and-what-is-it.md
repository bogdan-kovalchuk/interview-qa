---
id: emb-elcirc-0037
title: "What is SPICE and what is its purpose?"
track: electronics
section: circuit-analysis
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-direct-current
    title: "All About Circuits textbook, Volume I: DC"
    url: https://www.allaboutcircuits.com/textbook/direct-current/
  - source_id: berkeley-spice-report-1973
    title: "UC Berkeley EECS Technical Report UCB/ERL M382: SPICE"
    url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1973/22871.html
  - source_id: ngspice-manual
    title: "ngspice User's Manual"
    url: https://ngspice.sourceforge.io/docs/ngspice-manual.pdf
---

## Short answer

SPICE stands for **Simulation Program with Integrated Circuit Emphasis**, a circuit simulator originated at UC Berkeley in 1973.[^berkeley-spice-report-1973] It computes the behavior of a specified circuit model, including DC operating conditions, transient responses, and small-signal AC response, without requiring a physical prototype.[^ngspice-manual]

## Detailed explanation

SPICE provides software simulation of an electrical circuit from a netlist description that lists components, their connected nodes, and models.[^ngspice-manual]

The name originates from Simulation Program with Integrated Circuit Emphasis. The original software was developed at UC Berkeley; a 1973 technical report describes nodal analysis alongside non-linear DC, small-signal, and transient analysis. Today, the name SPICE refers to a family of compatible simulators, so specific commands, device models, and supported features must be checked against the documentation of the particular tool.[^berkeley-spice-report-1973]

The simulator translates a netlist into a mathematical model. For a linear resistive circuit, it applies Kirchhoff's laws and component parameters; for non-linear components such as diodes and transistors, the solver computes the operating state using numerical methods. In transient analysis, it iteratively solves the model at discrete time steps, while in AC analysis, it linearizes non-linear components around the DC operating point and evaluates the small-signal response.[^ngspice-manual]

The outcome depends on model quality and underlying assumptions. A physical resistor has a tolerance, a transistor exhibits specific parameter spreads, and parasitics or temperature can alter behavior; a netlist cannot guess physics that was never included. Therefore, SPICE is valuable for verifying expected operation, comparing design alternatives, and catching mistakes prior to assembly, but it does not replace parameter sensitivity checks or measurements on the physical board.[^ngspice-manual]

**Common mistake:** Treating simulation as absolute proof that the physical board will operate identically. Ensure that device models correspond to real components and operating conditions, and keep in mind that conclusions are limited strictly to the physical effects the simulator actually models.[^ngspice-manual]

---
id: emb-elintro-0001
title: What is the "lumped circuit model" and why is it needed?
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
  - source_id: mit-lumped
    title: "MIT 6.200 Lecture 1: Lumped circuit abstraction"
    url: https://circuits.mit.edu/_static/S23/handouts/lec01a/lecture01a.pdf
---

## Short answer

The lumped circuit model represents a circuit as connected ideal elements such as resistors, capacitors and inductors. It replaces a spatial electromagnetic-field problem with voltages, currents and circuit equations, provided propagation effects and other neglected field effects are insignificant. [^mit-lumped]

## Detailed explanation

A resistor concentrates resistance in one element, a capacitor concentrates electric-field energy storage, and an inductor concentrates magnetic-field energy storage. Interconnecting wires are initially treated as ideal connections. Kirchhoff equations then describe node voltages and branch currents without solving the full field distribution. This is an approximation with explicit assumptions, not a different physical law. [^mit-lumped]

Its propagation assumption requires the circuit transit time to be much shorter than the relevant signal time scale. A slowly varying signal on a small board can often be modeled this way; a long cable or a fast digital edge may require a transmission-line model. Edge rise time matters even if the clock repetition rate is low. [^mit-lumped]

For example, a source and a resistor can be represented by one voltage and one branch current instead of a separate voltage at every point along a wire. When an ignored wire impedance or delay matters, refine the model by adding parasitic elements or distributed interconnects. A useful model is the simplest one that retains the effects needed for the question.

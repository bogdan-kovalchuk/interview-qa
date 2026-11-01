---
id: emb-elintro-0099
title: "Why can a reactive load increase mains current without doing useful work?"
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
  - source_id: aac-ac-power
    title: "True, Reactive, and Apparent Power"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-11/true-reactive-and-apparent-power/
---

## Short answer

Ideal inductors and capacitors periodically store field energy and return it to the source, so their average real power over a period is zero, even though RMS current is not necessarily zero. This current still causes `I_rms^2*R` losses in wiring and source internal resistance; real reactive components also have losses.[^aac-ac-power]

## Detailed explanation

In a reactive circuit, current and voltage are phase-shifted. In an ideal inductor, energy transfers into the magnetic field, and in an ideal capacitor, into the electric field; during another part of the cycle, the field returns the energy to the source. Over a full period, the net energy transfer into an ideal reactive element equals zero, but instantaneous current and energy exchange continue.[^aac-ac-power]

The grid and generator are loaded not only by real power, but also by RMS current. Reactive current increases apparent power in `VA`; through cable resistance and the source's internal resistance, this current dissipates heat according to `P_loss = I_rms^2*R`. Therefore, the phrase "without doing useful work" refers to the ideal reactive portion of the load rather than the entire real circuit: conductors heat up, and inductors have winding resistance and other losses.[^aac-ac-power]

For a sinusoidal single-phase circuit, `P = V_rms*I_rms*cos(φ)`. If the power factor drops while voltage and real power remain unchanged, the source requires a higher RMS current. For example, for `120 W` at `120 V` and `cos(φ) = 0.5`, `I_rms = 2 A` is required; at a power factor of `1`, the same real power requires `1 A`. This example assumes sinusoidal operation and constant voltage.[^aac-ac-power]

**Common mistake:** asserting that a reactive load draws current but "does nothing," so conductors do not heat up. It may consume zero average real power in an ideal model, but the current creates losses across all non-zero resistances of a real circuit.

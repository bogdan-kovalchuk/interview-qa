---
id: emb-elee-0038
title: "What is the main property of an inductor?"
track: electronics
section: ee101
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
  - source_id: aac-inductor-calculus
    title: "All About Circuits: Inductor voltage and current relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
---

## Short answer

An inductor develops a voltage that opposes changes in the current passing through it: for an ideal inductance, `v_L = L*di/dt`. It stores energy in a magnetic field according to `E = L*I^2/2`; under constant DC current, its induced voltage is zero.[^aac-inductor-calculus]

## Detailed explanation

The fundamental property of an inductor is that its voltage is related to the rate of change of current, rather than simply to the instantaneous value of current. For an ideal linear inductance, the governing relationship is `v_L = L*di/dt`, where `L` is measured in henries. Under the passive sign convention, the sign of the voltage is determined by the chosen reference directions for current and polarity; physically, self-induction opposes changes in current in accordance with Lenz's law.[^aac-inductor-calculus]

Attempting to increase current more rapidly requires a higher voltage across the inductor. When current is constant, its time derivative is zero, so the ideal inductive voltage is also zero, even though the magnetic field and stored energy may be non-zero. This is why an inductor is not a "resistor that limits DC current": during transients, it limits the rate of change of current rather than fixing its magnitude independently of the rest of the circuit.[^aac-inductor-calculus]

In an ideal linear model, the energy stored in the magnetic field is `E = L*I^2/2`. Increasing current increases stored energy; as current decreases, the inductor returns that energy to the circuit. Therefore, when a current path is interrupted, the inductor develops a voltage of appropriate polarity to maintain current flow until that energy is absorbed by an available discharge path or dissipated. A physical circuit requires such a path, such as a diode or clamp, sized to meet circuit voltage limits.[^aac-inductor-calculus]

A physical inductor includes winding resistance and other parasitic effects; at high enough currents, its magnetic core may also leave the linear region. Thus, while ideal model formulas effectively illustrate the mechanism, the terminal voltage measured on a real component also includes a resistive drop, and the effective `L` can vary with operating conditions.[^aac-inductor-calculus]

Example: if current through an ideal inductor with `L = 10 mH` rises at a rate of `2 A/ms`, the required inductive voltage is `v_L = 0.01 H * 2000 A/s = 20 V`. At that same current magnitude without change over time, the inductive voltage component is zero.[^aac-inductor-calculus]

**Common mistake:** claiming that an inductor "blocks current". It opposes changes in current; the actual current is determined by the overall circuit and its operating history.

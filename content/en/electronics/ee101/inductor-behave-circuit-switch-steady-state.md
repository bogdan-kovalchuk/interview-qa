---
id: emb-elee-0039
title: "How does an inductor behave in a DC circuit at switch-on and in steady state?"
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

In a series RL circuit after applying a constant voltage, current through the inductor cannot change instantaneously, rising instead toward steady state with time constant `τ = L/R`. In steady-state DC, an ideal inductor develops zero voltage and acts as a short circuit; a physical coil retains winding resistance and core losses.[^aac-inductor-calculus]

## Detailed explanation

At the instant of switching, inductor current cannot change discontinuously in a standard circuit with finite voltages. The equation `v_L = L*di/dt` shows that an instantaneous jump in current would require an infinite voltage. Therefore, the current immediately following switching equals the current immediately prior; it is not necessarily zero if the coil was already conducting current.[^aac-inductor-calculus]

For the common case of a series RL circuit with an ideal constant-voltage source `V`, a resistor `R`, and initially zero current, the current rises exponentially toward `V/R`. The time constant `τ = L/R` indicates the scale of the transient: after one `τ`, current has covered about 63.2% of the step from the initial to the final value. This rule strictly applies to a first-order circuit with constant parameters; a different topology or initial current yields different boundary values.[^aac-inductor-calculus]

Once the transient settles under constant DC current, `di/dt = 0`, so the voltage across an ideal inductor is zero. In such analysis, it is modeled as a short circuit, but that does not mean a physical coil has zero resistance: its winding has DC resistance (DCR) and dissipates heat, and its parameters can vary with frequency, current, and core properties.[^aac-inductor-calculus]

If a circuit carrying current is abruptly opened, the inductor attempts to maintain that current and can generate a high inductive spike. A practical design must provide a discharge path for this stored energy, such as a flyback diode for an appropriate low-voltage DC load or another clamp device selected for polarity, speed, and breakdown voltage. Without such a path, the voltage spike can damage the switch or insulation.[^aac-inductor-calculus]

Example for an ideal series circuit: with `V = 12 V`, `R = 6 Ω`, and `L = 30 mH`, the steady-state current is `12/6 = 2 A`, and `τ = 0.03/6 = 0.005 s = 5 ms`. Physical DCR must be included in the total series resistance, making the actual final current less than `2 A`.[^aac-inductor-calculus]

**Common mistake:** claiming that an inductor is always an "open circuit" at switch-on. It simply maintains its previous current value; how current evolves after switching is dictated by the rest of the circuit.

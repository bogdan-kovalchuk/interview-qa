---
id: emb-elee-0047
title: "How does an RC circuit differ from an RL circuit in DC steady state and in phase?"
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
  - source_id: phase-basics
    title: "Phase Relationships in Inductive and Capacitive Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/phase-relationships/
---

## Short answer

In steady-state DC, an ideal capacitor acts as an open circuit, whereas an ideal inductor acts as a short circuit. Under sinusoidal AC conditions, current through a capacitor leads voltage by 90°, whereas voltage across an inductor leads current by 90°.[^phase-basics]

## Detailed explanation

A capacitor and an inductor store energy, so they cannot instantaneously change their voltage or current, respectively. Their constitutive relations `i = C*dv/dt` and `v = L*di/dt` explain their behavior over time. In steady-state DC, the capacitor voltage does not change, so the current through an ideal capacitor is zero. The current of an ideal inductor is constant, so the voltage across it is zero.[^phase-basics]

In sinusoidal steady state, the derivative shifts the phase by a quarter of a period. For a capacitor, current leads voltage by 90°, whereas for an inductor, voltage leads current by 90°. This statement applies to an ideal reactive element. In a real circuit, resistance, other components, and loads are present, so the overall phase angle depends on frequency and topology and is generally not exactly 90°.[^phase-basics]

For example, at `f = 1 kHz`, the period is `1 ms`, and a quarter period is `0.25 ms`. In a pure inductor, the voltage maximum occurs a quarter period earlier than the current maximum. Steady-state DC has no period or phase lead: it is a different operating regime, not a sine wave with zero phase.[^phase-basics]

**Common mistake:** confusing the direction of the phase shift. ELI indicates that in an inductor (`L`), electromotive force/voltage (`E`) leads current (`I`); ICE reminds us that in a capacitor (`C`), current leads voltage. Verify this using the component governing equations and remember conventions regarding polarity and phasors.

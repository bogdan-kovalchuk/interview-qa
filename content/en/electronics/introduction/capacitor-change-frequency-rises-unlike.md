---
id: emb-elintro-0140
title: "How does a capacitor's `X_C` change as frequency rises, unlike `X_L`?"
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
  - source_id: aac-capacitor-reactance-precise
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
---

## Short answer

For an ideal capacitor, `X_C = 1/(2π*f*C)`, so reactance decreases as frequency rises. In comparison, `X_L = 2π*f*L` increases; claims about passing signals depend on the entire circuit, not just the component.[^aac-capacitor-reactance-precise]

## Detailed explanation

The capacitive reactance of an ideal capacitor for sinusoidal AC is determined by the formula `X_C = 1/(2π*f*C)`, where `f` – frequency in hertz, and `C` – capacitance in farads. Because frequency is in the denominator, for an unchanged capacitance the reactance is inversely proportional to frequency: doubling the frequency halves `X_C`.[^aac-capacitor-reactance-precise]

The reason relates to the relationship between current and voltage change across a capacitor. At higher frequencies, voltage changes more rapidly, so the capacitor can conduct a larger alternating current for the same voltage amplitude. For ideal DC, when frequency is zero after the transient process, the capacitor behaves as an open circuit; a real component has leakage and parasitic effects.[^aac-capacitor-reactance-precise]

For comparison, inductive reactance `X_L = 2π*f*L` increases with frequency, so ideal C and L have opposite frequency dependencies. For example, if the frequency of a sine wave is doubled, `X_C` is halved, and `X_L` is doubled for unchanged `C` and `L`. The reactances of both components are measured in ohms, but they are not resistive losses.[^aac-capacitor-reactance-precise]

One cannot draw a universal conclusion that "a capacitor passes HF" from the formula alone. Actual signal transmission depends on the topology, source, and load: in a series RC circuit and a parallel connection, the component's function is different. At very high frequencies, parasitic inductance and resistance also disrupt the ideal model.

**Common mistake:** Confusing a component's low `X_C` with guaranteed signal passage through any circuit.

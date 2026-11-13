---
id: emb-elee-0042
title: "How does a real inductor differ from an ideal one?"
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
---

## Short answer

A physical inductor exhibits winding resistance that causes conduction losses, along with inter-turn parasitic capacitance that forms a self-resonant frequency with the inductance. Near and above this frequency, the component ceases to behave as a simple inductor; in coils with magnetic cores, inductance can also drop sharply near saturation.[^aac-alternating-current]

## Detailed explanation

An ideal inductor is modeled as a lossless inductance free of parasitic parameters. A physical component additionally exhibits winding resistance, core losses, and inter-turn parasitic capacitance. As a result, its behavior depends on frequency, temperature, current amplitude, and specific physical construction.[^aac-alternating-current]

Wire resistance produces a voltage drop and heating, so a physical coil dissipates active power. At high frequencies, parasitic capacitance becomes significant. Together with the inductance, it forms the coil's self-resonance; below resonance the component typically behaves predominantly inductively, whereas near and above resonance the simple model `X_L = 2*pi*f*L` is no longer sufficient. The exact self-resonant frequency (SRF) must be obtained from the component datasheet.[^aac-alternating-current]

In a coil with a ferromagnetic core, excessive current can drive the core toward saturation. Under saturation, permeability and differential inductance drop, allowing current to rise much more steeply for a given voltage. This does not mean that every coil contains a magnetic core or that saturation occurs at a universal threshold: an air-core coil does not suffer core saturation, and saturation limits depend on core geometry, material, air gap, and operating temperature.[^aac-alternating-current]

Example: in a power supply filter, winding temperature rise depends on winding resistance and RMS current, while inductance shift under load can alter ripple voltage. When selecting a component, one must verify not only nominal inductance, but also rated current, winding resistance, and frequency characteristics from the datasheet.[^aac-alternating-current]

**Common mistakes:**

- Treating a physical inductor as an ideal short circuit at DC: once the transient completes, inductive voltage is near zero, but winding resistance remains.
- Assuming any high current proves core saturation. The current level must be evaluated against core characteristics and datasheet limits.
- Describing a coil simply as a capacitor at all frequencies above SRF; high-frequency behavior is more complex, and SRF is a parameter specific to each individual component.[^aac-alternating-current]

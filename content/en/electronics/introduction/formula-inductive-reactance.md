---
id: emb-elintro-0139
title: "What is the formula for inductive reactance `X_L`?"
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
  - source_id: aac-inductor-reactance-precise
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
---

## Short answer

For an ideal inductor in sinusoidal AC, inductive reactance is `X_L = 2π*f*L`, measured in ohms and increasing with frequency. This is a reactance, not ordinary resistance; a real coil has losses and parasitic parameters.[^aac-inductor-reactance-precise]

## Detailed explanation

The inductive reactance of an ideal coil in steady-state sinusoidal AC equals `X_L = 2π*f*L`, where `f` – frequency in hertz, and `L` – inductance in henries. The result is measured in ohms. The factor `2π*f` is the angular frequency, so for an unchanging inductance, reactance is directly proportional to frequency.[^aac-inductor-reactance-precise]

The physical relationship stems from inductor behavior: it creates a voltage proportional to the rate of change of current. A higher-frequency sine wave changes faster, so it requires a larger voltage across the same inductance and current amplitude. In the purely ideal case with direct current, `f = 0`, so the inductive reactance is zero; this does not account for the wire resistance of a real winding.[^aac-inductor-reactance-precise]

Example: for `L = 10 mH = 0.01 H` at a frequency of `1 kHz`, the reactance is approximately `2π*1000*0.01 ≈ 62.8 Ω`. This does not mean that the coil is a 62.8 Ω resistor: reactance is associated with phase shift and energy exchange with the field. In a mixed circuit, current is determined by total impedance, which also accounts for resistive components.[^aac-inductor-reactance-precise]

The formula describes an ideal model. A real coil has winding resistance, parasitic capacitance, and core losses; near and above the self-resonant frequency, the behavior can deviate from a simple increase in `X_L`.

**Common mistake:** Substituting frequency in kilohertz as a number without converting to hertz, or calling `X_L` the ohmic resistance of the coil.

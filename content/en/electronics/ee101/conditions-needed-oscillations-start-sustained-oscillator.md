---
id: emb-elee-0248
title: "Which conditions are needed for oscillations to start and be sustained in an oscillator?"
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
  - source_id: libretexts-fiore-oscillators
    title: "Fiore: Operational Amplifiers and Linear Integrated Circuits, 9.4 Summary (Oscillators and Frequency Generators)"
    url: https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/09%3A_Oscillators_and_Frequency_Generators/9.4%3A_Summary
---

## Short answer

In steady state, the Barkhausen criterion requires `|A*beta| ≈ 1` and loop phase shift of an integer multiple of 360°; startup requires `|A*beta| > 1` so small perturbations grow.[^libretexts-fiore-oscillators] To compress the loop gain back to unity as amplitude builds, a non-linear limiting element such as a diode or incandescent bulb is placed in the negative feedback network.[^libretexts-fiore-oscillators] Here `beta` denotes the feedback factor rather than BJT current gain.

## Detailed explanation

An oscillator is an amplifier with positive feedback, in which part of the output signal is returned to the input. The loop is described by the product of gain `A` and feedback factor `beta`, namely `A*beta`. The Barkhausen criterion requires the loop phase shift to be 0° or an integer multiple of 360°, and the loop gain product to remain equal to unity to sustain oscillations.[^libretexts-fiore-oscillators] The signal traveling around the loop then returns with the same phase and amplitude, allowing oscillations to be sustained.

Startup requires a gain greater than unity: at `|A*beta| > 1`, each pass around the loop increases the amplitude, causing a small perturbation, such as power-on noise, to grow.[^libretexts-fiore-oscillators] The amplitude cannot grow indefinitely. Therefore, a limiting element, such as a diode or a lamp, is placed in the negative feedback network to reduce the gain back to unity.[^libretexts-fiore-oscillators] Steady-state oscillation is a condition where non-linearity holds `|A*beta|` near unity.

The phase condition selects the frequency at which the loop closes, and the precision of this frequency is determined by the network components. In op-amp RC oscillators, the frequency is set by an RC network, and precision depends on the tolerances of these components and, to a lesser extent, on the amplifier itself.[^libretexts-fiore-oscillators]

Example: let `|A*beta| = 1.02` and the initial perturbation be 1 mV. After `n` passes, the amplitude equals `1 mV * 1.02^n`. For it to reach 1 V, `n = ln(1000)/ln(1.02) ≈ 349` passes are required: `1.02^348 ≈ 984`, while `1.02^349 ≈ 1003`. If instead `|A*beta| = 0.98`, after 349 passes the amplitude will be `1 mV * 0.98^349 ≈ 0.87 µV`, meaning oscillations decay. The numbers are illustrative, as delays in a real loop are omitted.

**Common mistakes:**

- Relying only on `|A*beta| = 1`: startup requires `|A*beta| > 1`;[^libretexts-fiore-oscillators]
- Confusing `beta` with the BJT current gain: here it represents the feedback factor;
- Assuming that the Barkhausen criterion specifies the exact frequency: accuracy is determined by network components, such as the RC network.[^libretexts-fiore-oscillators]

---
id: emb-elee-0040
title: "What does an inductor's reactance `X_L` depend on?"
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

For a sinusoidal signal, an ideal inductor has reactance `X_L = 2*pi*f*L`, which increases proportionally with frequency `f` and inductance `L`. In steady-state DC with `f = 0`, its ideal `X_L` equals zero; practical windings retain non-zero wire resistance.[^aac-alternating-current]

## Detailed explanation

Inductive reactance describes how an ideal inductance opposes sinusoidal alternating current. It is not an ordinary resistance where active power is dissipated as heat: for an ideal inductor, voltage leads current by a quarter cycle (90°), and energy is cyclically exchanged between the source and the magnetic field.[^aac-alternating-current]

The formula `X_L = 2*pi*f*L` applies to the sinusoidal steady state of a linear inductor with constant inductance. Frequency is measured in hertz, inductance in henries, and the resulting reactance in ohms. Doubling `f` or `L` doubles `X_L`, all else being equal. For non-sinusoidal waveforms, harmonic components occur at different frequencies and therefore encounter different reactive impedances.[^aac-alternating-current]

Example: for an ideal inductor with `L = 10 mH` at frequency `f = 1 kHz`, `X_L = 2*pi*1000*0.01 ≈ 62.8 Ω`. This value alone does not determine current: the applied voltage and remaining circuit impedance are also required. In steady-state DC, current no longer changes, so the ideal inductive voltage component equals zero; the wire resistance of a physical coil remains.[^aac-alternating-current]

**Common mistakes:**

- Calling `X_L` winding resistance and attributing heat dissipation to it. Heat is associated with wire resistance and core losses.
- Applying the formula without confirming signal frequency, steady-state operation, and the assumption of constant `L`.
- Extending the monotonic increase of `X_L` to frequencies above the physical coil's self-resonant frequency: parasitic capacitance alters component behavior.[^aac-alternating-current]

---
id: emb-elee-0061
title: "How do X_C and X_L change at DC and as frequency increases?"
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
  - source_id: aac-capacitor-reactance
    title: "All About Circuits: AC Capacitor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-4/ac-capacitor-circuits/
  - source_id: aac-inductor-reactance
    title: "All About Circuits: AC Inductor Circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  - source_id: aac-inductor-quirks
    title: "All About Circuits: Inductor Quirks"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/inductor-quirks/
---

## Short answer

In an ideal model at DC after transients settle, a capacitor has infinite `X_C` and an inductor has zero `X_L`. For a sinusoidal signal, `X_C = 1/(2π*f*C)` decreases with increasing frequency, whereas `X_L = 2π*f*L` increases.[^aac-capacitor-reactance] Real components do not become ideal short circuits or open circuits, as parasitic parameters alter their behavior, especially near self-resonance.[^aac-inductor-quirks]

## Detailed explanation

For ideal components, capacitive reactance is defined as `X_C = 1/(2π*f*C)`, and inductive reactance as `X_L = 2π*f*L`. Consequently, as frequency increases, `X_C` decreases and `X_L` increases; this describes sinusoidal steady state rather than an arbitrary signal or a physical component at any arbitrary frequency.[^aac-capacitor-reactance] [^aac-inductor-reactance]

At zero frequency, that is, for steady-state DC, the ideal capacitor formula yields infinite reactance, while the ideal inductor formula yields zero. In circuit approximations, this is often termed an open circuit for a capacitor and a short circuit for an inductor. This does not describe the transient charging of a capacitor or current buildup in an inductor after switching: during transients, voltages and currents vary dynamically.[^aac-capacitor-reactance] [^aac-inductor-reactance]

**Common mistake:** applying the limits of ideal formulas to physical components and assuming that at very high frequencies a capacitor is always a short circuit and an inductor is an open circuit. A real inductor has winding resistance, parasitic capacitance, and losses; parasitic elements can alter the nature of the impedance beyond self-resonance. Therefore, a high-frequency model is chosen based on the operating frequency band and the specific component datasheet.[^aac-inductor-quirks]

For example, for an ideal inductor with constant `L`, doubling the frequency doubles `X_L`; for an ideal capacitor with constant `C`, it halves `X_C`. This comparison holds only within the range of validity of the lumped ideal model.[^aac-capacitor-reactance] [^aac-inductor-reactance]

The pitfall appears when choosing a filter or interpreting measurements at very high frequencies using these asymptotes: the ideal reactance calculation may cease to agree with the physical component. To avoid errors, distinguish DC steady state from transient processes, and for high frequencies verify parasitic parameters and the component's self-resonant frequency.[^aac-inductor-quirks]

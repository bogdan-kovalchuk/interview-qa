---
id: emb-elintro-0005
title: What is the function of an inductor?
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
  - source_id: aac-inductor
    title: "All About Circuits: AC inductor circuits"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  - source_id: aac-inductor-calculus
    title: "All About Circuits: Inductor voltage and current relationship"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
  - source_id: aac-inductor-practical
    title: "All About Circuits: Practical considerations for inductors"
    url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/practical-considerations-inductors/
---

## Short answer

An inductor stores energy in a magnetic field and opposes changes in current. For an ideal inductor `v = L*di/dt`; its sinusoidal reactance is `X_L = 2π*f*L`, increasing with frequency within the model’s valid range. A real winding also has resistance and parasitic effects. [^aac-inductor]

## Detailed explanation

A changing current produces a voltage across an inductor. With an applied voltage, current changes at a rate determined by inductance; the component does not generally block all current. Under ideal steady DC, current is constant and inductive voltage is zero. A real winding still produces a resistive voltage drop. [^aac-inductor] [^aac-inductor-calculus]

For a calculated sinusoidal example, 10 mH at 1 kHz has `X_L = 2π*1000*0.01 ≈ 62.8 Ω`. This is reactance, not dissipative resistance; phase must be included when combining it with other impedances. The stored magnetic energy in the ideal linear model is `E = L*I²/2`.

Inductors are useful in filters and switching converters because they retain energy while current changes. Opening a path carrying inductor current can generate a large voltage, so a suitable discharge or clamp path matters. Do not extend the simple increasing-reactance rule beyond the component’s self-resonant region: parasitic capacitance, winding loss and core saturation can invalidate the ideal model. [^aac-inductor-practical] [^aac-inductor-calculus]

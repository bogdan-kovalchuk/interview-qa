---
id: emb-elintro-0005
title: What is the function of an inductor?
description: What is the function of an inductor?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: DC circuits, Ohm''s law, Kirchhoff''s laws, sources and
    measurement; specific component values and circuits of the course can differ.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors
    and power supplies; specific component values and circuits of the course can differ.'
- source_id: aac-inductor
  title: 'All About Circuits: AC inductor circuits'
  url: https://www.allaboutcircuits.com/textbook/alternating-current/chpt-3/ac-inductor-circuits/
  accessed: 2026-10-04
  kind: book
  version: null
  applicability: Ideal inductive reactance and frequency dependence.
- source_id: aac-inductor-calculus
  title: 'All About Circuits: Inductor voltage and current relationship'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/inductors-and-calculus/
  accessed: '2026-10-04'
  kind: book
  version: null
  applicability: Voltage/current derivative, steady DC and response to opening an inductive current path.
- source_id: aac-inductor-practical
  title: 'All About Circuits: Practical considerations for inductors'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-15/practical-considerations-inductors/
  accessed: '2026-10-04'
  kind: book
  version: null
  applicability: Winding resistance, saturation, stray capacitance and self-resonance limitations.
---

## Short answer

An inductor stores energy in a magnetic field and opposes changes in current. For an ideal inductor `v = L*di/dt`; its sinusoidal reactance is `X_L = 2π*f*L`, increasing with frequency within the model’s valid range. A real winding also has resistance and parasitic effects. [^aac-inductor]

## Detailed explanation

A changing current produces a voltage across an inductor. With an applied voltage, current changes at a rate determined by inductance; the component does not generally block all current. Under ideal steady DC, current is constant and inductive voltage is zero. A real winding still produces a resistive voltage drop. [^aac-inductor] [^aac-inductor-calculus]

For a calculated sinusoidal example, 10 mH at 1 kHz has `X_L = 2π*1000*0.01 ≈ 62.8 Ω`. This is reactance, not dissipative resistance; phase must be included when combining it with other impedances. The stored magnetic energy in the ideal linear model is `E = L*I²/2`.

Inductors are useful in filters and switching converters because they retain energy while current changes. Opening a path carrying inductor current can generate a large voltage, so a suitable discharge or clamp path matters. Do not extend the simple increasing-reactance rule beyond the component’s self-resonant region: parasitic capacitance, winding loss and core saturation can invalidate the ideal model. [^aac-inductor-practical] [^aac-inductor-calculus]

## Sources

<!-- generated from frontmatter -->

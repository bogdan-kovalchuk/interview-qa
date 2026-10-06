---
id: emb-elee-0122
title: "How does changing R affect the cutoff frequency of RC and RL filters?"
description: "How does changing R affect the cutoff frequency of RC and RL filters?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: udemy-electronics-course
    title: "Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards"
    url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
    accessed: 2026-09-27
    kind: community
    version: null
    applicability: "Question origin: lecture 53 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
  - source_id: aac-alternating-current
    title: "All About Circuits textbook, Volume II: AC"
    url: https://www.allaboutcircuits.com/textbook/alternating-current/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: AC circuits, reactance, phasors, impedance, filters and transformers; specific component values and circuits of the course can differ."
  - source_id: aac-semiconductors
    title: "All About Circuits textbook, Volume III: Semiconductors"
    url: https://www.allaboutcircuits.com/textbook/semiconductors/
    accessed: 2026-09-27
    kind: book
    version: null
    applicability: "Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors and power supplies; specific component values and circuits of the course can differ."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Section 1.5: the voltage across an ideal inductor leads the current by 90 degrees, reactance `X_L = j*2*pi*f*L`. Section 10.3: for an RC lead network the break frequency is 3 dB below the midband level, `f_c = 1/(2*pi*R*C)`, and the output phase is +90 degrees at low frequencies and +45 degrees at the critical frequency. It does not treat the RL filter separately: the RL relations here are derived from the same voltage-divider formulas."
  - source_id: kuphaldt-low-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.2 Low-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.02:_Low-pass_Filters
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The cutoff of a low-pass filter is the frequency above which the output falls below 70.7% of the input; for an RC low-pass it is the frequency where the reactance equals the resistance R; the filter response also depends on the load resistance; inductors have significant resistive losses (wire, core). The readable page text has no RL cutoff formula (only in figures), so it is derived separately."
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Equivalent circuit of a real inductor: an ideal inductance, a series winding resistance `R_s` and a parallel parasitic capacitance `C_d`; a practical inductor is usable only below its self-resonant frequency, and skin effect raises the winding resistance. A general model, not the parameters of any specific coil from the course."
---

## Short answer

TODO

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

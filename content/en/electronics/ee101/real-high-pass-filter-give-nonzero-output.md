---
id: emb-elee-0121
title: "Why does a real RL high-pass filter give a nonzero output at DC and not pass \"any\" high frequency?"
description: "Why does a real RL high-pass filter give a nonzero output at DC and not pass \"any\" high frequency?"
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
  - source_id: kuphaldt-high-pass-filters
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 9.3 High-pass Filters (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/09:_Filters/9.03:_High-pass_Filters
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Inductive high-pass filter: a series resistor and an inductor in parallel with the load (output taken across the inductor); the cutoff is where the output equals 70.7% of the input; at high frequencies inductors behave unexpectedly because of skin effect and core losses. The readable page text has no RL formulas (they appear only in figures), so they are derived separately here."
  - source_id: fontys-passive-hf
    title: "Fontys University of Applied Sciences: 1.2 Passive components at high frequency (LibreTexts)"
    url: https://eng.libretexts.org/Courses/Fontys_University_of_Applied_Sciences/Telecommunications/01:_Passive_Components/1.02:_Passive_components_at_high_frequency
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Equivalent circuit of a real inductor: an ideal inductance, a series winding resistance `R_s` and a parallel parasitic capacitance `C_d`; a practical inductor is usable only below its self-resonant frequency, and skin effect raises the winding resistance. A general model, not the parameters of any specific coil from the course."
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Probes and oscilloscopes have a limited bandwidth (the signal is down by 3 dB at the bandwidth limit; a bandwidth margin of 3 to 5 times is advised for accurate amplitudes), and a probe loads the source, in particular with its tip capacitance, which lowers the system bandwidth. General statements, not specific instrument models from the course."
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
    accessed: 2026-10-06
    kind: official
    version: "VMN-SG2139-1203"
    applicability: "Defines DCR, SRF and distributed capacitance of an inductor: above SRF the capacitive reactance dominates, and lower distributed capacitance for a given inductance gives a higher SRF. It gives no numbers for the course inductor; take them from the datasheet of the actual part."
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

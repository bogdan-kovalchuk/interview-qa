---
id: emb-elee-0230
title: "How do you calculate the lower cutoff frequency of an audio stage's coupling capacitor?"
description: "How do you calculate the lower cutoff frequency of an audio stage's coupling capacitor?"
track: electronics
section: ee101
level: junior
type: concept
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Question origin: lecture 75 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
    accessed: 2026-10-14
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Open-license textbook (Creative Commons), lead network section (chapter 10): an RC network with the output across R is a high-pass filter; f_c = 1/(2*pi*R*C) is the frequency at which the signal drops by 3 dB; loss A'v = -10*log10(1+(f_c/f)^2) (example 10.13); X_C = 1/(2*pi*f*C). Formulas for a single RC network."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 7.3: coupling capacitors act as opens for DC and as shorts for the signal when their reactance is much smaller than the surrounding resistances; A_v = -r_C/(r'_e + r_E) has a minus sign (inversion, 180 degree phase shift); Z_out ≈ R_C when R_C is much smaller than r'_C; with a load A_divider = R_L/(R_L + R_C) (example 7.1)."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

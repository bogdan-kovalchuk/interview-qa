---
id: emb-elee-0207
title: "Which resistance sets the cutoff of a coupling capacitor between two stages?"
description: "Which resistance sets the cutoff of a coupling capacitor between two stages?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Question origin: lecture 70 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-multi-stage-amplifiers
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.6 Multi-Stage Amplifiers"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.6:_Multi-Stage_Amplifiers"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 7.6: the Z_in of the next stage is the load of the previous stage; system Z_in is that of the first stage and Z_out that of the last; the interstage capacitor blocks DC between stages. No cutoff formula is given here."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 7.3: A_v = -r_C/(r'_e + r_E), with the minus sign as the 180 degree inversion in the midband; Z_in(base) = β(r'_e + r_E); Z_out ≈ R_C; an unbypassed (swamping) R_E lowers gain and distortion and raises input impedance; the numerical examples apply only to those circuits."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 10.3 (Bode plots): RC network with the output taken across R and a series C; f_c = 1/(2*pi*R*C), with the gain at the break 3 dB below midband; the lower break comes from coupling and stray capacitances; below f_c the lead network response falls at 6 dB per octave."
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

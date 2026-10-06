---
id: emb-elee-0173
title: "What are the basic relations of an ideal transformer and what does its VA rating mean?"
description: "What are the basic relations of an ideal transformer and what does its VA rating mean?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Question origin: lecture 64 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The instantaneous voltage across a coil equals its number of turns times the rate of change of the flux linking it; the common core flux induces a voltage in the secondary winding (mutual inductance). An idealized treatment without losses."
  - source_id: kuphaldt-transformer-ratios
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.2 Step-up and Step-down Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.02:_Step-up_and_Step-down_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The voltage and current transformation ratio equals the ratio of winding turns, voltage and current are stepped in opposite directions because a transformer only converts power and does not produce it; the turns ratio equals the square root of the inductance ratio. A 10:1 SPICE example; losses are not included."
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Transformer ratings by winding voltage and VA (the current is derived from the VA); the example of 120 V / 48 V, 1 kVA; the efficiency of modern power transformers typically exceeds 95 %, losses in the windings and core, and leakage inductance lowers the secondary voltage as current grows. A general teaching text."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Section 3.2.2: ideally the voltage scales with the turns ratio and the current inversely, with no loss in the transformer; the VA rating is the product of the nominal secondary voltage and the maximum allowed secondary current; section 3.2.3: with a capacitor after the rectifier the diode current has short peaks; section 3.2.4: an example of 24 V * 0.3 A = 7.2 VA as a minimum. A teaching treatment, not a standard."
  - source_id: fiore-ac-apparent-power
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (section 7.2, Power Waveforms)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-06
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Section 7.2: apparent power S has the unit volt-ampere (VA) and is the product of the voltmeter and ammeter readings; without the phase angle between voltage and current it does not equal the real power in watts."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

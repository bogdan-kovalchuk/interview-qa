---
id: emb-elee-0172
title: "What does offline power mean and what does a mains transformer do?"
description: "What does offline power mean and what does a mains transformer do?"
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
  - source_id: ti-an556
    title: "Texas Instruments AN-556 (SNVA006B): Introduction to Power Supplies"
    url: https://www.ti.com/lit/an/snva006b/snva006b.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNVA006B, May 2004"
    applicability: "The functions of a mains-powered supply (rectification, voltage transformation, filtering, regulation, isolation, protection); a linear supply with a 50/60 Hz transformer, rectifier, capacitor and regulator; the meaning of off-line (the DC voltage to the switch is developed right from the AC line), the mandatory isolation in off-line converters on 110/220 V mains provided by a transformer, and the smaller size of a high-frequency transformer. A 2004 overview; the specific circuits and power levels are not a standard."
  - source_id: kuphaldt-transformer-operation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.1 Mutual Inductance and Basic Operation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.01:_Mutual_Inductance_and_Basic_Operation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "How a transformer works: alternating current changes the flux in a common core, and the changing flux induces a voltage in the secondary winding (mutual inductance). An idealized treatment without losses."
  - source_id: kuphaldt-transformer-isolation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.3 Electrical Isolation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.03:_Electrical_Isolation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A transformer transfers power between circuits without a conductive connection (electrical isolation), and a common-mode voltage on the secondary circuit is not impressed on the primary; isolation transformers have a 1:1 ratio. This is a SPICE-based model, not a safety standard."
  - source_id: kuphaldt-transformer-practical
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.8 Practical Considerations – Transformers (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.08:_Practical_Considerations_-_Transformers
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Transformer ratings by winding voltage and VA (the current is derived from the VA); the example of 120 V / 48 V, 1 kVA; the windings must be insulated well enough from each other to maintain electrical isolation; core saturation at a lowered frequency (50 instead of 60 Hz). A general teaching text."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

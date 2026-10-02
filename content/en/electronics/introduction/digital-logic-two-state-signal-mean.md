---
id: emb-elintro-0016
title: What does "digital logic is a two-state signal" mean?
description: What does "digital logic is a two-state signal" mean?
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
  applicability: 'Historical question provenance: lecture 4 of the Udemy course. Original flashcards remain in imports.
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
- source_id: ti-hc00
  title: TI SN74HC00 quadruple NAND gates datasheet
  url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
  accessed: 2026-10-04
  kind: official
  version: SCLS181H
  applicability: Section 6.3 input thresholds; switching characteristics and PDIP/SOIC package drawings.
---

## Short answer

Two-state digital logic interprets a signal as LOW or HIGH, conventionally representing 0 or 1 in positive logic. These states are voltage ranges defined by input thresholds, not necessarily exact 0 V and supply voltage. Intermediate voltages may have no guaranteed logical interpretation. [^ti-hc00]

## Detailed explanation

A binary state is an interpretation of the input voltage by a receiver. Real outputs may sit above ground for LOW or below the supply for HIGH, especially under load. What matters is that the output levels meet the receiving device’s specified input limits. Different logic families can have different limits. [^ti-hc00]

For the TI SN74HC00 at `V_CC = 4.5 V`, section 6.3 specifies `V_IL(max) = 1.35 V` and `V_IH(min) = 3.15 V`. Within the specified input-voltage range, a level at or below 1.35 V is accepted as LOW and at or above 3.15 V as HIGH. The interval between them is not guaranteed as either. These numbers belong to this device and supply condition. [^ti-hc00]

Thus 1 V and 4 V can encode the two states in this example without being ideal rail voltages. Logic-level compatibility requires comparing transmitter output specifications with receiver input thresholds. A supply label such as 3.3 V is not sufficient on its own.

## Sources

<!-- generated from frontmatter -->

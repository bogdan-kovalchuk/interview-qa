---
id: emb-elintro-0007
title: How do you identify a diode's cathode from its package?
description: How do you identify a diode's cathode from its package?
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
- source_id: vishay-diode
  title: Vishay 1N4001-1N4007 rectifier datasheet
  url: https://www.vishay.com/docs/88503/1n4001.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Cathode band, reverse-voltage ratings and temperature-dependent reverse leakage.
---

## Short answer

On common axial rectifier diodes, a band near one end identifies the cathode; the other end is the anode. This is a package convention, not a rule for every diode package, so confirm the marking and pinout in the datasheet. [^vishay-diode]

## Detailed explanation

The Vishay 1N4001-1N4007 DO-41 family explicitly specifies a color band for the cathode. With that device in hand, the band identifies one terminal regardless of how the body is rotated. Do not identify a diode terminal by an assumed color of the lead itself. [^vishay-diode]

Package markings and schematic symbols solve different tasks: the body marking locates the physical terminal; the symbol names its electrical role. Conventional forward current travels from anode to cathode when the diode is forward biased. The band does not mean that current enters that end.

For SMD devices, multi-diode packages and LEDs, obtain the exact part’s pinout rather than copying the axial rule. A multimeter diode test can help confirm a simple isolated junction, but parallel paths in a populated circuit can affect the reading. A package drawing remains the reference for assembly orientation.

## Sources

<!-- generated from frontmatter -->

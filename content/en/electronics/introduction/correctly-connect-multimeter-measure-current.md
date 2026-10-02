---
id: emb-elintro-0014
title: How do you correctly connect a multimeter to measure current?
description: How do you correctly connect a multimeter to measure current?
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
- source_id: fluke-meter
  title: Fluke 3000 FC Users Manual
  url: https://media.fluke.com/437e18a0-de4d-4090-ab8a-b0df016de4fd_original%20file.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Functions, terminals and power-off/series/current-measurement procedure, printed page 17.
---

## Short answer

Turn off circuit power, select the correct current function, rated input jack and range, then open the branch and insert the meter in series. Restore power only after connection; turn it off again before disconnecting. Never place a meter in current mode directly across a voltage source. [^fluke-meter]

## Detailed explanation

Current measurement routes the branch current through the meter’s internal current-measurement path. Therefore the meter must be in series with the branch being measured. In contrast, a voltage measurement places a high-impedance input across two nodes. Confusing these connections can short the source through the current input. [^fluke-meter]

The Fluke procedure explicitly says to remove power, break the circuit, connect in series and then restore power. Select AC or DC as applicable and use the function, terminal and range rated for the expected current. Do not assume every meter has a 10 A input: the cited 3000 FC meter has specified mA measurement ranges. The actual meter’s manual controls its limits. [^fluke-meter]

The inserted meter can change the circuit through its burden voltage; the measured current need not be exactly the original undisturbed current. After measurement, remove power before restoring the circuit, and return the lead to the voltage/resistance jack for those functions. Verify the wiring and input rating before the next measurement.

## Sources

<!-- generated from frontmatter -->

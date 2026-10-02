---
id: emb-elintro-0015
title: What is the function of a multimeter – what does it measure?
description: What is the function of a multimeter – what does it measure?
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

A multimeter combines voltage, current and resistance measurement; many models also offer continuity, diode test, capacitance or frequency. Available functions, terminals, ranges and limits depend on the model. Use the correct function and connection for each measurement. [^fluke-meter]

## Detailed explanation

Voltage is measured across two nodes; current is measured in series in a branch. Resistance is measured by applying the meter’s test stimulus, so disconnect circuit power and discharge capacitors before a resistance measurement. The same display can show very different quantities because the meter switches its input circuitry between functions. [^fluke-meter]

Continuity is a threshold-based convenience indication, not a precision resistance measurement. Diode test reports a junction voltage under the meter’s test conditions, not the diode’s maximum current or complete datasheet characteristics. Capacitance and frequency are examples of optional capabilities: consult the actual manual rather than assuming every instrument supports them. [^fluke-meter]

Auto-ranging can choose a measurement range but cannot correct a wrong function, lead jack or unsafe connection. Measurement resolution is also different from accuracy: a display with more digits does not automatically measure more accurately. For a meaningful result, check the specified accuracy, input impedance, permitted waveform and rating for the intended use.

## Sources

<!-- generated from frontmatter -->

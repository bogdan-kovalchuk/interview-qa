---
id: emb-elintro-0003
title: What is the function of a resistor in a circuit?
description: What is the function of a resistor in a circuit?
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
- source_id: aac-resistors
  title: 'All About Circuits: Resistors'
  url: https://www.allaboutcircuits.com/textbook/direct-current/chpt-2/resistors/
  accessed: 2026-10-04
  kind: book
  version: null
  applicability: Resistance, voltage/current relationship and dissipation.
---

## Short answer

A resistor relates voltage and current through resistance: for an ideal ohmic resistor, `V = I*R`. It limits current, forms voltage dividers and dissipates electrical energy as heat, within its power rating. [^aac-resistors]

## Detailed explanation

Resistance is not a fixed voltage drop: the drop depends on current. Conversely, a fixed applied voltage produces less current when resistance increases. A resistor does not consume charge; it transfers electrical energy into heat. Use `P = V*I = I²*R = V²/R` for the ideal resistive model. [^aac-resistors]

For a calculated example, 5 V across 1 kΩ gives `I = 5/1000 = 5 mA` and `P = 25 mW`. That result is for the voltage across the resistor, not automatically the whole supply voltage if other series components are present.

For an LED with an assumed 2 V forward drop on a 5 V supply, a 220 Ω series resistor gives approximately `(5-2)/220 = 13.6 mA`; resistor dissipation is about 41 mW. This is a worked model, not a universal LED design: verify actual forward voltage, allowable LED current, resistor tolerance and rated power. Real resistance can also vary with temperature.

## Sources

<!-- generated from frontmatter -->

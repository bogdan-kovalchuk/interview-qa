---
id: emb-elintro-0009
title: What do the 4 bands on a resistor mean?
description: What do the 4 bands on a resistor mean?
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
- source_id: vishay-colors
  title: Vishay resistor color code chart
  url: https://www.vishay.com/docs/49411/resistor_color_code_calculator.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Four/five band digits, multipliers and tolerances.
---

## Short answer

In a four-band resistor code, two bands give significant digits, the third a multiplier and the fourth tolerance. Brown-black-red-gold means `10 × 100 = 1000 Ω` with ±5% tolerance; multipliers can also be fractional. [^vishay-colors]

## Detailed explanation

Read a four-band code from the digit end toward the tolerance band, which is commonly separated by a larger gap. Brown is 1 and black is 0, so the significant number is 10, not the decimal number 1.0. Red multiplies by 100; gold specifies ±5%. [^vishay-colors]

The nominal value is therefore 1 kΩ. A calculated tolerance interval is `1000*(1-0.05)` through `1000*(1+0.05)`, or 950–1050 Ω under the tolerance specification’s conditions. It does not promise that temperature or aging can never change resistance beyond an initial tolerance interval.

Gold used as a multiplier means 0.1 and silver means 0.01, so describing multipliers only as “adding zeros” is incomplete. A five-band code uses three significant digits followed by multiplier and tolerance. First identify the code format; a color’s role depends on its band position. [^vishay-colors]

## Sources

<!-- generated from frontmatter -->

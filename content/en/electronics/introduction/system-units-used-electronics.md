---
id: emb-elintro-0020
title: Which system of units is used in electronics?
description: Which system of units is used in electronics?
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
- source_id: bipm-si
  title: 'BIPM: The International System of Units, SI Brochure'
  url: https://www.bipm.org/documents/20126/41483022/SI-Brochure-9.pdf
  accessed: 2026-10-04
  kind: official
  version: 9th edition, version 4.01
  applicability: SI base units, named derived units and decimal prefixes.
---

## Short answer

Electronics uses SI: base units include the second, metre, kilogram and ampere; volt, ohm, farad, henry, coulomb, joule, watt and hertz are derived units. Decimal prefixes such as milli, micro and kilo scale these units. Unit symbols and prefix case matter. [^bipm-si]

## Detailed explanation

The seven SI base units are second (s), metre (m), kilogram (kg), ampere (A), kelvin (K), mole (mol) and candela (cd). Common electrical quantities use SI units: current is in A, voltage in V, resistance in Ω, capacitance in F and inductance in H. Hertz (Hz) expresses frequency as inverse seconds. [^bipm-si]

Unit relationships make equations checkable: `1 C = 1 A*s`, `1 V = 1 J/C`, `1 Ω = 1 V/A`, and `1 W = 1 J/s = 1 V*A`. A number without its unit is insufficient for an electrical quantity. For example, 5 mA and 5 A differ by a factor of 1000. [^bipm-si]

Prefixes denote powers of ten: milli (m) is `10^-3`, micro (µ) is `10^-6`, nano (n) is `10^-9`, kilo (k) is `10^3` and mega (M) is `10^6`. Thus mA and MA differ by a factor of one billion. Write a space between value and unit, as in `10 kΩ`; keep symbol case unchanged when translating prose. [^bipm-si]

## Sources

<!-- generated from frontmatter -->

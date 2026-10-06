---
id: emb-elee-0176
title: "What must be considered when connecting two transformer secondaries?"
description: "What must be considered when connecting two transformer secondaries?"
track: electronics
section: ee101
level: junior
type: pitfall
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
  - source_id: kuphaldt-phasing
    title: "Workforce LibreTexts: Lessons in Electric Circuits, Vol. II (Kuphaldt), 10.4 Phasing"
    url: "https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.04:_Phasing"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The dot convention marks the transformer winding terminals that have the same instantaneous polarity; matching or non-matching dots determine a zero or 180-degree phase shift between windings. The section does not cover series or parallel connection of secondary windings."
  - source_id: esp-transformers-part2
    title: "Elliott Sound Products: Beginners’ Guide to Transformers, Part 2 (section 8, Windings in Series and Parallel)"
    url: https://sound-au.com/xfmr2.htm
    accessed: 2026-10-06
    kind: book
    version: "page updated January 2023"
    applicability: "Series and parallel connection of secondary windings: a 2 x 25 V / 5 A (250 VA) example gives 50 V / 5 A in series or 25 V / 10 A in parallel; in series, in-phase voltages add and out-of-phase voltages subtract without harming the transformer; parallel is acceptable only with equal voltages and in phase, a circulating-current estimate for 0.25 ohm windings, advice to measure the voltages and use a fuse. A practitioner's self-published tutorial, not a standard or a datasheet; the numbers in the examples are illustrative."
  - source_id: hammond-266m20
    title: "Hammond Manufacturing: 266M20 power transformer, dual primary and secondary (datasheet)"
    url: https://www.hammfg.com/files/parts/pdf/266M20.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "For the 266M20 model (60 VA) the manufacturer gives the secondary ratings: series (center-tapped) 20 V / 3 A, parallel 10 V / 6 A, and allows the secondaries to be used center-tapped, in parallel or individually. The values apply to this model only; for other transformers the connection scheme comes from their own datasheet."
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

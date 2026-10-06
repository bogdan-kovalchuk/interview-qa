---
id: emb-elee-0144
title: "What is a Zener diode's dynamic resistance `r_Z`?"
description: "What is a Zener diode's dynamic resistance `r_Z`?"
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
    applicability: "Question origin: lecture 58 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "The real Zener curve in breakdown is not vertical, the dynamic resistance R_dyn = ΔV_Z/ΔI_Z is larger than zero; the differential resistance r_dif = ΔV_Z/ΔI_Z is the steepness of the V_Z–I_Z curve, ideally 0 Ω; a minimum Zener current of about 5 mA for diodes up to 17 V; data are for Nexperia series, other manufacturers can have other numbers."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Maximum r_dif at T_j = 25 °C: for 5.1 V (BZX84-C5V1) 480 Ω at 1 mA and 60 Ω at 5 mA, for 6.2 V 150 Ω at 1 mA and 10 Ω at 5 mA; values for this series, not for all Zener diodes."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

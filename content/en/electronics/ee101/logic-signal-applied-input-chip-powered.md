---
id: emb-elee-0171
title: "Can a 5 V logic signal be applied to the input of a chip powered from 3.3 V?"
description: "Can a 5 V logic signal be applied to the input of a chip powered from 3.3 V?"
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
    applicability: "Question origin: lecture 63 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: ti-hc00
    title: TI SN74HC00 quadruple NAND gates datasheet
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-06
    kind: official
    version: SCLS181H
    applicability: "A standard CMOS input: recommended input voltage 0 to VCC, the input clamp current limit IIK of ±20 mA for VI > VCC + 0.5 V and the note that the voltage ratings may be exceeded if the current ratings are observed, input and output clamp diodes to VCC and GND (section 8.5), VIH(min) of 3.15 V at VCC = 4.5 V. Applies only to the SN74HC00; other devices have other limits."
  - source_id: ti-sn74lvc1g125
    title: "Texas Instruments SN74LVC1G125 datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74lvc1g125.pdf
    accessed: 2026-10-06
    kind: official
    version: "SCES223U, August 2026"
    applicability: "An example of a 5 V-tolerant input: for VCC from 1.65 to 5.5 V the input accepts 0 to 5.5 V, VIH(min) = 2 V at VCC from 3 to 3.6 V and 0.7*VCC at VCC from 4.5 to 5.5 V, Ioff for partial-power-down. Applies only to the SN74LVC1G125; for another device the tolerance must be found in its own datasheet."
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

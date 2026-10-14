---
id: emb-elee-0222
title: "Is one flyback diode enough for a bidirectional H-bridge, and does it remove all motor noise?"
description: "Is one flyback diode enough for a bidirectional H-bridge, and does it remove all motor noise?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-14
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
    applicability: "Question origin: lecture 73 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
  - source_id: ti-slva321a
    title: "Texas Instruments SLVA321A: Current Recirculation and Decay Modes"
    url: https://www.ti.com/lit/an/slva321a/slva321a.pdf
    accessed: 2026-10-14
    kind: official
    version: "SLVA321A, revised April 2021"
    applicability: "TI application report on H-bridges: current in an inductive load needs a safe decay path, either free-wheeling diodes in parallel with the FET switches or synchronous decay; in fast decay the load voltage equals the supply plus two diode drops. Covers TI driver designs; the diodes of a given design differ."
  - source_id: ti-slvae59a
    title: "Texas Instruments SLVAE59A: Using Motor Drivers to Drive Solenoids"
    url: https://www.ti.com/lit/an/slvae59a/slvae59a.pdf
    accessed: 2026-10-14
    kind: official
    version: "SLVAE59A, revised April 2022"
    applicability: "TI application report on solenoids: a diode across an inductive load gives a low-impedance path so that the MOSFET does not see large voltage spikes. About solenoids, not brushed motors; brush noise is not covered."
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

---
id: emb-elee-0126
title: "What causes discrepancies between the calculation and the measurement of an RL filter?"
description: "What causes discrepancies between the calculation and the measurement of an RL filter?"
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
    applicability: "Question origin: lecture 54 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: vishay-inductors-primer
    title: "Vishay: Inductors 101 – Primer Instructional Guide"
    url: https://www.vishay.com/docs/49782/49782.pdf
    accessed: 2026-10-06
    kind: official
    version: "VMN-SG2139-1203"
    applicability: "Defines DCR, SRF and distributed capacitance of an inductor: DCR is the winding resistance with no alternating current, and above SRF the capacitive reactance dominates. It gives no numbers for the course inductor; take them from the datasheet of the actual part."
  - source_id: vishay-ihlp-2525cz-l7
    title: "Vishay Dale: IHLP-2525CZ-L7 inductors datasheet"
    url: https://www.vishay.com/docs/34254/ihlp-2525cz-l7.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 02-Jun-2023"
    applicability: "Datasheet example: inductance tolerance ±20 % (at 100 kHz, 0.25 V, 0 A), DCR with ±5 % tolerance and typical SRF are given as parameters. It applies only to this series of power inductors; for another inductor take the values from its own datasheet."
  - source_id: tektronix-abcs-probes
    title: "Tektronix: ABCs of Probes Primer"
    url: https://download.tek.com/document/02_ABCs-of-Probes-Primer.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Probes and oscilloscopes have a limited bandwidth (the signal is down by 3 dB at the bandwidth limit; a bandwidth margin of 3 to 5 times is advised for accurate amplitudes), and a probe loads the source, in particular with its tip capacitance, which lowers the system bandwidth. General statements, not specific instrument models from the course."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

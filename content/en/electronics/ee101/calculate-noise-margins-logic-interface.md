---
id: emb-elee-0235
title: "How do you calculate the noise margins of a logic interface?"
description: "How do you calculate the noise margins of a logic interface?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Question origin: lecture 76 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
  - source_id: ti-szza036c
    title: "TI SZZA036C: Understanding and Interpreting Standard-Logic Data Sheets"
    url: https://www.ti.com/lit/an/szza036c/szza036c.pdf
    accessed: 2026-10-14
    kind: official
    version: "SZZA036C, revised June 2016"
    applicability: "Figure 50 (Logic Compatibility Between I/Os) labels High Noise Margin between VOH (min) and VIH (min), and Low Noise Margin between VIL (max) and VOL (max); explains how to read these datasheet parameters. Gives no values for specific devices."
  - source_id: ti-hc00
    title: "TI SN74HC00 quadruple NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SCLS181H"
    applicability: "Sections 6.3 and 6.5 (25 °C): VIH and VIL at VCC = 4.5 V; VOH and VOL at IOH and IOL of 20 uA and 4 mA for the 74HC00. CMOS series only, not TTL."
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SDLS025D"
    applicability: "Section 6.5 (SNx400, TTL): VOH (min) 2.4 V at VCC (min) and IOH -0.4 mA; VOL (max) 0.4 V at IOL 16 mA. TTL input levels: VIH 2 V, VIL 0.8 V. Not applicable to CMOS series."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

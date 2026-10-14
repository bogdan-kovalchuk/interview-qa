---
id: emb-elee-0238
title: "Do simple resistor-transistor gates reproduce industrial TTL?"
description: "Do simple resistor-transistor gates reproduce industrial TTL?"
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
  - source_id: ti-sn74ls00
    title: "TI SDLS025D: SNx400, SNx4LS00, SNx4S00 quadruple 2-input NAND gates datasheet"
    url: https://www.ti.com/lit/ds/symlink/sn74ls00.pdf
    accessed: 2026-10-14
    kind: official
    version: "SDLS025D"
    applicability: "Section 6.5 (SNx400, TTL): VOH (min) 2.4 V at IOH -0.4 mA and VOL (max) 0.4 V at IOL 16 mA. Section 11: multiple-emitter inputs in the SN74 and SN74S series. TTL input levels VIH 2 V, VIL 0.8 V. Does not describe RTL."
  - source_id: adi-ttl-lab
    title: "Analog Devices Wiki: TTL inverter and NAND gate activity for ADALM2000"
    url: https://wiki.analog.com/university/courses/electronics/electronics-lab-27
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Vendor lab activity for ADALM2000: a TTL inverter with an input current-steering stage, a phase splitter and a totem-pole output pair that can both source and sink current. Not a datasheet: it gives no guaranteed levels."
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
    accessed: 2026-10-14
    kind: book
    version: "last updated 1996-07-16"
    applicability: "1996 lecture material (section B.2): a resistor as the load (pull-up) and a transistor in place of the lower resistor give an inverter; diode drop about 0.7 V. Gives no parameters of specific devices."
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

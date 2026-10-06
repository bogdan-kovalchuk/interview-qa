---
id: emb-elee-0149
title: "Why is diode logic unsuitable for long chains, and why does it use Schottky diodes?"
description: "Why is diode logic unsuitable for long chains, and why does it use Schottky diodes?"
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
    applicability: "Question origin: lecture 59 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: nexperia-diode-handbook
    title: "Nexperia: Diode Application Handbook (Design Engineer’s Guide), 2022"
    url: https://assets.nexperia.com/documents/brochure/Nexperia_document_book_DiodeApplicationHandbook_2022.pdf
    accessed: 2026-10-06
    kind: official
    version: "2022"
    applicability: "Section 7.4 (Switching diode): simple slow diode OR and AND functions with a resistor (figures 114–117): the diodes decouple the inputs, with a low input the resistor sees V_F, with all inputs high the output is high; section 2: a Schottky diode has a low forward drop, with a trade-off between V_F, leakage current and reverse voltage. General information, not parameters of a specific diode."
  - source_id: utah-cs6710-diode-logic
    title: "Logic Gates from Resistors, Diodes, and Transistors (B.2), handout CS 6710, University of Utah"
    url: https://my.eng.utah.edu/~cs6710/handouts/AppendixB/appendixB.doc2.html
    accessed: 2026-10-06
    kind: book
    version: "last updated 1996-07-16"
    applicability: "A 1996 course lecture handout using a simplified diode model; supplementary source for: diode AND and OR gates with a resistor, a diode drop of “approximately 0.7 V”, drops accumulating when gates are cascaded (five AND gates at 0.7 V give 3.5 V), no inverter possible from diodes and resistors alone. Contains no parameters of specific parts."
  - source_id: vishay-bat54
    title: "Vishay: BAT54, BAT54A, BAT54C, BAT54S small signal Schottky diodes (datasheet)"
    url: https://www.vishay.com/docs/86410/bat54_bat54a_bat54c_bat54s.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 1.1, 21-Feb-2024"
    applicability: "Maximum V_F at 25 °C: 240 mV at 0.1 mA, 320 mV at 1 mA, 400 mV at 10 mA, 800 mV at 100 mA; leakage up to 2 μA at V_R = 25 V; V_BR at least 30 V. Values apply to this small-signal Schottky series, not to all Schottky diodes."
  - source_id: ti-hc00
    title: "TI: SN74HC00, SN54HC00 quadruple 2-input NAND gates (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/sn74hc00.pdf
    accessed: 2026-10-06
    kind: official
    version: "SCLS181H"
    applicability: "Section 6.3 Recommended Operating Conditions: V_IL(max) = 1.35 V and V_IH(min) = 3.15 V at V_CC = 4.5 V; the table has no row for V_CC = 5 V. Values apply to this HC family, other logic families have other thresholds."
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

---
id: emb-elee-0146
title: "How is a diode AND gate built?"
description: "How is a diode AND gate built?"
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
  - source_id: libretexts-fiore-diode-models
    title: "Fiore: Semiconductor Devices, 2.4 Diode Circuit Models (Engineering LibreTexts)"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/02:_PN_Junctions_and_Diodes/2.4:_Diode_Circuit_Models"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Diode models: the 0.7 V knee voltage of silicon as a behavioral approximation, the R_bulk resistance, dynamic resistance of about 26 mV / I. These are simplified models, not exact values for a specific device."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

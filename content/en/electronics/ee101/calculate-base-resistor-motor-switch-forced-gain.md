---
id: emb-elee-0220
title: "How do you calculate the base resistor for a 100 mA motor switch with a forced gain of 10 driven from 5 V?"
description: "How do you calculate the base resistor for a 100 mA motor switch with a forced gain of 10 driven from 5 V?"
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
  - source_id: rohm-bjt-basics
    title: "ROHM: Bipolar Junction Transistor (BJT) Basics: Operation and Applications (NPN & PNP)"
    url: https://techweb.rohm.com/product/transistors-diodes/transistors/27319/
    accessed: 2026-10-14
    kind: official
    version: "2026.02.17"
    applicability: "Manufacturer guide (ROHM): I_B must be at least I_C/β_forced, with β_forced chosen below the datasheet minimum h_FE (common starting point 5–10); for silicon NPN, typical saturation V_BE of 0.7–0.9 V and V_CE below 0.3 V. Values are typical and depend on the device and current; a specific transistor's datasheet takes precedence."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-14
    kind: book
    version: "Spring 2006"
    applicability: "University lecture notes: in saturation the base-collector junction is forward biased and the relation between I_C and I_B is nonlinear. Not a manufacturer document; specific transistors can differ."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

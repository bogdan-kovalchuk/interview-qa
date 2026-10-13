---
id: emb-elee-0195
title: "Why does a 4.7 kΩ load break current stabilization in the same circuit (`V_B` = 1.7 V, `R_E` = 1 kΩ, +5 V)?"
description: "Why does a 4.7 kΩ load break current stabilization in the same circuit (`V_B` = 1.7 V, `R_E` = 1 kΩ, +5 V)?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-13
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
    applicability: "Question origin: lecture 68 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.2: I_E = I_C + I_B, I_C = β·I_B; with I_C much larger than I_B, I_E ≈ I_C; V_BE ≈ 0.7 V for silicon. General picture, not for a specific transistor."
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.3: three collector-curve regions: saturation on the left (V_CE(sat) a few tenths of a volt), nearly constant current in the middle used for linear amplifiers, and breakdown on the right. General picture, not for a specific transistor."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.6: DC load line with the Q point (I_CQ, V_CEQ) on it; if the calculated current exceeds the limit, the transistor is saturated and the real current equals that limit; typical V_CE(sat) about a tenth of a volt, with a 0.15 V example at I_C = 10 mA and I_B = 0.3 mA. Exact values are read from the transistor's graphs."
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

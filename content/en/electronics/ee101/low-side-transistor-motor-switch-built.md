---
id: emb-elee-0218
title: "How is a low-side transistor motor switch built?"
description: "How is a low-side transistor motor switch built?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Question origin: lecture 73 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-bjt-switching
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 4.7.1: the saturating switch – the transistor completes the circuit between the supply, the load and ground; for saturation the ratio of saturation current to base current must be much less than β; direct DC motor drive with a saturating BJT; a diode across the motor winding (snubbing diode) prevents the transistor from being damaged by the voltage spike when it turns off. The example numbers apply only to these circuits."
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook section 4.3: three zones of the collector curves – saturation (left, V_CE(sat) a few tenths of a volt), the nearly constant-current zone used for linear amplifiers in the middle, and breakdown on the right; saturation is used in switching. Section 4.3.1: I_C rises with V_CE; extending the constant-current region gives the Early voltage V_A. General picture, not a specific transistor."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.2: I_E = I_C + I_B, I_C = β·I_B; with I_C much larger than I_B, I_E ≈ I_C; V_BE ≈ 0.7 V for silicon. General picture, not for a specific transistor."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

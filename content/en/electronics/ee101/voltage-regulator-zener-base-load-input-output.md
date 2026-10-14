---
id: emb-elee-0226
title: "Voltage regulator with a 5.6 V Zener on the base, 50 mA load, β ≈ 100, 9 V input. What are the output, the base current and the transistor power?"
description: "Voltage regulator with a 5.6 V Zener on the base, 50 mA load, β ≈ 100, 9 V input. What are the output, the base current and the transistor power?"
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
    applicability: "Question origin: lecture 74 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
  - source_id: vishay-silicon-zener-diodes
    title: "Vishay: Silicon Zener Diodes (application document)"
    url: https://www.vishay.com/docs/84117/84117.pdf
    accessed: 2026-10-14
    kind: official
    version: null
    applicability: "Manufacturer document: a Zener in reverse breakdown as a constant voltage source V_Z0 with a differential resistance; the dynamic resistance rises sharply at very small Zener currents; temperature coefficient α_VZ. Specific V_Z and I_ZT values depend on the type and are not given here."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 4.2: I_E = I_C + I_B, I_C = β·I_B; when I_C is much larger than I_B, I_E ≈ I_C; V_BE ≈ 0.7 V for silicon. General picture, not for a specific transistor."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 4.6: I_C(sat) = V_CC/R_C as the maximum collector current in saturation; V_CE(sat) is \"a tenth of a volt or so\" for small-signal devices; one example gives 0.15 V at I_C = 10 mA, I_B = 0.3 mA. The calculation does not include the emitter drop."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0196
title: "What should you check after calculating a transistor's collector current?"
description: "What should you check after calculating a transistor's collector current?"
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
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.5: proper NPN bias requires V_C > V_B > V_E; β varies between devices, with current and temperature; Ebers-Moll model. General picture; example numbers apply only to their own circuits."
  - source_id: fiore-bjt-datasheet
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.4 BJT Data Sheet Interpretation"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.4:_BJT_Data_Sheet_Interpretation"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.4: 2N3904 datasheet example – 625 mW at 25 °C free air, I_C up to 200 mA, V_CE up to 40 V, not simultaneously; normalized β falls at low current and rises with temperature; V_CE(sat) graph. Applies only to this device."
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

## Sources

<!-- generated from frontmatter -->

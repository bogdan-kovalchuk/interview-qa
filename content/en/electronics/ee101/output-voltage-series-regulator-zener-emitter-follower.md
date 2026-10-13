---
id: emb-elee-0202
title: "What output voltage does a series regulator with a 5.6 V Zener on an emitter follower's base give?"
description: "What output voltage does a series regulator with a 5.6 V Zener on an emitter follower's base give?"
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
    applicability: "Question origin: lecture 69 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-zener-follower
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.7 BJT Switching and Driver Applications"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.7:_BJT_Switching_and_Driver_Applications"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.7.3 (Zener Follower): the Zener is reverse-biased through a resistor and the output is taken from the emitter; output voltage V_Z − V_BE. The section does not cover how V_BE depends on current and temperature, or the Zener's minimum current."
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 7.2: exponential junction model (q/kT ≈ 38.6 at 300 K, i.e. V_T ≈ 25.9 mV); dynamic resistance r'_e = 26 mV / I_C without bulk resistance; depends on temperature; small-signal model for low and mid frequencies."
  - source_id: fiore-bjt-basics
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.2 The Bipolar Junction Transistor"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.2:_The_Bipolar_Junction_Transistor"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.2: I_E = I_C + I_B, I_C = β·I_B; with I_C much larger than I_B, I_E ≈ I_C; V_BE ≈ 0.7 V for silicon. General picture, not for a specific transistor."
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-13
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Application note: the series resistor R1 must pass the Zener's minimum current plus the maximum load current; the datasheet V_Z test current (about 5 mA up to 17 V) is named a good value; the temperature coefficient S_Z depends on the working current, more strongly at lower voltages. Nexperia data; other manufacturers may have other numbers."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

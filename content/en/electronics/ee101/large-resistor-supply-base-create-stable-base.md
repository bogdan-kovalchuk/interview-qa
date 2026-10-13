---
id: emb-elee-0197
title: "Does one large resistor from the supply to the base create a stable base voltage?"
description: "Does one large resistor from the supply to the base create a stable base voltage?"
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
  - source_id: fiore-bjt-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.5: base-bias example with R_B, I_B = (V_BB - V_BE)/R_B; collector current 4.65 mA at β = 100 and 9.3 mA at β = 200; β varies between devices, with current and temperature. General picture; the numbers apply only to this circuit."
  - source_id: fiore-bias-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 5.2: why bias is needed (V_BE ≈ 0.7 V; without DC bias the negative half of a signal of a few hundred millivolts is ignored); an unstable Q point degrades gain, distortion and output power. General picture."
  - source_id: fiore-voltage-divider-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.4 Voltage Divider Bias"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.4:_Voltage_Divider_Bias"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 5.4: voltage divider bias with Thevenin equivalent V_TH and R_TH; base-emitter loop; approximation I_E ≈ I_C and the condition R_E much larger than R_TH/β; the divider is described as a configuration with high bias stability. Textbook example values apply only to its own circuit."
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

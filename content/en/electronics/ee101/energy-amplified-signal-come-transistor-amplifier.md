---
id: emb-elee-0191
title: "Where does the energy of the amplified signal come from in a transistor amplifier?"
description: "Where does the energy of the amplified signal come from in a transistor amplifier?"
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
    applicability: "Question origin: lecture 67 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-biasing-need
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.2 The Need For Biasing"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.2:_The_Need_For_Biasing"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 5.2: amplification needs an additional source of energy; without DC bias the negative half-cycle and voltages below about 0.7 V are not amplified; a stable operating point should not move when β changes. Qualitative; gives no device data."
  - source_id: fiore-ebers-moll
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.5 Ebers-Moll Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.5:_Ebers-Moll_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.5: β depends on the device, temperature, I_C and V_CE; the fixed-I_B base bias example (β = 100 gives I_C = 4.65 mA, β = 200 gives 9.3 mA) and thermal positive feedback; the simplified Ebers-Moll model. Gives no data for a specific device."
  - source_id: fiore-emitter-bias
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 5.3 Two-Supply Emitter Bias"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/05:_BJT_Biasing/5.3:_Two-Supply_Emitter_Bias"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 5.3: two-supply emitter bias, I_C = (|V_EE| - V_BE)/(R_E + R_B/β); if R_E is much larger than R_B/β, β plays virtually no role in I_C; V_C = V_CC - I_C*R_C. The 1 % figure applies only to this example's values."
  - source_id: fiore-amplifier-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 6.2 Amplifier Model"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/06:_Amplifier_Concepts/6.2:_Amplifier_Model"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 6.2: power gain is the ratio P_out/P_in (example: 50 mW output from 10 mW input gives 5). The model does not explain how the circuit creates the gain."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

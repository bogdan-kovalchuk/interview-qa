---
id: emb-elee-0231
title: "How do you debug an assembled transistor audio amplifier?"
description: "How do you debug an assembled transistor audio amplifier?"
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
    applicability: "Question origin: lecture 75 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-14; the course is not proof of these claims."
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
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 4.2: in active mode the base-emitter junction is forward-biased and the base-collector junction reverse-biased; V_BE ≈ 0.7 V for silicon; I_C ≫ I_B, so I_E ≈ I_C. General picture, not for a specific transistor."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 4.6: load line; I_C(sat) = V_CC/R_C is the largest collector current; V_CE(cutoff) = V_CC at I_C = 0; in saturation V_CE(sat) is a tenth of a volt or so for small-signal devices."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 7.3: coupling capacitors act as opens for DC and as shorts for the signal when their reactance is much smaller than the surrounding resistances; A_v = -r_C/(r'_e + r_E) has a minus sign (inversion, 180 degree phase shift); Z_out ≈ R_C when R_C is much smaller than r'_C; with a load A_divider = R_L/(R_L + R_C) (example 7.1)."
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-14
    kind: book
    version: null
    applicability: "Textbook, section 7.2: r'_e = 26 mV / I_C is an approximate dynamic resistance of the base-emitter junction at a given DC collector current; a low- and mid-frequency model without junction capacitances."
  - source_id: fiore-ac-circuit-analysis
    title: "James M. Fiore: AC Electrical Circuit Analysis, A Practical Approach (sections 1.5 and 10.3)"
    url: https://www2.mvcc.edu/users/faculty/jfiore/Circuits2/ACElectricalCircuitAnalysis.pdf
    accessed: 2026-10-14
    kind: book
    version: "1.1.2, 22 April 2021"
    applicability: "Open-license textbook (Creative Commons), lead network section (chapter 10): an RC network with the output across R is a high-pass filter; f_c = 1/(2*pi*R*C) is the frequency at which the signal drops by 3 dB; loss A'v = -10*log10(1+(f_c/f)^2) (example 10.13); X_C = 1/(2*pi*f*C). Formulas for a single RC network."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

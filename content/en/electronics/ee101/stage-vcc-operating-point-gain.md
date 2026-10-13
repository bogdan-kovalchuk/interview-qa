---
id: emb-elee-0210
title: "CE stage: `V_CC` = 10 V, `I_E` ≈ 1 mA, `R_E` = 1 kΩ, `R_C` = 4.7 kΩ. What are the operating point and the gain?"
description: "CE stage: `V_CC` = 10 V, `I_E` ≈ 1 mA, `R_E` = 1 kΩ, `R_C` = 4.7 kΩ. What are the operating point and the gain?"
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
    applicability: "Question origin: lecture 71 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
    applicability: "Textbook, section 4.2: I_E = I_C + I_B; for I_C ≫ I_B, I_E ≈ I_C; V_BE ≈ 0.7 V for silicon. General picture, not a specific transistor."
  - source_id: fiore-bjt-dc-load-line
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.6 DC Load Lines"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.6:_DC_Load_Lines"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 4.6: load line; I_C(sat) = V_CC/R_C is the maximum collector current at saturation, and V_CE(cutoff) = V_CC at I_C = 0; a calculated current above I_C(sat) gives I_C(sat). The formula V_CC/R_C ignores V_CE(sat)."
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 7.2: r'_e = 26 mV / I_C as the dynamic junction resistance (V_T ≈ 25.9 mV at 300 K); bulk resistance not included; depends on I_C and temperature; g_m is the transconductance; low and mid-band model without junction capacitances."
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 7.3: AC equivalent by superposition; capacitors replaced by shorts, DC sources by their ideal internal resistance (AC ground); A_v = -r_C/(r'_e + r_E); Z_in(base) = β(r'_e + r_E); Z_out ≈ R_C; an unbypassed R_E reduces gain and distortion. Numerical examples apply only to those circuits."
  - source_id: mit-6071-bjt-notes
    title: "MIT OCW 6.071/22.071 (Spring 2006): Transistors: Bipolar Junction Transistors (BJT), lecture notes"
    url: "https://ocw.mit.edu/courses/6-071j-introduction-to-electronics-signals-and-measurement-spring-2006/b30aa58fb0c9915da21e5a5855384818_19_bjt_1.pdf"
    accessed: 2026-10-13
    kind: book
    version: "Spring 2006"
    applicability: "University lecture notes: cutoff (I_C = 0, V_o = V_CC), saturation (V_CE(sat) typically about 0.2 V; I_C(sat) = (V_CC - V_CE(sat))/R_C), I_C = β·I_B; for β = 100, α = 0.99 and I_C ≈ I_E. The notes do not cover small-signal parameters."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0217
title: "Why can the gain measured from the generator be lower than the gain calculated from the base?"
description: "Why can the gain measured from the generator be lower than the gain calculated from the base?"
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
    applicability: "Question origin: lecture 72 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-13; the course is not proof of these claims."
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
  - source_id: fiore-common-emitter-amplifier
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.3 Common Emitter Amplifier"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.3:_Common_Emitter_Amplifier"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Section 7.3: A_v = -r_C/(r'_e + r_E), with r_C = R_C || R_L at AC; coupling capacitors act as shorts, V_CC is AC ground, a bypassed R_E grounds the emitter for AC; Z_in = R_B || Z_in(base), Z_in(base) = β(r'_e + r_E); the divider Z_in/(Z_in + source resistance) of example 3; r'_C of the order of 100 kΩ, Z_out ≈ R_C; section 7.3.4: bypass capacitors bring the supply close to AC ground. The example numbers apply only to these circuits."
  - source_id: fiore-bjt-ac-model
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 7.2 Simplified AC Model of the BJT"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/07:_BJT_Small_Signal_Amplifiers/7.2:_Simplified_AC_Model_of_the_BJT"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook, section 7.2: i_C = β·i_B; dynamic resistance r'_e = 26 mV / I_C without bulk resistance; the model excludes junction capacitance and is for low and mid frequencies; the common-emitter stage inverts the phase."
  - source_id: fiore-bjt-collector-curves
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 4.3 BJT Collector Curves"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/04:_Bipolar_Junction_Transistors_(BJTs)/4.3:_BJT_Collector_Curves"
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Textbook section 4.3: three zones of the collector curves – saturation (left, V_CE(sat) a few tenths of a volt), the nearly constant-current zone used for linear amplifiers in the middle, and breakdown on the right; saturation is used in switching. Section 4.3.1: I_C rises with V_CE; extending the constant-current region gives the Early voltage V_A. General picture, not a specific transistor."
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

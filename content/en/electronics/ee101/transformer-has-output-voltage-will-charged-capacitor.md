---
id: emb-elee-0174
title: "A transformer has a \"9 V AC\" output. What voltage will a charged capacitor show after the bridge?"
description: "A transformer has a \"9 V AC\" output. What voltage will a charged capacitor show after the bridge?"
track: electronics
section: ee101
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-06
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
    applicability: "Question origin: lecture 64 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Section 3.2.3: a capacitor after the rectifier charges to the peak of the secondary (under light load the output floats to the peak), ripple grows with load current and the nominal output drops; section 3.2.4: in a bridge rectifier the load sees the secondary voltage minus two forward diode drops, the peak equals RMS*sqrt(2) (24 V RMS gives 34 V), and the capacitor is chosen for the peak voltage with margin. The silicon diode drop of about 0.7 V is an approximation."
  - source_id: kuphaldt-transformer-regulation
    title: "Tony R. Kuphaldt: Lessons In Electric Circuits, Vol. II (AC), 10.6 Voltage Regulation (LibreTexts)"
    url: https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_II_-_Alternating_Current_(Kuphaldt)/10:_Transformers/10.06:_Voltage_Regulation
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "The secondary voltage decreases as the load current grows; in the SPICE example 9.990 V at no load and 9.348 V at full load; for a power transformer with a resistive load a regulation below 3 % is considered good, and an inductive load makes it worse. The numbers of the example are not parameters of a real transformer."
  - source_id: vishay-1n400x
    title: "Vishay: 1N4001–1N4007 datasheet"
    url: https://www.vishay.com/docs/88503/1n4001.pdf
    accessed: 2026-10-06
    kind: official
    version: "29-Apr-2020"
    applicability: "Maximum instantaneous forward voltage VF = 1.1 V at 1.0 A (TA = 25 °C) for the 1N4001–1N4007 series; other diodes and currents have a different drop."
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

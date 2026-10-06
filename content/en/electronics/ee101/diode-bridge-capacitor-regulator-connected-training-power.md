---
id: emb-elee-0178
title: "How are the diode bridge, capacitor and regulator connected in a training power supply?"
description: "How are the diode bridge, capacitor and regulator connected in a training power supply?"
track: electronics
section: ee101
level: junior
type: concept
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
    applicability: "Question origin: lecture 65 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
    applicability: "A bridge rectifier with a filter capacitor on an ordinary (non-center-tapped) secondary, available as a single four-lead part; two diodes conduct in each half-cycle, so the load sees the secondary voltage minus two drops; the capacitor smooths the ripple and is chosen for the peak voltage (example: 34 V peak, a 50 V part is used). The book does not cover specific bridges or regulators."
  - source_id: vishay-gbu4
    title: "Vishay: GBU4A-GBU4M glass passivated single-phase bridge rectifier (datasheet)"
    url: https://www.vishay.com/docs/88614/gbu4a.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 13-Jul-2020"
    applicability: "The GBU package has terminals marked \"~\", \"+\" and \"-\", and its Mechanical Data section says \"Polarity: as marked on body\". This is an example of one bridge type; the pin layout of other packages comes from their datasheets."
  - source_id: vishay-alu-intro
    title: "Vishay BCcomponents: Aluminum Electrolytic Capacitors – Introduction, Basic Concepts, and Definitions"
    url: https://www.vishay.com/docs/28356/alucapsintrobcc.pdf
    accessed: 2026-10-06
    kind: official
    version: "Revision 13-Feb-2026"
    applicability: "Marking section: polarity is shown by a strip, band or negative sign next to the negative terminal (and/or a plus sign); the definition of reverse voltage U_REV as the maximum voltage applied in the reverse polarity direction to the terminals. The document does not give an allowed reverse-voltage value."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "TO-220 pins: 1 – input, 2 – ground, 3 – output; the description on the first page says input bypassing is needed only if the regulator is located far from the filter capacitor of the power supply. The values apply to TI's LM340/LM7805 family, not to 7805 devices of other makers."
  - source_id: ti-ua78
    title: "TI: uA7805, uA7808, uA7810, uA7812, uA7815, uA7824 positive-voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/ua78.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVS056P, January 2015"
    applicability: "Recommended Operating Conditions section: the input voltage of the uA7805 is 7 to 25 V. The values apply to TI's uA78xx family, not to 7805 devices of other makers."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

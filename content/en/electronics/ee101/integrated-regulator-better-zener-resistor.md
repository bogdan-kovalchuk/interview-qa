---
id: emb-elee-0145
title: "When is an integrated regulator better than a Zener with a resistor?"
description: "When is an integrated regulator better than a Zener with a resistor?"
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
    applicability: "Question origin: lecture 58 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: nexperia-an90031
    title: "Nexperia AN90031: Zener diodes – physical basics, parameters and application examples"
    url: https://assets.nexperia.com/documents/application-note/AN90031.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 3.0, 7 June 2023"
    applicability: "Zener dynamic resistance r_dif = ΔV_Z/ΔI_Z > 0; section 3: the basic Zener stabilizer with series resistor R1 for rather low power, choosing R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max)), maximum Zener dissipation with no load P_ZD1 = V_Z*(V_IN - V_Z)/R1; data are for Nexperia series, other manufacturers can have other numbers."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Section 3.2.6: Zener regulator with a current-limiting resistor, how current splits between the Zener and the load, loss of regulation when the load current is too high (the resistor forms a divider with the load), maximum Zener dissipation at no load, remark about low efficiency; the book gives no data for specific integrated regulators."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "LM340A table (V_O = 5 V, V_I = 10 V): load regulation up to 25 mV for 5 mA ≤ I_O ≤ 1.5 A (25 °C), quiescent current up to 6 mA, dropout 2 V (typical) at 1 A, short-circuit current 2.1 A (typical); internal current limiting, thermal shutdown above 150 °C and the formula P_DMAX = (T_JMAX - T_A)/θ_JA. Values apply to this family, not to all integrated regulators."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

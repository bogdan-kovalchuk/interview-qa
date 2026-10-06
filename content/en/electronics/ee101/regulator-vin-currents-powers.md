---
id: emb-elee-0134
title: "Regulator: `V_in` = 9 V, `V_Z` ≈ 5.1 V, R = 390 Ω. What are the currents and powers?"
description: "Regulator: `V_in` = 9 V, `V_Z` ≈ 5.1 V, R = 390 Ω. What are the currents and powers?"
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
    applicability: "Question origin: lecture 56 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
    applicability: "Behaviour of a Zener diode in the forward and reverse directions, the Zener effect up to about 5 V and avalanche breakdown above, the sign change of the temperature coefficient S_Z near 6 V, differential resistance r_dif, the V_Z test current, choosing R with R1 = (V_IN - V_Z)/(I_Z(min) + I_LOAD(max)) and the dissipated powers in a simple regulator; the data are for Nexperia series, other manufacturers can have other numbers."
  - source_id: nexperia-bzx84
    title: "Nexperia BZX84 series: voltage regulator diodes (datasheet)"
    url: https://assets.nexperia.com/documents/data-sheet/BZX84_SER.pdf
    accessed: 2026-10-06
    kind: official
    version: "Rev. 7, 1 January 2023"
    applicability: "Parameters of the BZX84-C5V1: V_Z = 4.8–5.4 V at 5 mA, maximum r_dif of 480 Ω at 1 mA and 60 Ω at 5 mA, P_tot ≤ 250 mW at T_amb ≤ 25 °C; values for this series, not for every 5.1 V Zener diode."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Capacitor filter and ripple (discharge between peaks, ripple growing with load current, charging current spikes), the bridge rectifier (two diodes conduct in each half-cycle, two V_F drops), the simple Zener regulator and loss of regulation when the load current is too large; the book gives neither the formula ΔV = I/(f*C) nor the V_F of a specific diode."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-elee-0150
title: "Why is a bleeder resistor placed across the capacitor in a diode circuit?"
description: "Why is a bleeder resistor placed across the capacitor in a diode circuit?"
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
    applicability: "Question origin: lecture 59 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: kuphaldt-bleeder-supply
    title: "Workforce LibreTexts: Electric Circuits VI – Experiments (Kuphaldt), 5.19 Vacuum Tube Audio Amplifier"
    url: "https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Electric_Circuits_VI_-_Experiments_(Kuphaldt)/05:_Discrete_Semiconductor_Circuits/5.19:_Vacuum_Tube_Audio_Amplifier"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "In a power-supply circuit with a filter capacitor, a 100 kΩ resistor in parallel with the capacitor gives it a discharge path after the AC power is turned off; without it the capacitor would likely keep a dangerous charge for a long time. The example of 47 µF and 100 kΩ gives a time constant of 4.7 s, and a larger capacitor needs a smaller resistor or a longer wait. The book describes one teaching experiment, not safety regulations."
  - source_id: vishay-pre-charge-bleed
    title: "Vishay: Pre-charge resistor and bleed resistor selection (Did You Know?, MS8772259-1810)"
    url: https://www.vishay.com/docs/48468/_ms8772259-1810-didyouknow-rs_rh-nh.pdf
    accessed: 2026-10-06
    kind: official
    version: "MS8772259-1810, 2018"
    applicability: "One sentence stating that a bleed resistor safely discharges inverter capacitors when the system is not in use (hybrid and electric vehicles), and a list of parameters needed to select such a resistor. The document gives no formulas or resistance values."
  - source_id: fiore-rectification
    title: "Engineering LibreTexts: Semiconductor Devices – Theory and Application (Fiore), 3.2 Rectification"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Semiconductor_Devices_-_Theory_and_Application_(Fiore)/03:_Diode_Applications/3.2:_Rectification"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "A rectifier capacitor charges while the diode conducts and discharges into the load when the diode turns off; under light load the output stays near the peak of the secondary voltage with little ripple. The book does not discuss a bleeder resistor separately."
  - source_id: fiore-peak-detector
    title: "Engineering LibreTexts: Operational Amplifiers and Linear Integrated Circuits (Fiore), 7.2 Precision Rectifiers"
    url: "https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electronics/Operational_Amplifiers_and_Linear_Integrated_Circuits_-_Theory_and_Application_(Fiore)/07:_Nonlinear_Circuits/7.02:_Precision_Rectifiers"
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Op-amp peak detector: after the peak the diode turns off and the capacitor discharges through a resistance; the discharge time constant sets how long the peak is held, giving a nearly constant output for a long constant and an envelope for a shorter one; capacitor leakage limits the largest discharge resistance. An op-amp circuit, not an ordinary mains rectifier."
  - source_id: gatech-rc-charging-discharging
    title: "Georgia Tech Physics Book: Charging and Discharging a Capacitor"
    url: https://physicsbook.gatech.edu/Charging_and_Discharging_a_Capacitor
    accessed: 2026-10-06
    kind: book
    version: null
    applicability: "Discharging a capacitor through a resistor: time constant τ = R*C, charge Q(t) = Q0*e^(-t/(R*C)), so the voltage decays along the same exponential law; an ideal RC circuit with no extra load or leakage."
---

## Short answer

TODO

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

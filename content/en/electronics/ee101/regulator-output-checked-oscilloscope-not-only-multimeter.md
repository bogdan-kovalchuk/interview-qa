---
id: emb-elee-0166
title: "Why should a regulator's output be checked with an oscilloscope and not only with a multimeter?"
description: "Why should a regulator's output be checked with an oscilloscope and not only with a multimeter?"
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
    applicability: "Question origin: lecture 62 of the Udemy course; the original card is preserved in imports. The Ukrainian short answer and explanation were checked against cited technical sources on 2026-10-06; the course is not proof of these claims."
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
  - source_id: keysight-34401a-tutorial
    title: "Agilent (Keysight) 34401A: Digital Multimeter Tutorials"
    url: https://www.ee.torontomu.ca/guides/instrument-manuals/Agilent-HP_34401A_Tutorial.pdf
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Section on rejecting power-line noise: a digital multimeter with an integrating A/D converter measures the average of the input by integrating it over a fixed period; an integration time that is a whole number of power line cycles averages power-line noise out to approximately zero. A document about one instrument (the 34401A), hosted on a university site; other multimeters use other intervals and modes."
  - source_id: tek-dmm7510-ripple-an
    title: "Tektronix (Keithley): Measuring Low Level Ripple Voltage Using the DMM7510 7-1/2-Digit Graphical Sampling Multimeter"
    url: https://www.tek.com/en/documents/application-note/measuring-low-level-ripple-voltage-using-dmm7510-7-1-2-digit-graphical-s-0
    accessed: 2026-10-06
    kind: official
    version: null
    applicability: "Introduction: traditional DMMs often lack the capability to measure the dynamic behavior of power supplies, and an oscilloscope is typically needed to examine ripple voltage, switching voltage and power-up glitches; an oscilloscope may lack the resolution for very low level ripple, and in DC coupling it is limited by the maximum DC offset on its lowest range, while in AC coupling it resolves the ripple to some extent. The example in the note is a switching buck converter, not a linear regulator."
  - source_id: teledyne-probe-ground-lead
    title: "Teledyne LeCroy: Passive Probe Ground Lead Effects"
    url: https://www.teledynelecroy.com/doc/passive-probe-ground-lead-effects
    accessed: 2026-10-06
    kind: official
    version: "June 2013"
    applicability: "A long alligator-clip ground lead (about 10 inches, rule of thumb 20 nH per inch, roughly 200 nH) together with the probe input capacitance forms a series resonance, reduces bandwidth and causes ringing on fast edges; ground blades or springs have 10–20 nH. The numbers refer to 500 MHz passive probes from Teledyne LeCroy; other probes differ."
  - source_id: ti-lm340
    title: "TI: LM340, LM340A, LM7805 family wide VIN 1.5-A fixed voltage regulators (datasheet)"
    url: https://www.ti.com/lit/ds/symlink/lm340.pdf
    accessed: 2026-10-06
    kind: official
    version: "SNOSBT0L, September 2016"
    applicability: "An output capacitor is not needed for stability but improves transient response; if the regulator is more than about six inches from the supply filter, an input capacitor of 0.1 µF or more is needed 'for stability'. The values apply to the LM340/LM7805 family; other regulators and manufacturers may require otherwise."
  - source_id: ti-slva079
    title: "Texas Instruments SLVA079: Understanding the Terms and Definitions of LDO Voltage Regulators"
    url: https://www.ti.com/lit/an/slva079/slva079.pdf
    accessed: 2026-10-06
    kind: official
    version: "SLVA079, October 1999"
    applicability: "Section 10: LDO manufacturers typically give a stable range of compensation series resistance (CSR = output capacitor ESR plus an additional resistor), because CSR can cause instability depending on output current (TPS763xx example: 0.2–9 Ω). A report about LDOs; the capacitor requirements of the 7805 are different."
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

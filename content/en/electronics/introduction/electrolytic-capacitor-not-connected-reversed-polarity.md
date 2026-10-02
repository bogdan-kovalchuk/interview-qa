---
id: emb-elintro-0010
title: Why must an electrolytic capacitor not be connected with reversed polarity?
description: Why must an electrolytic capacitor not be connected with reversed polarity?
track: electronics
section: introduction
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
- source_id: udemy-electronics-course
  title: 'Udemy: Crash Course Electronics and PCB Design (Andre LaMothe), course flashcards'
  url: https://www.udemy.com/course/crash-course-electronics-and-pcb-design/
  accessed: 2026-09-27
  kind: community
  version: null
  applicability: 'Historical question provenance: lecture 3 of the Udemy course. Original flashcards remain in imports.
    Current answers and explanations were independently revised against cited technical sources on 2026-10-04; this
    source is not factual proof of the revised prose.'
- source_id: aac-direct-current
  title: 'All About Circuits textbook, Volume I: DC'
  url: https://www.allaboutcircuits.com/textbook/direct-current/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: DC circuits, Ohm''s law, Kirchhoff''s laws, sources and
    measurement; specific component values and circuits of the course can differ.'
- source_id: aac-semiconductors
  title: 'All About Circuits textbook, Volume III: Semiconductors'
  url: https://www.allaboutcircuits.com/textbook/semiconductors/
  accessed: 2026-09-27
  kind: book
  version: null
  applicability: 'Authoritative section-level reference: diodes, Zener diodes, bipolar and field-effect transistors
    and power supplies; specific component values and circuits of the course can differ.'
- source_id: nichicon-polarity
  title: 'Nichicon: Technical notes for aluminum electrolytic capacitors'
  url: https://www.nichicon.co.jp/english/products/pdf/aluminum.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Polarized oxide dielectric, charge/energy relations and reverse-voltage damage, section 2-3-2.
- source_id: vishay-tantalum
  title: 'Vishay: Solid tantalum capacitor FAQ'
  url: https://www.vishay.com/docs/40110/faq.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: 'Polarity markings: white bar marks the positive anode on molded SMD tantalum capacitors.'
---

## Short answer

Reverse voltage can damage a polarized electrolytic capacitor’s dielectric, causing leakage, heat and gas generation. Identify polarity from the exact component markings and datasheet: typical radial aluminum parts mark the negative side, whereas the bar on molded SMD tantalum capacitors marks the positive anode. [^nichicon-polarity] [^vishay-tantalum]

## Detailed explanation

In a polarized aluminum electrolytic capacitor, the thin oxide dielectric is formed for the intended polarity. Nichicon explains that reverse voltage can increase leakage and produce heat and gas, with possible venting or failure. An explosion is a possible severe outcome, not a guaranteed response to every momentary reversal. [^nichicon-polarity]

On typical radial aluminum parts, a negative stripe and an uncut longer positive lead help orientation. Lead length is no longer reliable after trimming. Do not turn the negative-stripe convention into a rule for all electrolytics: Vishay explicitly states that the white bar on molded SMD tantalum parts identifies the positive anode. [^vishay-tantalum]

Before installation, match the body marking and datasheet pinout to the schematic and PCB polarity. Also check the applied waveform: a positive average voltage does not make reverse excursions acceptable automatically. Observe rated voltage and permitted ripple current. Bipolar electrolytics are a distinct specified part type; do not assume an ordinary polarized part behaves like one. [^nichicon-polarity]

## Sources

<!-- generated from frontmatter -->

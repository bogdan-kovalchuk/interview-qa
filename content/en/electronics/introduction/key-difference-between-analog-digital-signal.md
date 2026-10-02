---
id: emb-elintro-0002
title: What is the key difference between an analog and a digital signal?
description: What is the key difference between an analog and a digital signal?
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
- source_id: ti-pam4
  title: 'TI SNAA325A: PAM-4 signaling'
  url: https://www.ti.com/lit/an/snaa325a/snaa325a.pdf
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: 'Section 1.2: four discrete signaling levels encode two bits per symbol.'
---

## Short answer

An analog signal represents information through a continuously varying quantity; a digital signal uses a discrete set of symbols. Binary logic commonly uses LOW and HIGH, but digital signaling can use more than two levels: PAM-4 uses four levels carrying two bits per symbol. [^ti-pam4]

## Detailed explanation

The distinction concerns how information is represented and interpreted. An analog voltage may encode a measured temperature over a continuous range. A digital receiver assigns the received waveform to one of a finite set of symbols. The electrical voltage itself still changes continuously during transitions; it does not become a physically discrete quantity.

In binary signaling, two recognized states encode 0 and 1. PAM-4 is a counterexample to the rule that every digital signal has only two voltage levels: four symbol levels encode two bits per symbol. Thus “digital” is broader than “binary.” [^ti-pam4]

A signal can also be discrete in time without being binary in amplitude. Sampling chooses observation times; quantization chooses representable amplitude values. Keep these two operations separate when explaining an ADC. A digital representation enables processing of symbols, but does not by itself guarantee immunity to electrical noise.

## Sources

<!-- generated from frontmatter -->

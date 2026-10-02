---
id: emb-elintro-0019
title: Why is the digital representation of an analog signal not perfectly accurate?
description: Why is the digital representation of an analog signal not perfectly accurate?
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
  applicability: 'Historical question provenance: lecture 4 of the Udemy course. Original flashcards remain in imports.
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
- source_id: adi-adc
  title: 'Analog Devices: Analog-to-digital conversion, chapter 20'
  url: https://wiki.analog.com/university/courses/electronics/text/chapter-20
  accessed: 2026-10-04
  kind: official
  version: null
  applicability: Sampling and finite-bit quantization, ADC/DAC distinction.
- source_id: adi-quantization
  title: 'Analog Devices MT-001: Quantization error and ADC SNR'
  url: https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf
  accessed: 2026-10-04
  kind: official
  version: MT-001
  applicability: Ideal quantization error within half a step; real converter errors are additional.
---

## Short answer

A finite sampled representation can lose information through quantization, insufficient sampling, noise and converter errors. More bits reduce the ideal amplitude step, while adequate sampling and filtering prevent aliasing under the applicable signal assumptions. The error is not necessarily nonzero for every sample. [^adi-adc] [^adi-quantization]

## Detailed explanation

With a fixed input span, a uniform N-bit step is approximately `span/2^N`. At 3.3 V span, the calculated step decreases from about 12.89 mV for 8 bits to 0.806 mV for 12 bits. That is finer resolution, not automatically better accuracy: real noise and systematic errors may dominate. The ideal half-step quantization bound requires a suitable quantizer model without clipping. [^adi-quantization]

Sampling adds a separate limitation. Different time-varying signals can produce the same samples if their spectra are not constrained, a phenomenon called aliasing. Anti-alias filtering and a sample rate appropriate to the signal bandwidth are therefore part of acquisition, not a substitute for more amplitude bits. [^adi-adc]

Sampling alone is not inherently lossy under every theoretical condition: an ideally band-limited signal with sufficiently fast ideal sampling can be reconstructed from its samples. Practical finite records, finite precision and imperfect converters do not meet all of those ideal conditions. Distinguish that theorem from an actual ADC measurement, and avoid saying every sample must contain a quantization error.

## Sources

<!-- generated from frontmatter -->

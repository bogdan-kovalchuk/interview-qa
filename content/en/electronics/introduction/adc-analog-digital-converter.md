---
id: emb-elintro-0018
title: What does an `ADC` (analog-to-digital converter) do?
description: What does an `ADC` (analog-to-digital converter) do?
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

An analog-to-digital converter maps an analog input to numeric codes. In a sampled-data system, sampling selects times and quantization maps amplitudes to a finite set of codes; an N-bit output has up to `2^N` codes. Resolution, input range and sampling behavior must be specified. [^adi-adc]

## Detailed explanation

Sampling and quantization answer different questions: when is the signal observed, and which numeric value represents that observation? Increasing sample rate does not itself increase the number of amplitude codes. Increasing bit depth does not itself capture faster signal changes. ADC architectures implement these operations differently, so the simplified model is a functional description. [^adi-adc]

For an ideal uniform 8-bit converter spanning 0–3.3 V, a useful step model is `LSB = 3.3/256 ≈ 12.89 mV`. An ideal nearest-level quantizer has error within half a step for inputs inside its unclipped range, away from endpoint conventions. Exact transitions and full-scale definitions should follow the converter datasheet. [^adi-quantization]

Real accuracy also includes reference error, offset, gain error, nonlinearity and noise. A sample can happen to match a representable level exactly: quantization does not imply a nonzero error for every input. A DAC performs the opposite conversion to an analog output, usually followed by appropriate reconstruction filtering.

## Sources

<!-- generated from frontmatter -->

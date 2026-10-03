---
id: emb-dtypes-0113
title: "What are little-endian and big-endian, and where do they matter in embedded systems?"
description: "Endianness defines the byte order of multibyte values in memory and matters in protocols, peripherals, flash images, and debugging; bit order in SPI or I2C is a separate property."
track: embedded
section: data-types-and-memory-layout
level: middle
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
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: python-struct-byte-order
    title: "Python 3 struct module: byte order, size, and alignment"
    url: https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
    accessed: 2026-10-04
    kind: official
    version: "3"
    applicability: "Describes little-endian and big-endian in serialization formats and cautions against relying on native byte order when exchanging data; it does not define bit order for a specific peripheral."
---

## Short answer

**Endianness** defines the byte order of a multibyte value in memory: little-endian places the least significant byte at the lowest address, big-endian – the most significant. In embedded systems, this matters in binary protocols, peripheral FIFOs, network byte order, flash images, and debug memory view.[^python-struct-byte-order] Bit order within an SPI/I2C frame is a separate property and does not equal CPU endianness.[^iso-c-n1570]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

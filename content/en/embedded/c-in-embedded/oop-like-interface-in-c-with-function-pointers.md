---
id: emb-cemb-0031
title: "How can an OOP-like interface be implemented in C with structs, function pointers, and opaque handles?"
description: "Opaque types and function-pointer tables provide encapsulation and polymorphism in C driver APIs."
track: embedded
section: c-in-embedded
level: middle
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

The public API declares an opaque type `typedef struct uart uart_t;`, and the implementation hides the struct fields in a `.c` file. Methods accept `uart_t*`, and polymorphism can be achieved through a table of function pointers: `read`, `write`, `ioctl`. This way the driver API has encapsulation without C++ ABI and without exposing internal MMIO/state.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

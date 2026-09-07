---
id: emb-cemb-0021
title: "What is the difference between C-style and C++ casts?"
description: "A C-style cast can hide several operations, while separate C++ casts state the conversion type and intent explicitly."
track: embedded
section: c-in-embedded
level: junior
type: comparison
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

**A C-style cast** looks like `(T)x` and can perform several kinds of conversion at once: numeric conversion, removing `const`, pointer reinterpretation. Because of this it is short but imprecise and can hide a dangerous operation.[^dou-embedded-interview]

In C++ it is better to use explicit casts: `static_cast` for ordinary safer conversions, `const_cast` only for changing cv-qualifiers, `reinterpret_cast` for low-level reinterpretation, `dynamic_cast` for runtime-checked casts in polymorphic classes. They are longer, but they show intent and are easier to find in code.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Sources

<!-- generated from frontmatter -->

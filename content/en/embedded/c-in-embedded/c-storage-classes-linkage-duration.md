---
id: emb-cemb-0040
title: "What storage classes exist in C, and how do they relate to linkage and storage duration?"
description: "Storage-class specifiers in C affect visibility, linkage, or object lifetime, but not all in the same way."
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

The main specifiers are: `auto`, `register`, `static`, `extern`, `_Thread_local`. `static` at block scope gives static storage duration, and at file scope gives internal linkage. `extern` typically declares an object/function with external linkage, but the lifetime is determined by the object itself, not by the `extern` keyword.[^dou-embedded-interview]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

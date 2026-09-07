---
id: emb-cemb-0018
title: "What is extern \"C\" for?"
description: "extern \"C\" disables C++ name mangling so that symbols are compatible with C linkage across language boundaries."
track: embedded
section: c-in-embedded
level: junior
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

`extern "C"` is used in C++ to tell the compiler to apply C linkage to functions or variables.[^dou-embedded-interview] The main effect is disabling C++ name mangling, so the symbol name in the object/shared library will be C-compatible.

This is needed when C++ code calls a C library or C code needs to call a function written in C++. A typical header is written as: `#ifdef __cplusplus extern "C" { #endif` ... `#ifdef __cplusplus } #endif`, but the function body itself remains C++ code, while the ABI and symbol name become C-compatible.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

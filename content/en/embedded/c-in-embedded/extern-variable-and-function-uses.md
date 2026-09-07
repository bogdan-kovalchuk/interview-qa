---
id: emb-cemb-0025
title: "What are common uses of `extern`?"
description: "extern declares a name defined in another translation unit; in C++, extern \"C\" disables name mangling for C API compatibility."
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

`extern` declares a name that is defined in another translation unit: in a header you write `extern int counter;`, and in one `.c` file there must be a definition `int counter;`. This allows separating declaration and definition without duplicating the global variable.

`extern` is also used for functions, although for ordinary functions external linkage is the default. In C++ there is a special case `extern "C"` – it disables C++ name mangling so that C++ code can link with a C API or a dynamic library.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

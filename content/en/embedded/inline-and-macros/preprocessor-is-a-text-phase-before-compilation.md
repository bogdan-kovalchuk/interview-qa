---
id: emb-macros-0001
title: "What is the C preprocessor and when does it do its work?"
description: "The preprocessor is a text phase that runs before compilation and handles #include, #define and #if directives."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
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
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-cpp-overview
    title: "GCC manual: The C Preprocessor, Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes GNU CPP's role and limits before compilation; implementation details can differ in other preprocessors."
  - source_id: gcc-cpp-invocation
    title: "GCC manual: The C Preprocessor, Invocation"
    url: https://gcc.gnu.org/onlinedocs/cpp/Invocation.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Confirms that gcc -E stops after preprocessing; this instruction is specific to GCC."
---

## Short answer

**The preprocessor** is a text phase that runs before compilation and handles `#include`, `#define`, `#if` directives.

It processes preprocessing directives and expands macros, but does not check types or ordinary C/C++ semantics. An error may therefore become visible only after expansion, during later parsing or type checking.[^gcc-cpp-overview]

To inspect GCC's preprocessing output, use `gcc -E file.c`.[^gcc-cpp-invocation]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

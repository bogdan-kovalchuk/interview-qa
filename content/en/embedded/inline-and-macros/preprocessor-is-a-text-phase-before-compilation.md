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
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**The preprocessor** is a text phase that runs before compilation and handles `#include`, `#define`, `#if` directives.

It performs only text substitution: it knows nothing about types, scope, or C/C++ syntax. That is why an error in a macro surfaces after expansion, in the generated code, not at the `#define` site.

Rule: to see the actual expansion result, look at the output of `gcc -E file.c`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

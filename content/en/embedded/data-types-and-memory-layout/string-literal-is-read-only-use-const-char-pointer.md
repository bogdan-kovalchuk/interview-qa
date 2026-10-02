---
id: emb-dtypes-0006
title: "Why is `const char*` preferred over `char*` for a string literal?"
description: "The standard prohibits modifying a string literal array, although the standard does not specify its physical storage location."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 4
reconciled_with:
  uk: 3
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
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: cpp-draft-string-literals
    title: "C++ working draft, [lex.string]"
    url: https://eel.is/c++draft/lex.string
    accessed: 2026-10-04
    kind: spec
    version: "current"
    applicability: "Type of ordinary C++ string literals and prohibition on modifying their objects; this is a C++ working draft."
  - source_id: gcc-write-strings
    title: "GCC 16.1 Warning Options: -Wwrite-strings"
    url: https://gcc.gnu.org/onlinedocs/gcc-16.1.0/gcc/Warning-Options.html
    accessed: 2026-10-04
    kind: official
    version: "GCC 16.1"
    applicability: "GCC -Wwrite-strings diagnostic behavior; this is a compiler diagnostic, not a language rule."
---

## Short answer

In C, the string literal `"hello"` has type `char[6]`, but the standard prohibits modifying its array: an attempt has <span class="warn">undefined behavior</span>; the standard does not specify where an implementation stores the literal. In C++, a string literal has type `const char[6]`, so `const char *p = "hello";` preserves that restriction in the type system. In C, `char *p = "hello";` is allowed for compatibility, but writing through that pointer still has undefined behavior.[^iso-c-n1570] [^cpp-draft-string-literals]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

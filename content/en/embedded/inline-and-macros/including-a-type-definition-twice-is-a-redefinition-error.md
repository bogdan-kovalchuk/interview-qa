---
id: emb-macros-0039
title: "Trap: what happens if a header defining a `struct` is included twice without an include guard?"
description: "Redefinition error because redefining the same type or struct in one translation unit is forbidden."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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

<span class="warn">Redefinition error</span>: redefining the same type/`struct`/`typedef` in one translation unit is forbidden.

Double inclusion happens easily through transitive paths: `a.h` and `b.h` both include `types.h`, and `main.c` includes both. Without a guard the contents of `types.h` are processed twice.

Protection: wrap every header in an `#ifndef` guard or `#pragma once` – then the second `#include` becomes a no-op.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

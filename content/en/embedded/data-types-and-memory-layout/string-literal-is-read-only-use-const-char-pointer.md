---
id: emb-dtypes-0006
title: "Why is `const char*` preferred over `char*` for a string literal?"
description: "A string literal lives in read-only memory, so const char documents that it must not be written."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

In C, the string literal `"hello"` has type **`char[6]`**, but it is stored in a read-only region, typically `.rodata`. Modifying such an array has <span class="warn">undefined behavior</span>. In C++, the type of a string literal is `const char[6]`.

Practically correct: `const char *p = "hello";` – the type does not allow accidentally writing `p[0] = 'H'`. In C, the assignment `char *p = "hello";` is historically allowed, but GCC with `-Wwrite-strings` will warn about it;

This difference is critical: `char*` hides the read-only nature from the type system.[^embeddedinterviewlab]

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

---
id: emb-dtypes-0016
title: "What is the danger here? `int arr[10]; arr[10] = 0;`"
description: "Writing past the end of a declared array is undefined behavior that the compiler does not check."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
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

<span class="warn">Out-of-bounds access is undefined behavior.</span> Valid indices are `0..9`, so `arr[10]` is past the end of the array.

In practice it may overwrite another local variable on the stack (for example, the return address), causing corruption, a crash, or a security vulnerability, and the compiler does not check bounds.

Mitigation: `-fsanitize=address` during development, `static_assert` plus explicit checks.[^embeddedinterviewlab]

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

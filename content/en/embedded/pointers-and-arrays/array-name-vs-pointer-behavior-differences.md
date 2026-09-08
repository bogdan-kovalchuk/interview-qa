---
id: emb-ptrarr-0001
title: "What is the difference between an array name and a pointer in C, and when do they behave differently?"
description: "An array is a fixed-size object, while a pointer is a separate object that stores an address; array expressions convert to pointers in most, but not all, contexts."
track: embedded
section: pointers-and-arrays
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: c17-standard
    title: "ISO/IEC 9899:2018 (C17 Standard)"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2310.pdf
    accessed: 2026-09-08
    kind: official
    version: "C17"
    applicability: "Official C language standard."
---

## Short answer

**An array is an object with a fixed element count, whereas a pointer is a separate object storing an address.** In most expressions an array is converted to a pointer to its first element, but not when it is the operand of `sizeof` or unary `&`.[^c17-standard] Therefore `sizeof arr` measures the whole array, while `sizeof ptr` measures the pointer, and `&arr` has pointer-to-array type. Arrays are not assignable, while a non-const pointer is; in a function parameter declaration, however, `int a[]` is adjusted to `int *a`.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

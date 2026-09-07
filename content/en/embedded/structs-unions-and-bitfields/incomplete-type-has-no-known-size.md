---
id: emb-structs-0036
title: "Why can an incomplete struct not be created as an object in a header?"
description: "Impossible because the compiler does not know the size of Driver."
track: embedded
section: structs-unions-and-bitfields
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

## Question code

```c
typedef struct Driver Driver;

Driver d;
```

## Short answer

<span class="warn">Impossible, because the compiler does not know the size of `Driver`.</span>

A forward declaration creates an incomplete type. You can declare pointers to it because the pointer size is known, but you cannot allocate an object by value or access its fields.

Defence: an opaque API returns a `Driver *` or accepts caller-provided storage through a separate API that knows the required size/alignment.[^embeddedinterviewlab]

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

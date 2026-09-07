---
id: emb-macros-0033
title: "How do you do a compile-time check without `static_assert` in older C?"
description: "A negative array size trick triggers a compile error before the program runs when the condition is false."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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
#define STATIC_ASSERT(c, name) \
  typedef char name[(c) ? 1 : -1]
```

## Short answer

**The trick uses a negative array size**: if the condition is false, an array of size `-1` is declared -> <span class="warn">compile error</span> before the program runs.

This is the classic way to check layout: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)`.

Rule: in C11/C++ use the built-in `_Static_assert`/`static_assert` with a proper message; the macro trick is only for older toolchains.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

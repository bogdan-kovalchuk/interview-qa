---
id: emb-macros-0043
title: "Why is `static inline` safer than a macro for a bit operation?"
description: "A static inline function gives type checking, single argument evaluation, and debugger visibility that a macro cannot provide."
track: embedded
section: inline-and-macros
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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
static inline uint32_t set_bit(uint32_t v, unsigned n) {
  return v | (1u << n);
}
```

## Short answer

**Type checking + single evaluation of arguments + debugger visibility.**

The macro `#define SET_BIT(v,n) ((v) | (1u << (n)))` may work in this simple case, but it does not check parameter types, provides no proper symbol/debug info, and easily turns into a double-evaluation bug as the body grows. The inline version takes typed parameters and inlines just as well.

Rule: in embedded, keep bit manipulations as `static inline`, leaving macros for addresses and masks.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

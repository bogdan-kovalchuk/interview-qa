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
updated: 2026-10-04
content_revision: 4
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
---

## Question code

```c
static inline uint32_t set_bit(uint32_t v, unsigned n) {
  return v | (1u << n);
}
```

## Short answer

**Typed parameters and single evaluation of arguments.**

The macro `#define SET_BIT(v,n) ((v) | (1u << (n)))` may work in this simple case, but the preprocessor does not check parameter types and can substitute an argument in multiple places. A `static inline` function takes typed parameters, and each argument expression is evaluated once; the compiler may inline it, but is not required to.

For the shown shift, `n` must be less than the width of the left operand's type; enforce that bound separately.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

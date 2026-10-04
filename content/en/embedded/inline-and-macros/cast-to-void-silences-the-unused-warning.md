---
id: emb-macros-0034
title: "What is the `UNUSED(x)` macro for and what does it look like?"
description: "Suppresses the unused parameter warning while explicitly showing the value is deliberately unused."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-warning-options-unused
    title: "GCC: Warning Options – unused diagnostics"
    url: https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html
    accessed: 2026-10-04
    kind: official
    version: current
    applicability: "Documents GCC behavior for -Wunused-value and an example suppressing a warning by casting an expression to void; diagnostics depend on compiler and flags."
---

## Question code

```c
#define UNUSED(x) ((void)(x))
```

## Short answer

**Casting an expression to `void` explicitly discards its value**; GCC documents this for `-Wunused-value` and unused locals, while diagnostics depend on compiler and flags.[^gcc-warning-options-unused]

The `UNUSED(x)` macro in the code snippet applies that cast to a parameter, for example `UNUSED(ctx)` in a callback. The expression `x` is still evaluated: casting to `void` does not remove its side effects.[^gcc-warning-options-unused]

This does not silence every parameter warning; GCC documents the `unused` attribute for `-Wunused-parameter`. Suppress locally only when the non-use is intentional.[^gcc-warning-options-unused]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

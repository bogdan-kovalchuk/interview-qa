---
id: emb-macros-0018
title: "What does `##` before `__VA_ARGS__` mean in a variadic macro?"
description: "The ## before VAARGS removes the trailing comma when no variadic arguments are passed to the macro."
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
  - source_id: gcc-cpp-variadic-macros
    title: "GCC CPP: Variadic Macros"
    url: https://gcc.gnu.org/onlinedocs/cpp/Variadic-Macros.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Describes the GNU comma-before-__VA_ARGS__ extension and portable __VA_OPT__; behaviour depends on language mode and preprocessor."
---

## Question code

```c
#define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
```

## Short answer

**`##__VA_ARGS__` removes the trailing comma** when there are no variadic arguments.

With the GNU preprocessor, a call like `DBG("hi")` would leave a comma before the empty variadic argument without special handling; the GNU form removes that comma, producing `printf("hi")`.

This is a GNU extension, not portable standard syntax; C23 and C++20 provide `__VA_OPT__(,)`.[^gcc-cpp-variadic-macros]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-macros-0010
title: "Why is a statement macro wrapped in `do { ... } while(0)`?"
description: "Do-while-zero makes a multi-statement macro behave as a single statement that works correctly with if-else and semicolons."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
---

## Question code

```c
#define LOG_ERR(m) do { \
    uart_puts("[ERR] "); \
    uart_puts(m); \
} while (0)
```

## Short answer

**So that a multi-statement macro behaves as a single statement** and works correctly with `if/else` and a semicolon.

`do { ... } while(0)` forms a single block that requires a `;` at the call site, so `if (c) LOG_ERR(x); else ...` compiles correctly.

For a multi-action statement macro, this idiom preserves the expected `if/else` structure; a trailing backslash continues the preprocessor directive onto the next line.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

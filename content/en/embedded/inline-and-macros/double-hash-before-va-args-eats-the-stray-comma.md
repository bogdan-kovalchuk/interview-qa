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
#define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
```

## Short answer

**`##__VA_ARGS__` removes the trailing comma** when there are no variadic arguments.

Without `##`, a call like `DBG("hi")` would expand to `printf("hi", )` – a <span class="warn">syntax error</span> from the dangling comma. With `##` the comma disappears -> `printf("hi")`.

Rule: `##__VA_ARGS__` is a GNU extension (GCC/Clang); in C23/C++20 the portable equivalent is `__VA_OPT__(,)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

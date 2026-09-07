---
id: emb-macros-0041
title: "How do you generate a unique variable name from the line number?"
description: "Two macro levels are needed: an inner one expands LINE to a number, an outer one pastes it onto the prefix via ##."
track: embedded
section: inline-and-macros
level: junior
type: mechanism
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
#define CAT(a, b) a##b
#define XCAT(a, b) CAT(a, b)
#define UNIQUE(p) XCAT(p, __LINE__)
```

## Short answer

**Two levels are needed**: `CAT` pastes tokens, while `XCAT` first expands `__LINE__` into a number before pasting.

Then `int UNIQUE(tmp_);` on line 42 yields `int tmp_42;`. Used for scope guards, RAII helpers, test macros.

Rule: for both `#` and `##` with built-in macros an extra indirection level is always required.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-cemb-0019
title: "What is the purpose of the `static` keyword?"
description: "static changes the lifetime of a local variable, the linkage of a global variable or function, and how a C++ class member is shared."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Embedded Engineer interview questions (community Anki deck)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of this question and answer; the answer text is not independently verified against the original community Anki deck."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

Depending on context, `static` does three different things:[^dou-embedded-interview]

1. **Local variable** – retains its value between function calls, lives for the entire program lifetime, and is not placed on the stack.
2. **Global variable or function** – restricts visibility to the current file (internal linkage) and prevents name conflicts between `.c` files.
3. **C++ class member** – has a single copy for the entire class, not a separate copy for each object.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

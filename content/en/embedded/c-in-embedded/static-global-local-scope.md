---
id: emb-cemb-0020
title: "How does `static` affect global and local variables?"
description: "For a local variable, static changes lifetime; for a global variable or function, it gives the name internal linkage within the current file."
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

For a **local variable**, `static` changes the lifetime: the variable is created once, lives until the program ends, and retains its value between function calls. The scope remains local to the block.

For a **global variable** or function, `static` changes the linkage: the name is visible only in the current `.c`/`.cpp` file. This is called internal linkage and helps avoid name conflicts between translation units.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

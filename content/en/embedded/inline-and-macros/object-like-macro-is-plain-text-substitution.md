---
id: emb-macros-0002
title: "How does an object-like macro differ from an ordinary constant?"
description: "An object-like macro is plain text substitution with no type and no scope, visible from the define site to end of file."
track: embedded
section: inline-and-macros
level: junior
type: concept
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
#define BUFFER_SIZE 256
```

## Short answer

**An object-like macro is plain text substitution**: wherever `BUFFER_SIZE` appears, the preprocessor inserts `256`.

Unlike a `const` variable, a macro <span class="warn">has no type and no scope</span> – it is visible from the `#define` site to the end of the file (or `#undef`) and ignores blocks, functions and namespaces.

Rule: for named constants in C++ and modern C, `const`/`constexpr`/`enum` are usually preferable because they are type-safe and visible to the debugger.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

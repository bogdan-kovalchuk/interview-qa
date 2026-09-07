---
id: emb-volconst-0042
title: "Trap: why does `const` in C not mean compile-time constant everywhere?"
description: "In C, const means a read-only object through that identifier, but not always an integer constant expression."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

## Short answer

<span class="warn">In C, `const` means a read-only object through that identifier, but not always an integer constant expression.</span>

For example, a file-scope `const int n = 10;` in C cannot be used everywhere as the size of a static array where a compile-time constant expression is required. In C++, the rules differ. For C embedded code, `enum`, `#define`, or linker symbols are often used for compile-time constants.

Protection: do not confuse object immutability with a preprocessor or translation-time constant.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

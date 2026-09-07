---
id: emb-macros-0016
title: "How does `#pragma once` differ from a classic include guard?"
description: "Pragma once gives the same protection as an include guard in one line but is not part of the C or C++ standard."
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

## Short answer

**`#pragma once` gives the same protection in a single line** at the top of the file, without the risk of guard macro name collisions.

Downside: it is <span class="warn">not part of the C/C++ standard</span>, although it is supported by GCC, Clang, MSVC and IAR. A classic `#ifndef` guard is more portable and works even with unusual file systems and symlinks.

Rule: for maximum portability use an `#ifndef` guard; for convenience in a known toolchain `#pragma once` is acceptable.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

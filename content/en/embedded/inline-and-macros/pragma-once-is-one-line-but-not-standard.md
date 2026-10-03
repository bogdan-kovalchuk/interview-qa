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
  - source_id: gcc-once-headers
    title: "GCC: Once-Only Headers"
    url: https://gcc.gnu.org/onlinedocs/cpp/Once-Only-Headers.html
    accessed: 2026-10-04
    kind: official
    version: "GCC 16.1"
    applicability: "GCC documentation describes #pragma once behavior in this toolchain and notes that it is less portable than #ifndef."
  - source_id: msvc-once
    title: "Microsoft Learn: once pragma"
    url: https://learn.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-170
    accessed: 2026-10-04
    kind: official
    version: "MSVC 170"
    applicability: "Documents #pragma once behavior and limits in MSVC; this does not establish behavior in other compilers."
---

## Short answer

**`#pragma once` asks the compiler to include a header at most once** per translation unit, without a separate guard macro.

Downside: the directive <span class="warn">does not have this behavior standardized by C or C++</span>, so support depends on the compiler. A classic `#ifndef` guard uses standard conditional directives and is more portable.

Check your toolchain documentation for support and include-path behavior before choosing it.[^gcc-once-headers] [^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

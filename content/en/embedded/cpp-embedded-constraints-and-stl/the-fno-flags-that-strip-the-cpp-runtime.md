---
id: emb-cppstl-0019
title: "What are the key compilation flags for embedded C++?"
description: "Flags like -fno-exceptions, -fno-rtti, -fno-threadsafe-statics, -fno-use-cxa-atexit and -fno-unwind-tables strip heavy runtime features."
track: embedded
section: cpp-embedded-constraints-and-stl
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

**`-fno-exceptions`, `-fno-rtti`, `-fno-threadsafe-statics`, `-fno-use-cxa-atexit`, `-fno-unwind-tables`.**

They strip: exceptions, RTTI, the mutex on static initialization (pthread), destructor registration via `__cxa_atexit`, and `.eh_frame` tables. Often combined with `-Os` and `-std=c++17`.

Rule: these flags make C++ deterministic and compact on bare metal.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

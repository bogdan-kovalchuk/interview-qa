---
id: emb-cppstl-0008
title: "Trap: why is overriding the global `operator new` with a pool allocator dangerous?"
description: "Overriding global operator new silently changes the semantics of every allocation"
track: embedded
section: cpp-embedded-constraints-and-stl
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
  - source_id: iso-cpp-n4861
    title: "C++ International Standard working draft N4861"
    url: https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/n4861.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N4861"
    applicability: "Authoritative section-level reference for the C++ language rules involved; freestanding and vendor toolchains can differ."
---

## Short answer

<span class="warn">It silently changes the semantics of EVERY allocation, including third-party libraries.</span>

Any code that calls `new` anywhere inside (even library code) will suddenly go through your pool – with unpredictable consequences for size/timing.

Defence: it is safer to `= delete` the global `operator new` entirely, so that an accidental heap allocation becomes a compile error.[^embeddedinterviewlab]

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

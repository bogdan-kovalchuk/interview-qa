---
id: emb-cppoop-0009
title: "Trap: why can merely declaring a destructor inflate ROM?"
description: "A global object's destructor can pull atexit/cxaatexit infrastructure into the linker, wasting ROM bytes."
track: embedded
section: cpp-classes-and-oop
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

<span class="warn">A destructor of a global object can force the linker to pull in the `atexit()`/`__cxa_atexit` runtime cleanup infrastructure</span> – extra ROM bytes.

For global objects, the compiler must register the dtor to call it at program exit. In bare-metal firmware, exit often never happens, so this infrastructure is unnecessary.

Protection: avoid non-trivial destructors in global objects; if needed, configure the toolchain (`-fno-use-cxa-atexit`) or keep objects "eternal".[^embeddedinterviewlab]

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

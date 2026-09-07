---
id: emb-cppstl-0017
title: "What is name mangling and why does it make `extern \"C\"` necessary?"
description: "C++ encodes the function signature into the symbol for overload resolution, so cross-language interfaces require C linkage."
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

**C++ encodes the signature into the symbol (for overload resolution): `sensor_read(uint8_t)` -> `_Z10sensor_readh`; C does not mangle.**

Without `extern "C"` the linker looks for the mangled name and does not find the unmangled C symbol -> link error.

Rule: mangling is the reason a cross-language interface requires C linkage.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-cppstl-0021
title: "What does `-fno-use-cxa-atexit` do and why is it fine on an MCU?"
description: "It skips registering global object destructors via cxaatexit since MCU programs never exit."
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

**It does not register global object destructors via `__cxa_atexit`.**

On an MCU the program usually never exits, so global destructors are not needed – registration only pulls in runtime infrastructure and ROM.

Rule: static objects on an MCU are "eternal"; `-fno-use-cxa-atexit` removes unnecessary cleanup.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

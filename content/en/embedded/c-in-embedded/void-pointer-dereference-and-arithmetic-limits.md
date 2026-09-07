---
id: emb-cppfound-0014
title: "What is void* and what limitations does this pointer type have?"
description: "A type-erased pointer that can hold any object address but cannot be dereferenced or used in arithmetic without a cast."
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
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**void*** – a type-erased pointer: it can hold the address of an object of any type without an explicit cast.

Limitations:
- <span class="warn">Cannot be dereferenced</span> without a cast: `*p` – compilation error;
- <span class="warn">Cannot undergo arithmetic</span> without a cast (C standard). GCC allows it as an extension (element size = 1 byte).

Uses: `malloc`/`free`, `memcpy`/`memset`, generic callbacks, `qsort`. In embedded: generic ISR handler tables.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

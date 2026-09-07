---
id: emb-cppfound-0043
title: "What value does `&arr` return, and how does it differ from `arr` when `int arr[8]`?"
description: "arr and &arr share an address but have different pointer types."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
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

Both expressions yield the **same numeric address** (the address of the first element of the array), but have different **types**:

`arr` -> decays to `int*`. `arr+1` -> +4 bytes (one int). `&arr` -> `int(*)[8]` (pointer to array). `&arr+1` -> +32 bytes (one array).

In practice: `&arr` is used to pass to a function that expects `int(*)[8]` – it preserves the array size in the type.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

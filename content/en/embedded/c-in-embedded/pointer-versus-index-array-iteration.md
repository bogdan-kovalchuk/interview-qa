---
id: emb-cppfound-0094
title: "What is the efficient way to iterate through an array with a pointer versus an index?"
description: "How optimized compilers usually treat pointer and index iteration."
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

Pointer iteration: `for(int *p=arr; p!=arr+n; p++) use(*p);` Index iteration: `for(int i=0; i<n; i++) use(arr[i]);`

With modern optimizing compilers (`-O2`): **the code is usually identical** – the compiler converts between forms on its own.

However: pointer iteration avoids recomputing the base address (`arr + i` each time). Without optimization, pointer iteration can be faster. In embedded (no optimization): pointer iteration is more efficient for Cortex-M0.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

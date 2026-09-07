---
id: emb-cppfound-0038
title: "What is a wild pointer and how does it differ from a NULL or dangling pointer?"
description: "The distinction between wild, NULL, and dangling pointers."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Wild pointer** – an uninitialized pointer with a garbage value (a random address from the stack).

Comparison:
- **NULL pointer**: explicitly invalid address 0, can be checked;
- **Dangling pointer**: pointed to a valid object that has been destroyed;
- **Wild pointer**: never pointed to a valid object.

All three -> undefined behavior when dereferenced. A wild pointer is the most dangerous: its address is non-zero and random, so it passes the `if(p != NULL)` check.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

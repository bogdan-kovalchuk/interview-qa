---
id: emb-cppfound-0012
title: "In which three contexts does an array not decay to a pointer?"
description: "The three contexts where an array does not decay to a pointer: sizeof, address-of, and string literal initialization."
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

An array stays an array and **does not decay** in three cases:

1. `sizeof(arr)` – returns the total size of the array in bytes, not the pointer size;
2. `&arr` – returns a pointer to the array `int(*)[N]`, not `int*`;
3. String literal initialization: `char arr[] = "hi"` – copies the characters into the array.

Remember these three exceptions – they come up often in interviews.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

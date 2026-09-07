---
id: emb-cppfound-0065
title: "What is the memory difference between `int *arr[5]` and `int (*arr)[5]`?"
description: "How an array of pointers differs from a pointer to an array."
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

`int *arr[5]` is an array of 5 pointers. Size: `5 × sizeof(int*) = 20 bytes`; each of the 5 elements is an address of some int and can point to different memory locations.

`int (*arr)[5]` is a single pointer to an array of 5 int. The size of `arr` = `sizeof(int*) = 4` bytes; `arr+1` -> offset by `5 × sizeof(int) = 20` bytes.

Reading rule: parentheses around `*arr` mean "pointer to".[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

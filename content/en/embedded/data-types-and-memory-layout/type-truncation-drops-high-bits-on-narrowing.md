---
id: emb-dtypes-0039
title: "What is type truncation, and when does it happen?"
description: "Type truncation drops the high bits when a wider type is assigned to a narrower one, e.g. int into uint8t."
track: embedded
section: data-types-and-memory-layout
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
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

**Type truncation** is dropping the high bits when a wider type is assigned to a narrower one.

Example: `int x = 300; uint8_t y = x;` -> `300 = 0x012C`, drop `0x01`, leaving `0x2C = 44`.

It occurs on assignment, on function return, and when passing a smaller-type argument. Implicit truncation often produces no warning without `-Wall -Wconversion`. Always check the range before narrowing.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-dtypes-0030
title: "What does this return? `uint16_t x = 60000; x += 10000;`"
description: "Unsigned overflow is defined as modular arithmetic, so 60000+10000 gives 4464 rather than undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: mechanism
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

`x = 4464`: `uint16_t` has the range `0..65535`, and `60000 + 10000 = 70000` goes out of range.

Unsigned overflow is **defined by the standard** as modular arithmetic: `70000 mod 65536 = 4464` – this is NOT undefined behavior (unlike signed overflow).

But if `70000` was expected, it is a bug from the wrong type choice; use `uint32_t`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

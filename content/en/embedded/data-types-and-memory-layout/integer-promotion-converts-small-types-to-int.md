---
id: emb-dtypes-0014
title: "What is integer promotion in C?"
description: "Integer promotion automatically converts narrow integer types to int before arithmetic."
track: embedded
section: data-types-and-memory-layout
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

Integer promotion is the **automatic conversion** of `char`, `short`, `uint8_t`, `int16_t`, and similar types to `int` before arithmetic operations (C standard §6.3.1.1).

Example: `uint8_t a = 200, b = 100;` -> before `+` both become `int`, the sum is 300 (as `int`), then truncated to `uint8_t` = 44.

Promotion always happens, regardless of the programmer's intent.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

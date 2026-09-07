---
id: emb-structs-0040
title: "Trap: why is `memcmp(&a, &b, sizeof a)` a bad way to compare structs?"
description: "Padding bytes may differ even when all fields are equal."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
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
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

<span class="warn">Because padding bytes may differ even when all fields are equal.</span> Padding is not a logical part of the struct state and may contain old stack bytes or different values after different initialization paths, so `memcmp` (which compares raw bytes) may return "not equal" for structs with identical member values.

Defence: compare fields explicitly or normalize the serialization format. For security-sensitive output do not leak padding bytes externally.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

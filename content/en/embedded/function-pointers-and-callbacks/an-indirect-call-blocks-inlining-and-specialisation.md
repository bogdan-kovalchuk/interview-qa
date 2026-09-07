---
id: emb-fnptr-0056
title: "Why do function pointers affect optimisation?"
description: "An indirect call is harder to optimise than a direct call."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: concept
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

**An indirect call is harder to optimise than a direct call.**

The compiler often does not know the exact callee function, so it cannot inline it, remove unused branches inside the callee or build an accurate call graph. LTO sometimes helps when the table is static and visible, but the guarantees are weaker.

Embedded conclusion: function pointers give flexibility but can increase code size and latency; in hot paths evaluate the generated assembly.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

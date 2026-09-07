---
id: emb-patterns-0019
title: "Why is `ERR_OK` always zero?"
description: "So that zero means success and any non-zero value means an error"
track: embedded
section: common-code-patterns
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

**So that `0` means success and any non-zero value means an error** (truthiness).

Then `if (result) { handle_error(); }` and `if (sensor_read(...) != ERR_OK)` work naturally. This is the typical convention of a HAL (hardware abstraction layer) and many POSIX-like APIs (application programming interface): 0 = success, non-zero/negative value = error.

Rule: in an error enum `ERR_OK = 0` comes first; real codes are non-zero.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

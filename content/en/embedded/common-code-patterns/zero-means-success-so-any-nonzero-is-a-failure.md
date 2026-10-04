---
id: emb-patterns-0019
title: "Why do many APIs use zero for `ERR_OK`?"
description: "So that zero means success and any non-zero value means an error"
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
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

Rule: in an error enum `ERR_OK = 0` comes first; real codes are non-zero.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

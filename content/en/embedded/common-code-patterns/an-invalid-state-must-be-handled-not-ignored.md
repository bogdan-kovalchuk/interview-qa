---
id: emb-patterns-0006
title: "Why must a state machine handle the default or invalid state?"
description: "An invalid state or unexpected event must be handled explicitly rather than silently ignored."
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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

**An unexpected state or event should be handled explicitly, not silently skipped.**

Corrupted data or external input can produce a value outside the valid state set. A missing `default` is not itself necessarily undefined behavior, but indexing a table without checking bounds can cause an out-of-bounds access.[^iso-c-n1570]

Add a `default`/error handler and check bounds before accessing the transition table.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

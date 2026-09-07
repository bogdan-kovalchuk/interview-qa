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

**An invalid state or unexpected event must be handled explicitly, not silently ignored.**

Memory corruption, a bug or external input can produce a state outside the `enum`; without a `default` handler this leads to undefined behavior or out-of-bounds access in the table.

Rule: always have a default branch/handler and a bounds check on the state index.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

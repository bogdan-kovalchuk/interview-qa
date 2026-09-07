---
id: emb-fnptr-0053
title: "Trap: why are weak hooks worse than an explicit callback for several driver instances?"
description: "A weak function has one global name and carries no per-instance context."
track: embedded
section: function-pointers-and-callbacks
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

<span class="warn">A weak function has one global name and carries no per-instance context.</span>

If there are two UARTs or two timers, one weak hook does not know which object the event belongs to unless this is passed separately. Also, a weak override is hidden at the linker level, which complicates testing and dependency tracking.

Defence: for reusable drivers use explicit registration `cb + ctx`; keep weak hooks for startup defaults or board-level extension points.[^embeddedinterviewlab]

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

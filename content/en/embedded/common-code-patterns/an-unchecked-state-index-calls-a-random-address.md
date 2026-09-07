---
id: emb-patterns-0040
title: "Trap: what happens if a state machine does not check the state index before `handlers[state]`?"
description: "An invalid or corrupted state causes an out-of-bounds read and an indirect call at a random address, likely a HardFault."
track: embedded
section: common-code-patterns
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

<span class="warn">Invalid/corrupted state -> out-of-bounds table read and an indirect call at a random address</span> (likely a HardFault).

Data becomes control flow, so a state from external input or corruption directly controls which function is called.

Defense: `if (state < ARRAY_SIZE(handlers) && handlers[state]) handlers[state](evt); else on_error();`[^embeddedinterviewlab]

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

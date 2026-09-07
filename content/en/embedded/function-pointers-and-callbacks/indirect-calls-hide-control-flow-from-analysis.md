---
id: emb-fnptr-0045
title: "Trap: why is a function pointer state machine harder to analyse?"
description: "Indirect calls hide control flow from the reader, the debugger and some static analysers."
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

<span class="warn">Indirect calls hide control flow from the reader, the debugger and some static analysers.</span>

Instead of an explicit `switch`, you see only `handlers[state](...)`. If the table is initialised at runtime or modified, it is harder to prove which functions can be called. This can affect safety certification and MISRA checks.

Defence: make tables `static const`, name handlers explicitly, check state bounds and document the transition table.[^embeddedinterviewlab]

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

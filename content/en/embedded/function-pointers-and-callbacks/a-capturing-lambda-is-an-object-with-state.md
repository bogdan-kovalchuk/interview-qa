---
id: emb-fnptr-0038
title: "Trap: why can a capturing lambda not be passed directly as `void (*)(void)`?"
description: "A capturing lambda is an object with state, not just a function address."
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

<span class="warn">A capturing lambda is an object with state, not just a function address.</span>

It needs storage for captured variables and is invoked through `operator()`. A C function pointer has no room for state, so the compiler cannot implicitly convert a capturing lambda to `void (*)(void)`.

Protection: pass state through `void *ctx`, or use a C++ callback abstraction if embedded constraints allow.[^embeddedinterviewlab]

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

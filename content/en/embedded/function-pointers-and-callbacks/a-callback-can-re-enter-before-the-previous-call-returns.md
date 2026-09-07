---
id: emb-fnptr-0051
title: "Trap: why can a callback be a reentrancy problem?"
description: "A callback can be called again before the previous invocation has finished."
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

<span class="warn">A callback can be called again before the previous invocation has finished.</span>

For example, a UART RX interrupt can arrive while the previous byte is still being handled, or a callback can call an API that synchronously triggers a new callback. If the callback uses a static local buffer without protection, state can be corrupted.

Defence: document reentrancy, minimise shared mutable state, use queues or critical sections, or forbid nested callbacks by design.[^embeddedinterviewlab]

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

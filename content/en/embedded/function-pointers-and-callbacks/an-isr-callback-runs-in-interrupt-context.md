---
id: emb-fnptr-0026
title: "Why must a callback invoked from an ISR be short?"
description: "The ISR callback runs in interrupt context where the system must not be blocked for long."
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

**The ISR callback runs in interrupt context**, where the system must not be blocked for long.

A long callback increases interrupt latency, can break real-time deadlines and is often not allowed to call blocking RTOS or API functions. If the callback is registered by user code, the driver must explicitly document that it is called from an ISR.

Rule: an ISR callback should quickly save the event or wake a task; heavy work belongs in thread or main context.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

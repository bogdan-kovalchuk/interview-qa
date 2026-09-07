---
id: emb-fnptr-0027
title: "Trap: what is unsafe about calling `printf` from an ISR callback?"
description: "printf is usually not ISR-safe and may be blocking or reentrant-unsafe."
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

<span class="warn">`printf` is usually not ISR-safe and may be blocking or reentrant-unsafe.</span>

It may take a lock, use the heap, wait for UART TX or modify global state. In interrupt context this can cause deadlock, jitter or corrupt output, especially if the main code also prints.

Protection: in the ISR callback set a flag, write to a lock-free or ring buffer, or use a dedicated non-blocking trace backend.[^embeddedinterviewlab]

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

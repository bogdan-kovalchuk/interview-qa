---
id: emb-structs-0041
title: "Trap: how can padding become an information leak?"
description: "Sending or writing raw struct bytes can leak old stack or RAM data through padding."
track: embedded
section: structs-unions-and-bitfields
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

<span class="warn">If you send or write raw bytes of a struct, padding may contain old data from the stack/RAM.</span>

For example, `send(fd, &msg, sizeof msg)` may include padding bytes between fields. These bytes are not initialized by individual field assignments and may contain fragments of previous variables.

Mitigation: zero-initialize the struct before populating it, serialize fields explicitly, and do not export raw struct layout as a security boundary.[^embeddedinterviewlab]

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

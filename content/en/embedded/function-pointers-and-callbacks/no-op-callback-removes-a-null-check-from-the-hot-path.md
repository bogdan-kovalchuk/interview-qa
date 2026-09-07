---
id: emb-fnptr-0010
title: "For an optional callback, is a `NULL` check or a no-op function better?"
description: "Both options are valid, but a no-op callback can simplify the hot path."
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

Both options are valid, but a no-op callback can simplify the hot path.

If the callback is optional and called frequently, the driver can initialize it with `static void noop(void *ctx) { (void)ctx; }`. Then the call site has no `if (cb)` branch. But this must be documented so the callback pointer is never left uninitialized.

Rule: for a simple API a `NULL` check is clearer; for a performance-critical dispatch table a no-op entry may be better.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

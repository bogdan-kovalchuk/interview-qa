---
id: emb-fnptr-0035
title: "Can a callback be a `static` function?"
description: "Yes; static at file scope limits linkage but the address can still be passed as a callback."
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

**Yes.**

`static` at file scope limits the function's linkage to the current `.c` file, but its address can still be passed as a callback within that translation unit. This is even preferable for private handlers that should not be part of the public symbol table.

Rule: a callback must be visible where its address is passed; external linkage is needed only if another translation unit must refer to the function name directly.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

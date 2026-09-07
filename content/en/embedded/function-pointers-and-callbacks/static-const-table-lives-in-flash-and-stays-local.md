---
id: emb-fnptr-0022
title: "Why should a function pointer table be `static const`?"
description: "static const makes the table file-local and read-only so it can reside in Flash or .rodata."
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

**`static const`** makes the table file-local and read-only, so it can reside in Flash/`.rodata`.

For an MCU this saves RAM and protects the mapping from accidental runtime overwrite. If the table never needs to change after build time, a mutable global array is an unnecessary risk.

Example: `static const cmd_handler_t handlers[] = { cmd_ping, cmd_reset };`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

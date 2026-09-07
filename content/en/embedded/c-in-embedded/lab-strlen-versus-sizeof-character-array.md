---
id: emb-cppfound-0070
title: "What do `strlen(s)` and `sizeof(s)` return for `char s[20] = \"hello\"`?"
description: "The difference between string length and character-array capacity."
track: embedded
section: c-in-embedded
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-07
content_revision: 4
reconciled_with:
  uk: 2
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
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

`strlen(s)` -> **5**: counts characters up to '\0' (not including it) – a runtime function.

`sizeof(s)` -> **20**: the array size declared at compile time – the entire buffer, regardless of content. A compile-time operation.

The string "hello" occupies 6 bytes (`h,e,l,l,o,\0`), the remaining 14 bytes are zeros (due to `= "hello"` array initialization); `sizeof(s)/sizeof(s[0]) = 20/1 = 20` – the buffer capacity.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

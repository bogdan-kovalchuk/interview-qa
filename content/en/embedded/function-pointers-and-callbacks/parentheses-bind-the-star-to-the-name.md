---
id: emb-fnptr-0002
title: "How do you read the declaration `void (*handler)(int)`?"
description: "handler is a pointer to a function that takes int and returns void."
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

**`handler` is a pointer to a function that takes `int` and returns `void`.**

The parentheses around `*handler` are critical: they say the pointer belongs to the name `handler`, not to the return type. Without the parentheses it would be a different declaration.

Reading rule: start from the name. `handler` is pointer to function taking `int` returning `void`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

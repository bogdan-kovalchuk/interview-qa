---
id: emb-fnptr-0015
title: "What does the function parameter `void cb(int)` mean in a declaration?"
description: "In function parameters a function type adjusts to a function pointer automatically."
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

## Question code

```c
void register_cb(void cb(int));
```

## Short answer

In function parameters it adjusts to a function pointer: nearly equivalent to `void register_cb(void (*cb)(int));`.

Functions are not passed by value. A function-type parameter in a function prototype is automatically converted to a pointer to function. This is similar to an array parameter, which decays to a pointer.

Rule: for clarity in callback APIs, prefer pointer syntax or a typedef.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-fnptr-0004
title: "What does this typedef mean?"
description: "timercbt is a pointer-to-function type that takes a void context pointer and returns void."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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
typedef void (*timer_cb_t)(void *ctx);
```

## Short answer

**`timer_cb_t`** is a pointer-to-function type that takes `void *ctx` and returns `void`.

After this you can write `timer_cb_t cb;`, `void timer_start(timer_cb_t cb, void *ctx);`. Such a typedef dramatically reduces noise in driver APIs and makes the callback contract visible.

Embedded rule: declare the callback type once in a header rather than duplicating raw function pointer syntax in every function.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

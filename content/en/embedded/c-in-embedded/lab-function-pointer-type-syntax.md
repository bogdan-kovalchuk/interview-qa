---
id: emb-cppfound-0079
title: "How do you declare a pointer to a function taking `int` and returning `void`?"
description: "How to read and write a C function-pointer declaration."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 3
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

`void (*fp)(int);` – this declaration means a pointer to a function. Reading: `fp` is a pointer (`*fp`) to a function (`(*fp)(int)`) that returns void. For convenience – `typedef`:

```c
typedef void (*callback_t)(int);
callback_t fp = my_func;
```

Without typedef for an array: `void (*table[8])(int);` – an array of 8 function pointers; call with `fp(42);` or `(*fp)(42);` – both are valid.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

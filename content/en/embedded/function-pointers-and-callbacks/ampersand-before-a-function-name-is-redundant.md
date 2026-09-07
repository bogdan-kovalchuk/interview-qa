---
id: emb-fnptr-0008
title: "Do you need the `&` operator when assigning a function to a function pointer?"
description: "Usually no, because the function designator decays to a function pointer automatically."
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

**Usually no.**

`cb = foo;` and `cb = &foo;` have the same effect for a regular function: the function designator decays to a pointer to function. Likewise, when calling `cb()` you don't need to write `(*cb)()` explicitly, although that is also valid.

Rule: in production C the short style `cb = foo;` and `cb(arg);` is more common.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

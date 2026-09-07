---
id: emb-fnptr-0039
title: "How does a C++ pointer to member function differ from an ordinary function pointer?"
description: "A pointer to member function needs an object instance to be called."
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

**A pointer to member function needs an object instance to be called.**

`void (Class::*pmf)()` is not compatible with `void (*)()`. A non-static method has a hidden `this`, so it cannot be passed directly to a C API that expects a free function pointer.

Rule: for a C callback from a C++ class use a static member function wrapper and pass `this` through a context pointer.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

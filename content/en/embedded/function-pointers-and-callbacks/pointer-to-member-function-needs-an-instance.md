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
updated: 2026-10-04
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
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: cpp-member-pointer
    title: "C++ working draft: Pointers to members and pointer-to-member operators"
    url: https://eel.is/c++draft/dcl.mptr
    accessed: 2026-10-04
    kind: spec
    version: "current working draft"
    applicability: "Defines the distinct pointer-to-member type and applying it to an object; it does not specify a platform's physical representation."
---

## Short answer

**A pointer to member function needs an object instance to be called.**

`void (Class::*pmf)()` has a distinct type from `void (*)()`: the first is a pointer to member, while the second is a pointer to function. A pointer to member is applied to an object with `.*` or `->*`, then the result is called.[^cpp-member-pointer]

For a C callback from a C++ class, use a static member-function wrapper and pass `this` through a context pointer; a static member function can have an ordinary function pointer type.[^cpp-member-pointer]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

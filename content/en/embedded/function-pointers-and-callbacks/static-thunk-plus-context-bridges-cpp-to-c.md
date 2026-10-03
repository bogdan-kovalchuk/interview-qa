---
id: emb-fnptr-0041
title: "How do you make a C callback for a C++ object?"
description: "Use a static thunk plus a context pointer."
track: embedded
section: function-pointers-and-callbacks
level: junior
type: mechanism
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
  - source_id: cppreference-member-pointers
    title: "cppreference: Pointers"
    url: https://en.cppreference.com/w/cpp/language/pointer
    accessed: 2026-10-04
    kind: book
    version: null
    applicability: "Explains C++ function and member pointer types; it does not define requirements of a particular HAL callback API."
---

## Short answer

Use a static thunk plus a context pointer.

`static void thunk(void *ctx, uint8_t b) { static_cast<App *>(ctx)->on_rx(b); }` `uart_register(thunk, this);`

A static member function has no hidden `this` and is compatible with a plain function pointer if the signature matches. `ctx` restores the object instance manually.

Rule: this is the standard bridge between a C HAL and C++ class design.[^cppreference-member-pointers]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

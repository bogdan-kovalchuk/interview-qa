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
---

## Short answer

**For an ordinary function-pointer assignment, the `&` operator is optional.**

`cb = foo;` and `cb = &foo;` have the same effect for a compatible function: the function designator converts to a pointer to function, while `&foo` explicitly takes the function's address.[^iso-c-n1570] Likewise, both `cb()` and `(*cb)()` are permitted call forms.


## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

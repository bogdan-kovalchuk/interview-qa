---
id: emb-fnptr-0035
title: "Can a callback be a `static` function?"
description: "Yes; static at file scope limits linkage but the address can still be passed as a callback."
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

**Yes.**

`static` at file scope gives the function internal linkage, but its address can still be passed as a callback within the same translation unit. Another translation unit cannot refer to its name, but a callback that has received the address can call it.[^iso-c-n1570]

For example, a file-scope `static` handler can be passed to a local driver or scheduler without exporting its name to other translation units. `static` does not change the function or pointer type; it restricts the linkage of the name.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

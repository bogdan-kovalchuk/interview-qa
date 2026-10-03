---
id: emb-volconst-0056
title: "What does `static const` mean for a table inside a C file?"
description: "static limits linkage to this translation unit and const makes the data read-only through this identifier."
track: embedded
section: volatile-and-const
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

**At file scope, `static` gives the identifier internal linkage, and `const` prevents modification through that identifier.**

For an embedded lookup table this is a common form: other translation units cannot see the symbol, and the compiler may place the table in a read-only section. Placement in Flash depends on the linker script and platform.

Rule: declare file-private immutable tables as `static const` unless they must be part of the external ABI.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

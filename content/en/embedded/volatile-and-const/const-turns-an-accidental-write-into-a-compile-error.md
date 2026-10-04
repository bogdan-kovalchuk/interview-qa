---
id: emb-volconst-0061
title: "How does `const` help the compiler catch mistakes?"
description: "const turns an accidental write into a compile-time error when the access goes through a const-qualified type."
track: embedded
section: volatile-and-const
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
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

**`const` lets the compiler diagnose a write through a const-qualified lvalue.** In C, this violates a language constraint, for which an implementation must issue a diagnostic; the standard does not require every such diagnostic to stop the build.[^iso-c-n1570]

For example, a parser with `const uint8_t *frame` cannot modify a byte through that pointer. This type restriction does not make memory physically read-only or configure the MPU.

Rule: `const` documents a read-only access contract and helps diagnose mistaken assignments; it is not hardware memory protection.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-volconst-0031
title: "How do `const char *p = \"OK\"` and `char p[] = \"OK\"` differ?"
description: "const char p points to a read-only string literal, while char p[] creates a mutable array with a copy of the characters."
track: embedded
section: volatile-and-const
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
---

## Short answer

**`const char *p` points to a read-only string literal, while `char p[]` creates a mutable array with a copy of the characters.**

In the first case, `p[0] = 'N'` is forbidden by the type. In the second case, the array holds `'O'`, `'K'`, `'\0'` in its own storage, and `p[0] = 'N'` is allowed.

Embedded implication: the literal may reside in Flash, while a mutable array typically requires RAM.[^iso-c-n1570]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

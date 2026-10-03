---
id: emb-volconst-0042
title: "Trap: why does `const` in C not mean compile-time constant everywhere?"
description: "In C, const means a read-only object through that identifier, but not always an integer constant expression."
track: embedded
section: volatile-and-const
level: junior
type: pitfall
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

<span class="warn">In C, `const` restricts modification through that identifier, but the object’s value does not become an integer constant expression.</span>[^iso-c-n1570]

For example, `const int n = 10;` is not an integer constant expression in C and cannot serve as the size of an ordinary file-scope array where one is required. C++ rules differ. In C, an integer constant, `enum`, or `#define` is commonly used for a fixed size.

Protection: do not confuse restricted writes through `const` with the language requirement for an integer constant expression.[^iso-c-n1570]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

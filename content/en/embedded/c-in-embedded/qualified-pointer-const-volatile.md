---
id: emb-cppfound-0092
title: "What is a qualified pointer with volatile or const, and how does the qualifier apply?"
description: "How const and volatile qualifiers affect pointed-to data and pointer use."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
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
    applicability: "Origin of the question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for c in embedded concepts; details of specific devices and toolchains can differ."
---

## Short answer

A qualifier is part of the pointer type that indicates properties of the data or the pointer itself.

`const int *p` – qualifier on the data: `*p` cannot be modified. You can assign a less qualified pointer to a more qualified one: `int *p` -> `const int *q = p` (adding const is OK), the reverse -> warning/error.

`volatile uint32_t *reg` – every access is actually performed (for registers).

Rule: you can **add** a qualifier on assignment, but <span class="warn">not remove</span> one without an explicit cast.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

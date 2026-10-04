---
id: emb-patterns-0032
title: "How does an FSM on a function-pointer table scale?"
description: "A function-pointer table separates FSM state dispatch from handlers, while a new state still requires coordinated table and transition updates"
track: embedded
section: common-code-patterns
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

**A function-pointer table maps each FSM state to its handler; adding a state requires coordinated updates to the enum, table, and transitions.**

This separates dispatch from handler logic, but does not automatically avoid changes elsewhere. Whether a `static const` table resides in Flash depends on the MCU, compiler, and linker script.[^iso-c-n1570]

Validate the state index and ensure the selected handler pointer is non-null before calling it.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

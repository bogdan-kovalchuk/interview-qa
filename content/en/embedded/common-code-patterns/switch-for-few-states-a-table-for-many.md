---
id: emb-patterns-0029
title: "When do you choose enum plus switch and when a function-pointer table for an FSM?"
description: "enum+switch for few states with debug simplicity and warnings on missing cases"
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-08
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
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
---

## Short answer

**enum+switch** – about eight states or fewer, debug simplicity matters, and warnings on missing cases.

Function-pointer table – many states, O(1) dispatch is needed, and states are added without changing existing code (table in Flash).

Rule: a small FSM (finite state machine) uses switch; a large or dynamic one uses a handler table with bounds check and default.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

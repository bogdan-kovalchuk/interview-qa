---
id: emb-patterns-0032
title: "How does an FSM on a function-pointer table scale?"
description: "A 12-state FSM for HVAC can add a defrost priority mode through one new handler and one table row"
track: embedded
section: common-code-patterns
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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

**For example, a 12-state FSM (finite state machine) for HVAC (heating, ventilation, and air conditioning) can add a "defrost priority" mode through one new handler function plus one table row**, without changing existing handlers.

This is the main advantage of the table: open/closed – you extend without modifying. The table is `static const` in Flash.

Rule: when states or commands are added frequently, a function-pointer table minimizes regression risk.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

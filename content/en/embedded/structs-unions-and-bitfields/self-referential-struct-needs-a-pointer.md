---
id: emb-structs-0037
title: "What is a self-referential struct and why does it need a pointer?"
description: "A self-referential struct contains a pointer to its own type, for example a linked list node."
track: embedded
section: structs-unions-and-bitfields
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

A **self-referential struct** contains a pointer to an object of its own type, for example a linked list node.

`struct Node { int value; struct Node *next; };` is valid because `next` has pointer size. But `struct Node next;` inside `Node` itself is impossible: it would require an infinite struct size.

Embedded use case: intrusive lists for RTOS queues, driver registries, free lists and memory pools.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

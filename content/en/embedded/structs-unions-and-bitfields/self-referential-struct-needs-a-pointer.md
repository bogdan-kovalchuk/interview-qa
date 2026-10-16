---
id: emb-structs-0037
title: "What is a self-referential struct and why does it need a pointer?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

A **self-referential struct** contains a pointer to an object of its own type, for example a linked list node.

`struct Node { int value; struct Node *next; };` is valid because `next` has pointer size. But `struct Node next;` inside `Node` itself is impossible: it would require an infinite struct size.

In embedded code, this structure can be a node in an intrusive list for an RTOS queue or memory pool; node lifetimes and links must be managed separately.[^iso-c-n1570]

## Detailed explanation

TODO

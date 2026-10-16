---
id: emb-structs-0038
title: "Trap: what is wrong with this definition?"
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

## Question code

```c
struct Node {
    int value;
    struct Node next;
};
```

## Short answer

<span class="warn">The struct contains itself by value, so its size would be infinite.</span>

The compiler cannot complete the layout: to know the size of `Node`, it needs the size of `next`, which is again `Node`. The allowed variant is a pointer: `struct Node *next;`.

Defence: for recursive data structures use a pointer or an index into a pool, not a nested object of the same type.[^iso-c-n1570]

## Detailed explanation

TODO

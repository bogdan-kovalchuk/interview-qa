---
id: emb-fnptr-0002
title: "How do you read the declaration `void (*handler)(int)`?"
track: embedded
section: function-pointers-and-callbacks
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**`handler` is a pointer to a function that takes `int` and returns `void`.**

The parentheses around `*handler` are critical: they say the pointer belongs to the name `handler`, not to the return type. Without the parentheses it would be a different declaration.

Reading rule: start from the name. `handler` is a pointer to a function taking `int` and returning `void`.[^iso-c-n1570]

## Detailed explanation

TODO

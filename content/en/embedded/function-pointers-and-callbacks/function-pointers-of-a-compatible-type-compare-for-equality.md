---
id: emb-fnptr-0054
title: "Can function pointers be compared?"
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

**Yes, function pointers of one compatible type can be compared for equality and inequality.**

This is useful for checking `cb != NULL` or for determining whether a default handler is registered. But ordering comparison such as `<` has no meaning for function pointers.

Rule: use function pointer comparison only for equality checks, not for sorting or range checks on code addresses.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-volconst-0016
title: "What does `const uint8_t *buf` mean in a function parameter?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

**The function receives a pointer to const `uint8_t`**: it can move the pointer, but it cannot change the buffer bytes through `buf`.

For example, `void uart_write(const uint8_t *buf, size_t len)` documents that the passed buffer will only be read. This allows passing both a mutable RAM buffer and a read-only flash table.

If a function is intended only to read data, `const T *` expresses that restriction in its interface; by itself, this type does not make the object immutable through other available access paths.[^iso-c-n1570]

## Detailed explanation

TODO

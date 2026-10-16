---
id: emb-align-0023
title: "How do you safely read a `uint32_t` from offset 3 in a `uint8_t` buffer (for example from DMA)?"
track: embedded
section: memory-alignment-and-endianness
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
uint32_t value;
memcpy(&value, &buf[3], sizeof value);
```

## Short answer

**Via `memcpy`, not a cast to `(uint32_t*)&buf[3]`.**

`&buf[3]` cannot safely be dereferenced as a `uint32_t*`: the address may not meet the type's alignment requirement, and support for unaligned accesses depends on the core and instruction. `memcpy` copies bytes into a separate, properly aligned object; it does not define the byte order in the buffer.

Guard: check the buffer length, copy into a local variable, and decode endianness separately for a wire format.[^iso-c-n1570]

## Detailed explanation

TODO

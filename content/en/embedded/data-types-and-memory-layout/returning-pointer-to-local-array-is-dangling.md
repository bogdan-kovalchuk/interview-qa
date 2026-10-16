---
id: emb-dtypes-0080
title: "Find the bug: `char* get_name(void) { char buf[32] = \"test\"; return buf; }`"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

When the block ends, a local array with automatic storage duration reaches the end of its lifetime, and C makes a pointer value to such an object indeterminate.[^iso-c-n1570] A function therefore cannot safely return a pointer for the caller to use to access `buf`; “stack” describes a common implementation, not a requirement of the standard.[^iso-c-n1570] Pass in a caller-owned buffer, return static storage with an explicit sharing model, or allocate memory with documented ownership.

## Detailed explanation

TODO

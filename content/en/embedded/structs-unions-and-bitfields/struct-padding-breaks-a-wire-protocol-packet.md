---
id: emb-structs-0006
title: "Trap: why can you not send `sizeof(struct)` bytes as a protocol packet?"
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

<span class="warn">Because struct layout and padding are implementation-dependent.</span>

Padding bytes can have indeterminate values; byte order for multibyte numbers and field offsets also depend on the platform and ABI. Writing a raw struct does not define a portable packet format.

Serialize fields explicitly into a buffer, specify byte order, and check the packet length. A `static_assert` can check the layout of one build, but does not make the format portable by itself.[^iso-c-n1570]

## Detailed explanation

TODO

---
id: emb-structs-0013
title: "Why can a pointer to a packed field be dangerous?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: gcc-attributes
    title: "GCC: Common Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Question code

```c
struct __attribute__((packed)) P {
    uint8_t tag;
    uint32_t value;
};

uint32_t *p = &pkt.value;
```

## Short answer

<span class="warn">`&pkt.value` can be an unaligned address for a `uint32_t *`.</span>

A plain `uint32_t *` carries the assumption that the address is sufficiently aligned for `uint32_t`. If the field is packed, this assumption can be false. Dereferencing such a pointer can be undefined behavior or a fault on an MCU.

Defense: do not take a pointer to packed multi-byte fields; use `memcpy(&tmp, &pkt.value, sizeof tmp)` or a byte parser.[^gcc-attributes]

## Detailed explanation

TODO

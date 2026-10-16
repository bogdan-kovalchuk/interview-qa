---
id: emb-align-0009
title: "What does `__attribute__((packed))` do and why is it dangerous?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-packed
    title: "GCC: Common Type Attributes"
    url: https://gcc.gnu.org/onlinedocs/gcc/Common-Type-Attributes.html
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

**It asks GCC to place members as closely as possible to minimize storage.**

<span class="warn">Risk</span>: a multi-byte member can have less alignment than its type normally requires. The compiler may emit safe byte accesses, or target-specific code can still fault if an aligned instruction receives its address.

Treat `packed` as a compiler-specific layout tool, not as serialization or an endianness conversion.[^embeddedinterviewlab]

## Detailed explanation

`__attribute__((packed))` is a GNU extension, not ISO C. GCC documents that applying it to a structure places each member, except zero-width bit-fields, to minimize the required memory.[^gcc-packed]

```c
struct __attribute__((packed)) Packet {
    uint8_t  tag;
    uint32_t value;
};
```

This layout is commonly five bytes, with `value` at offset 1. The address of the whole `Packet` can satisfy the packed type's alignment while `&packet.value` is not suitably aligned for an ordinary `uint32_t *`.

### Symptom

Symptoms range from slower byte-wise code to an alignment fault. They can change with target flags or optimization because the compiler selects instructions from the alignment information it has. `-Waddress-of-packed-member` is valuable when code takes a pointer that loses the member's reduced-alignment context.

### Why it happens

Packing changes layout, not the language's integer representation or a protocol's byte order. It also does not recursively pack a nested structure unless that nested type is packed separately.[^gcc-packed]

Passing a packed member's address to an API that expects `uint32_t *` is especially dangerous: the callee is allowed to assume normal `uint32_t` alignment.

### How to avoid

- Prefer an explicit byte array plus encode/decode helpers for a wire format.
- If a packed layout is unavoidable, copy a member with `memcpy` into aligned storage before using it and perform byte-order conversion separately.
- Do not map MMIO with an indiscriminately packed structure. Use the access widths, offsets, reserved gaps, and `volatile` qualification required by the device manual.
- Lock any required external layout with compile-time size/offset assertions and the intended compiler/ABI.

LearnCpp's ordinary-layout examples are useful as contrast: reordering fields can often reduce padding without weakening member alignment.[^learncpp-struct-padding]

---
id: emb-align-0005
title: "How do you reorder fields to reduce padding?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: learncpp-struct-padding
    title: "LearnCpp: Struct miscellany"
    url: https://www.learncpp.com/cpp-tutorial/struct-miscellany/
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Question code

```c
struct { uint8_t a; uint32_t b; uint8_t c; };
```

## Short answer

Group fields by decreasing alignment:

```c
struct {
  uint32_t b; // @0
  uint8_t  a; // @4
  uint8_t  c; // @5, +2 tail
};
```

Under the stated four-byte `uint32_t` alignment, `sizeof` becomes 8 instead of 12: the small fields are adjacent and internal padding disappears, although two trailing bytes remain.

This is only safe when you control the layout; do not silently reorder a public ABI, protocol, file format, or register map.[^embeddedinterviewlab]

## Detailed explanation

Assume `uint8_t` has size/alignment 1 and `uint32_t` has size/alignment 4. C preserves member declaration order and permits unnamed padding between members and at the end of a structure.[^iso-c-n1570]

```c
struct { uint8_t a; uint32_t b; uint8_t c; };
```

The original order produces this layout:
```
Offset: 0  1  2  3  4  5  6  7  8  9  10 11
        [a][pad][pad][pad][  b  ][c][pad][pad][pad]
```
`a` occupies offset 0, three internal padding bytes move `b` to offset 4, and `c` occupies offset 8. Three trailing padding bytes make the array stride a multiple of 4, so `sizeof` is 12.

Now put the most strictly aligned member first:

```c
struct {
    uint32_t b;  // size 4, alignment 4
    uint8_t  a;  // size 1, alignment 1
    uint8_t  c;  // size 1, alignment 1
};
```

```
Offset: 0  1  2  3  4  5  6  7
        [  b  ][a][c][pad][pad]
```

The reordered layout has no internal padding and two trailing bytes, so `sizeof` is 8. In an array of 100 elements, the layout uses 800 rather than 1200 bytes. LearnCpp presents the same 12-versus-8 effect and recommends decreasing member size as a useful practical heuristic.[^learncpp-struct-padding]

Alignment is the more precise ordering key. Size and alignment often correlate for scalar types, but not universally. A good workflow is:

1. Inspect `_Alignof(T)` or `alignof(T)` for the target types.
2. Group members from stricter to weaker alignment and keep related small fields together.
3. Verify `sizeof` and critical offsets with compile-time assertions.
4. Measure whether the saved storage justifies any loss of readability or locality.

Do not apply this transformation where external layout is part of the contract: memory-mapped hardware registers, network packets, persistent binary files, shared-memory ABIs, or structures consumed by separately built code. Packing is not a general substitute because it can create unaligned accesses.

---
id: emb-align-0017
title: "How do you write `swap16` to reverse the byte order?"
description: "Shift the high byte down and the low byte up then combine them with bitwise OR"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: mechanism
tags: []
status: published
updated: 2026-09-08
content_revision: 4
reconciled_with:
  uk: 4
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Source question and answer; answer not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for the C language rules involved; specific devices and toolchains can differ."
  - source_id: gcc-byte-swap-builtins
    title: "Byte-Swapping Builtins"
    url: https://gcc.gnu.org/onlinedocs/gcc/Byte-Swapping-Builtins.html
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Documents GCC's explicit 16-bit, 32-bit, and 64-bit byte-swap operations."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of shifts and bitwise OR."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for byte-swap code generation."
---

## Question code

```c
static inline uint16_t swap16(uint16_t v) {
    return (uint16_t)((v << 8) | (v >> 8));
}
```

## Short answer

**The high byte is shifted down, the low byte – up, and they are combined with `|`.**

For `0xAABB`, the result is `0xBBAA`. Optimizing compilers commonly recognize this idiom, but the exact instruction depends on the target, compiler, and options.

Rule: write byte-swap in readable C – inline asm is usually not needed.[^embeddedinterviewlab]

## Detailed explanation

`v >> 8` moves bits 8 through 15 into positions 0 through 7. `v << 8` moves bits 0 through 7 into positions 8 through 15; converting the final result to `uint16_t` discards bits above position 15. The bitwise OR combines the two non-overlapping halves.

Use an unsigned fixed-width type. Right shift of an unsigned value is logical, and `uint16_t` states that the operation expects exactly two bytes when that typedef is available. The operands undergo integer promotion, so the explicit result cast also makes the intended narrowing visible.[^iso-c-n1570]

Useful properties for tests are:

- `swap16(0xAABB)` equals `0xBBAA`;
- `swap16(0x0000)` and `swap16(0xFFFF)` are unchanged;
- applying `swap16` twice returns the original value.

GCC also exposes `__builtin_bswap16`, whose documented meaning is to reverse the bytes of a 16-bit argument.[^gcc-byte-swap-builtins] A project can wrap that builtin when its toolchain contract permits it. Both the clear shift idiom and the builtin give the optimizer a chance to select the best instruction, but neither portable C nor the builtin documentation promises a particular Arm instruction for every build.

LearnCpp explains the shift and OR operators used here,[^learncpp-bitwise] while aCode is a supplementary roadmap for extending C and C++ study.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

---
id: emb-align-0018
title: "How do you write `swap32` for a 32-bit byte swap?"
description: "Masks isolate four bytes and shifts move each one to its mirror position"
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
  - source_id: learncpp-bit-masks
    title: "Bit manipulation with bitwise operators and bit masks"
    url: https://www.learncpp.com/cpp-tutorial/bit-manipulation-with-bitwise-operators-and-bit-masks/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of masks, shifts, and combining bit fields."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for byte-swap code generation."
---

## Short answer

```c
static inline uint32_t swap32(uint32_t v) {
    return ((v & 0x000000FFu) << 24)
         | ((v & 0x0000FF00u) << 8)
         | ((v & 0x00FF0000u) >> 8)
         | ((v & 0xFF000000u) >> 24);
}
```

Each byte moves to its mirror position; masks cut off the extras.

Rule: write defined unsigned operations or use a documented builtin, then inspect optimized output when one instruction matters.[^embeddedinterviewlab]

## Detailed explanation

Each mask selects one byte before the shift:

- `0x000000FFu` selects bits 0 through 7 and moves them to bits 24 through 31;
- `0x0000FF00u` selects bits 8 through 15 and moves them to bits 16 through 23;
- the other two terms perform the mirror moves toward the low end.

The four results occupy disjoint bit positions, so bitwise OR combines them. For example, `swap32(0x12345678u)` is `0x78563412u`, and applying the function a second time restores the original value.

`uint32_t` and the `u` suffix keep the computation unsigned and exactly 32 bits when that optional fixed-width type exists. Unsigned shifts are well-defined as long as the shift count is below the type width; the masks also make each term's intent visible.[^iso-c-n1570]

GCC provides `__builtin_bswap32` with the direct semantics of reversing the bytes of a 32-bit argument.[^gcc-byte-swap-builtins] A project-specific wrapper around the builtin can state intent more directly. Optimizers also commonly recognize the mask/shift idiom. Whether either form becomes one instruction is still a property of the selected target, optimization level, and compiler version, so verify generated assembly for performance-critical code.

LearnCpp's bit-mask material explains the operations in the portable implementation,[^learncpp-bit-masks] while the aCode roadmap is supplementary guidance for broader C and C++ learning.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

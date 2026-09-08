---
id: emb-align-0019
title: "Why prefer a recognizable byte-swap idiom or builtin to inline assembly?"
description: "It preserves semantics and portability while allowing the optimizer to select a target byte-swap instruction"
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
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
    applicability: "Documents GCC builtins whose semantics directly express 16-bit, 32-bit, and 64-bit byte reversal."
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of the portable shift and mask idiom."
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian learning roadmap; not normative evidence for compiler optimization."
---

## Short answer

**A clear unsigned shift/mask idiom or byte-swap builtin exposes the operation to the optimizer.**

On a suitable Arm target, an optimizing compiler can select `REV` or `REV16`; on another target it can choose that architecture's best sequence. This is a common optimization, not a guarantee for every compiler configuration.

Rule: start with clear C; reach for intrinsics/asm only if profiling shows a need.[^embeddedinterviewlab]

## Detailed explanation

Inline assembly commits the source to an instruction set, syntax, register constraints, and compiler interface. It can also block constant folding or instruction scheduling unless its constraints describe every effect correctly. A language-level operation retains more information for whole-program optimization and still has defined behavior on targets without a dedicated byte-swap instruction.

There are two good ways to express intent:

- use unsigned shifts, masks, and OR in a well-known idiom;
- use a toolchain builtin behind a small portability wrapper.

GCC documents `__builtin_bswap16`, `__builtin_bswap32`, and `__builtin_bswap64` as operations that reverse their argument's bytes.[^gcc-byte-swap-builtins] The builtin is especially explicit, while the portable idiom also works when that extension is unavailable. LearnCpp's bitwise overview covers the operators used by the latter.[^learncpp-bitwise]

Code generation depends on the selected CPU, ISA features, optimization level, surrounding code, and compiler version. For example, constant input may be folded with no runtime instruction, while an older target may require several shifts. Therefore, "this becomes one `REV`" is an observation to verify in the optimized disassembly, not part of the C contract.

Start with the clearest correct form, compile for the actual MCU with release options, and inspect or benchmark the hot path. Use an intrinsic or inline assembly only when the measured result and supported toolchain justify the added coupling. The aCode roadmap is supplementary guidance for continuing broader C and C++ study.[^acode-cpp-next]

## Sources

<!-- generated from frontmatter -->

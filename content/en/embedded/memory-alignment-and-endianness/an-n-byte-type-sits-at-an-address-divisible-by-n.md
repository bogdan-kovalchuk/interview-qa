---
id: emb-align-0001
title: "What is natural alignment?"
description: "An N-byte type must reside at an address that is a multiple of N"
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
  - source_id: learncpp-object-sizes
    title: "LearnCpp: Object sizes and the sizeof operator"
    url: https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-operator/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary explanation of object sizes and implementation-dependent type sizes in C++."
  - source_id: acode-next-cpp
    title: "aCode: End? What next?"
    url: https://acode.com.ua/end-cpp-what-is-next/
    accessed: 2026-09-08
    kind: community
    version: null
    applicability: "Supplementary Ukrainian C++ learning roadmap; not a normative source for alignment rules."
---

## Short answer

**An object must reside at an address that satisfies its type's alignment requirement.**

In a common MCU ABI, `uint32_t`, `uint16_t`, and `uint64_t` are naturally aligned to 4, 2, and 8 bytes respectively, but size alone does not define the portable rule. A valid address is a multiple of `_Alignof(T)` in C or `alignof(T)` in C++.

Misaligned typed access is undefined in C even when the target hardware can execute it.[^embeddedinterviewlab]

## Detailed explanation

An **alignment requirement** is an implementation-defined number of bytes between valid starting addresses for an object type. C exposes it through `_Alignof(T)`; C++ uses `alignof(T)`. The precise rule is based on that value, not on `sizeof(T)`.[^iso-c-n1570]

For example, on an ABI where `_Alignof(uint32_t) == 4`, valid starting addresses are divisible by 4. This remains an ABI statement: a 32-bit type is not guaranteed by the language alone to have four-byte alignment, and extended types may have an alignment smaller than their size. `sizeof` itself is implementation-dependent for most fundamental types.[^learncpp-object-sizes]

Alignment matters at two different levels:

- The C object model requires an object to be stored at a suitably aligned address. Converting a byte-buffer address to `T *` does not make it suitably aligned; dereferencing an invalidly aligned pointer has undefined behavior.
- The hardware may complete an unaligned instruction, split it into several transfers, or raise a fault. That behavior depends on the instruction, memory region, core configuration, and bus implementation.

Compilers satisfy the requirement for ordinary variables, array elements, and allocated objects. They also insert padding into structures so each member and each element of an array of structures begins at a valid address.

When bytes arrive from a packet, file, packed structure, or peripheral buffer, copy them into an aligned object with `memcpy` and decode the byte order explicitly. Do not assume that a cast fixes alignment or representation.

Use `_Alignas` in C or `alignas` in C++ when storage needs a stricter alignment than its declaration would otherwise provide. Verify protocol, DMA, cache-line, and peripheral requirements separately because they can be stricter than the language type's natural alignment.

## Sources

<!-- generated from frontmatter -->

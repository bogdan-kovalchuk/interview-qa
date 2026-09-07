---
id: emb-dtypes-0100
title: "Trap: legal in C or C++? `union { float f; uint32_t u; } pun; pun.f = 1.0f; uint32_t r = pun.u;`"
description: "In C this is common union type punning; formally in C++ reading the inactive member is undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and answer; the answer is not independently verified."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
---

## Short answer

In **C**: this is common union type punning. It is not a strict aliasing violation, but the resulting value depends on IEEE 754 representation, endianness, and the implementation; for maximally portable code, prefer `memcpy(&r, &pun.f, sizeof r)`.

In **C++**: formally, it is <span class="warn">undefined behavior</span> (active member rule: the active member is `f`, reading `u` is UB). GCC/Clang support it as an extension, but the standard does not guarantee it.

Safe alternative for C++ (C++20): `std::bit_cast<uint32_t>(1.0f)`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

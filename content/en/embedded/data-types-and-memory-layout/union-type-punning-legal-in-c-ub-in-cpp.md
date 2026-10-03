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
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Origin of the question and the original answer (owner's deck). The short answer and the Ukrainian explanation were checked against cited technical sources on 2026-10-04; this source is not proof of the claims."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Authoritative section-level reference for data types and memory layout concepts; details of specific devices and toolchains can differ."
  - source_id: cpp-union
    title: 'C++ working draft: Unions'
    url: https://eel.is/c++draft/class.union.general
    accessed: 2026-10-04
    kind: spec
    version: current working draft
    applicability: 'C++ active union member rules; the common initial sequence exception is separate and does not cover ordinary float-to-integer reinterpretation.'
  - source_id: cpp-bit-cast
    title: 'C++ working draft: bit_cast'
    url: https://eel.is/c++draft/bit.cast
    accessed: 2026-10-04
    kind: spec
    version: current working draft
    applicability: 'C++20 std::bit_cast requirements: equal size and trivially copyable types; the resulting representation depends on the source types and implementation.'
---

## Short answer

In **C**, reading another union member reinterprets the corresponding bytes; the result is not a portable numeric conversion, and a trap representation cannot safely be read as a value.[^iso-c-n1570]

In **C++**, reading inactive member `u` after writing `f` has <span class="warn">undefined behavior</span> in this case; the common initial sequence exception does not apply.[^cpp-union]

Use `memcpy` to copy a representation in C; in C++20, `std::bit_cast` is available when the types have equal size and are trivially copyable.[^cpp-bit-cast]

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

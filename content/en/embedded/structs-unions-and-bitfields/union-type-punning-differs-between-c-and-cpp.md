---
id: emb-structs-0016
title: "Trap: what is dangerous about union type punning?"
description: "The trap is not in C syntax but in the portability of the result and the difference between C and C++."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  uk: 1
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
---

## Question code

```c
union U { float f; uint32_t u; };
union U x;
x.f = 1.0f;
uint32_t bits = x.u;
```

## Short answer

<span class="warn">The trap is not in C syntax but in the portability of the result and the difference between C and C++.</span>

In C99/C11, reading a different union member to inspect object representation is a standard-described type punning pattern; this is not the same as a pointer-cast strict aliasing violation. But the value of `bits` still depends on the representation of `float` and on endianness. In C++, reading an inactive union member is usually undefined behavior.

Defense: for a portable bit copy, use `memcpy(&bits, &x.f, sizeof bits)`, and in C++20 use `std::bit_cast`.[^embeddedinterviewlab]

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

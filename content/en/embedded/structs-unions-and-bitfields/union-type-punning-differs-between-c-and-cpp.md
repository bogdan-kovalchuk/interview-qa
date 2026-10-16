---
id: emb-structs-0016
title: "Trap: what is dangerous about union type punning?"
track: embedded
section: structs-unions-and-bitfields
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
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

In C, a union's representation may be inspected through another member, but the resulting value can be implementation-defined or a trap representation. In C++, reading an inactive union member is generally not permitted, apart from narrow common-initial-sequence exceptions.

Use `memcpy` to copy bytes without violating aliasing rules; C++20 also provides `std::bit_cast`. Neither guarantees the same numeric result on platforms with different type representations.[^iso-c-n1570]

## Detailed explanation

TODO

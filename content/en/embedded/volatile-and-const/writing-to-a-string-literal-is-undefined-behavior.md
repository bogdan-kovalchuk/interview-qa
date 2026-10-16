---
id: emb-volconst-0030
title: "Trap: what is unsafe about `char *p = \"OK\"; p[0] = 'N';`?"
track: embedded
section: volatile-and-const
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

<span class="warn">Writing to a string literal has undefined behavior.</span>

In C, a string literal initializes an array with static storage duration, and attempting to modify that array has undefined behavior. Its physical placement is implementation-dependent; a write may fault on an MCU, but that symptom is not guaranteed.

Use `const char *p = "OK";` for read-only access, or a mutable array `char p[] = "OK";` if the characters must be changed.[^iso-c-n1570]

## Detailed explanation

TODO

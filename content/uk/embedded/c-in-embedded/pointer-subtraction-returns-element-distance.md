---
id: emb-cppfound-0049
title: "Як pointer arithmetic поводиться при відніманні двох вказівників?"
track: embedded
section: c-in-embedded
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

Відняття двох вказівників одного типу повертає **ptrdiff_t** – кількість елементів між ними (не байт).

`int *p = arr+4; int *q = arr+1; p - q = 3` (три `int`-елементи).

Умова: обидва вказівники мають вказувати на **один масив** (або one-past-the-end). Відняття вказівників що вказують на різні масиви/об'єкти -> <span class="warn">undefined behavior (UB)</span>.

Застосування: `strlen`-подібний підрахунок, offset між елементами буфера.[^embeddedinterviewlab]

## Detailed explanation

TODO

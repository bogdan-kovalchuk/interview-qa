---
id: emb-cppfound-0077
title: "Що таке strict aliasing rule і як він стосується pointer casting?"
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

**Strict aliasing rule** (C99 §6.5): компілятор може вважати що вказівники різних несумісних типів НЕ alias-ують (не вказують на одну область пам'яті).

Дозволяє агресивну оптимізацію: якщо змінили через `float*` – компілятор не зобов'язаний перечитати через `int*`.

Виключення: `char*` та `unsigned char*` можуть alias-увати будь-що.

Порушення: `int x; float *fp=(float*)&x; *fp=1.0f;` -> UB. Захист: `memcpy` або `union` (у C).[^embeddedinterviewlab]

## Detailed explanation

TODO

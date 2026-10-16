---
id: emb-cppfound-0039
title: "Що зробить `memcpy(dst, src, sizeof(src))` якщо `src` – параметр-масив функції?"
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

<span class="warn">Скопіює лише 4 або 8 байт</span> (розмір вказівника), а не розмір масиву.

У параметрі функції `src` – це `uint8_t*`, не масив. `sizeof(src) = sizeof(uint8_t*) = 4`. Тому `memcpy` копіює тільки 4 байти замість N.

Правильно: передавати розмір явно: `memcpy(dst, src, n * sizeof(src[0]))` або `memcpy(dst, src, n)` де `n` – окремий параметр.[^embeddedinterviewlab]

## Detailed explanation

TODO

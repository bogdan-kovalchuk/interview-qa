---
id: emb-cppfound-0044
title: "Навіщо `volatile` при роботі з hardware registers через вказівник?"
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

Без `volatile` компілятор може:
1. <span class="warn">Кешувати</span> значення регістру у CPU регістрі і не перечитувати (пропустить апаратну зміну);
2. <span class="warn">Видалити "зайві" записи</span> (dead store elimination) – якщо значення не читається далі;
3. <span class="warn">Переупорядкувати</span> операції для оптимізації.

З `volatile`: кожен read/write реально виконується у порядку написання.

Паттерн: `volatile uint32_t * const GPIOA_ODR = (volatile uint32_t*)0x40020014U;`[^embeddedinterviewlab]

## Detailed explanation

TODO

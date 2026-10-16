---
id: emb-cppfound-0025
title: "Trap: легально у стандартному C?"
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

## Question code

```c
void *p = malloc(10);
p++;
```

## Short answer

<span class="warn">НІ, це невалідний стандартний C</span> (constraint violation). Стандарт забороняє pointer arithmetic на `void*` – розмір елемента невідомий (sizeof(void) не визначений), тому компілятор має видати діагностику.

GCC дозволяє як extension: трактує `sizeof(void) = 1`, тому `p++` -> +1 байт. З `-pedantic-errors`: помилка.

Правильно: перед arithmetic – cast до конкретного типу: `uint8_t *bp = (uint8_t*)p; bp++;`[^embeddedinterviewlab]

## Detailed explanation

TODO

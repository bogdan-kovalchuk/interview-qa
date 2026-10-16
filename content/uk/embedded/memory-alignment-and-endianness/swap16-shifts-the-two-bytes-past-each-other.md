---
id: emb-align-0017
title: "Як написати `swap16` для зміни порядку байтів?"
track: embedded
section: memory-alignment-and-endianness
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
  - source_id: gcc-byte-swap-builtins
    title: "Byte-Swapping Builtins"
    url: https://gcc.gnu.org/onlinedocs/gcc/Byte-Swapping-Builtins.html
  - source_id: learncpp-bitwise
    title: "Bitwise operators"
    url: https://www.learncpp.com/cpp-tutorial/bitwise-operators/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Question code

```c
static inline uint16_t swap16(uint16_t v) {
    return (uint16_t)((v << 8) | (v >> 8));
}
```

## Short answer

**Старший байт зсувається вниз, молодший – вгору, і вони об'єднуються через `|`.**

Для `0xAABB` результатом є `0xBBAA`. Optimizing compilers часто розпізнають цей idiom, але точна інструкція залежить від target, compiler та options.

Правило: пиши byte-swap читабельним C – inline asm зазвичай не потрібен.[^embeddedinterviewlab]

## Detailed explanation

`v >> 8` переміщує біти від 8 до 15 у позиції від 0 до 7. `v << 8` переміщує біти від 0 до 7 у позиції від 8 до 15; перетворення кінцевого результату на `uint16_t` відкидає біти вище позиції 15. Bitwise OR об'єднує дві частини, що не перекриваються.

Використовуй unsigned fixed-width type. Right shift unsigned-значення є logical, а `uint16_t` указує, що операція очікує рівно два байти, якщо такий typedef доступний. Операнди проходять integer promotion, тому явний cast результату також показує задумане narrowing.[^iso-c-n1570]

Корисні властивості для тестів:

- `swap16(0xAABB)` дорівнює `0xBBAA`;
- `swap16(0x0000)` і `swap16(0xFFFF)` не змінюються;
- подвійне застосування `swap16` повертає початкове значення.

GCC також надає `__builtin_bswap16`, задокументований зміст якого – розвернути байти 16-бітного аргументу.[^gcc-byte-swap-builtins] Проєкт може загорнути цей builtin, якщо це дозволяє його toolchain contract. І зрозумілий shift idiom, і builtin дають optimizer змогу вибрати найкращу інструкцію, але ні portable C, ні документація builtin не гарантують конкретну Arm-інструкцію для кожної збірки.

LearnCpp пояснює використані тут shift та OR operators,[^learncpp-bitwise] а aCode є додатковою дорожньою картою для поглиблення знань C і C++.[^acode-cpp-next]

---
id: emb-align-0018
title: "Як написати `swap32` для 32-бітного byte-swap?"
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
  - source_id: learncpp-bit-masks
    title: "Bit manipulation with bitwise operators and bit masks"
    url: https://www.learncpp.com/cpp-tutorial/bit-manipulation-with-bitwise-operators-and-bit-masks/
  - source_id: acode-cpp-next
    title: "C++ вивчено – що далі?"
    url: https://acode.com.ua/end-cpp-what-is-next/
---

## Short answer

```c
static inline uint32_t swap32(uint32_t v) {
    return ((v & 0x000000FFu) << 24)
         | ((v & 0x0000FF00u) << 8)
         | ((v & 0x00FF0000u) >> 8)
         | ((v & 0xFF000000u) >> 24);
}
```

Кожен байт переміщується у дзеркальну позицію, маски відсікають зайве.

Правило: пиши визначені unsigned operations або використовуй документований builtin, а коли одна інструкція справді важлива – перевіряй optimized output.[^embeddedinterviewlab]

## Detailed explanation

Кожна mask виділяє один байт перед shift:

- `0x000000FFu` виділяє біти від 0 до 7 і переміщує їх у біти від 24 до 31;
- `0x0000FF00u` виділяє біти від 8 до 15 і переміщує їх у біти від 16 до 23;
- дві інші частини виконують дзеркальні переміщення до молодшого краю.

Чотири результати займають різні bit positions, тому bitwise OR об'єднує їх. Наприклад, `swap32(0x12345678u)` дає `0x78563412u`, а повторне застосування функції відновлює початкове значення.

`uint32_t` і suffix `u` зберігають обчислення unsigned та рівно 32-бітним, якщо цей optional fixed-width type існує. Unsigned shifts мають визначену поведінку, доки shift count менший за ширину типу; masks також явно показують призначення кожної частини.[^iso-c-n1570]

GCC надає `__builtin_bswap32` із прямою семантикою розвертання байтів 32-бітного аргументу.[^gcc-byte-swap-builtins] Project-specific wrapper навколо builtin може ще краще показати намір. Optimizers також часто розпізнають mask/shift idiom. Чи стане будь-яка з форм однією інструкцією, все одно залежить від target, optimization level і compiler version, тому для performance-critical коду перевіряй generated assembly.

Матеріал LearnCpp про bit masks пояснює операції в portable implementation,[^learncpp-bit-masks] а дорожня карта aCode є додатковим орієнтиром для ширшого вивчення C і C++.[^acode-cpp-next]

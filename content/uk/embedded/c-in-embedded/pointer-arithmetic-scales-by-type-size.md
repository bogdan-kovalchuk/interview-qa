---
id: emb-cppfound-0007
title: "Як відбувається pointer arithmetic і чому вона масштабується по `sizeof(T)`?"
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

Арифметика вказівників завжди враховує **розмір елемента типу**:

`T *p; p + n` -> фізично: `(char*)p + n * sizeof(T)`

Приклади:
- `uint8_t *p; p+1` -> +1 байт
- `uint16_t *p; p+1` -> +2 байти
- `uint32_t *p; p+1` -> +4 байти

Це дозволяє ітерувати масиви природно: `p++` – наступний елемент, незалежно від розміру. Критично у embedded при роботі з register banks і DMA буферами.[^embeddedinterviewlab]

## Detailed explanation

TODO

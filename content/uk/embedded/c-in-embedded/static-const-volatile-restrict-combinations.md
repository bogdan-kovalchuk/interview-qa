---
id: emb-cemb-0032
title: "Для чого потрібні static, const, volatile і restrict у C, і які комбінації мають сенс?"
track: embedded
section: c-in-embedded
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`static` керує linkage або storage duration, `const` забороняє зміну через цей lvalue, `volatile` змушує реально виконувати access, а `restrict` обіцяє відсутність aliasing для оптимізації. Для MMIO типовий pointer: `volatile uint32_t *`; для read-only register може бути `volatile const uint32_t *`. `static const` часто кладе таблиці у flash/rodata, а `restrict` доречний у DSP/buffer code, якщо контракт справді виконується.[^dou-embedded-interview]

## Detailed explanation

TODO

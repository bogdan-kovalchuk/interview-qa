---
id: emb-cemb-0016
title: "Розкажіть про бітові поля."
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

**Бітові поля** – це поля структури з явно заданою кількістю бітів: `struct Flags { unsigned ready:1; unsigned mode:3; };`.[^dou-embedded-interview] Вони зручні для компактного зберігання прапорців або опису частин register/status word.

Обмеження: не можна взяти адресу bit-field, порядок пакування бітів, signedness і padding часто implementation-defined, тому layout може відрізнятися між компіляторами й ABI. Для hardware registers і протоколів часто надійніше використовувати маски й зсуви над `uint32_t`, а bit-fields – тільки коли layout контролюється й перевірений.

## Detailed explanation

TODO

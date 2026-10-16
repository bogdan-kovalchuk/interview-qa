---
id: emb-cemb-0003
title: "Які є операції з вказівниками?"
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

Основні операції: взяти адресу `&x`, розіменувати `*p`, доступ до поля через `p->field`, порівняння з `NULL` або іншим вказівником, присвоєння адреси, приведення типу, передача у функцію.[^dou-embedded-interview]

Є pointer arithmetic: `p + 1` переходить не на 1 байт, а на `sizeof(*p)` байтів. Тому `int *p` при `p++` зсувається на розмір `int`. Коректна арифметика визначена в межах одного масиву або на позицію одразу після нього; вихід за межі й розіменування невалідної адреси – undefined behavior.

## Detailed explanation

TODO

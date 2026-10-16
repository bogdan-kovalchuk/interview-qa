---
id: emb-cemb-0018
title: "Для чого потрібен extern «C»?"
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

`extern "C"` використовується в C++, щоб сказати компілятору застосувати C linkage для функцій або змінних.[^dou-embedded-interview] Головний ефект – вимкнення C++ name mangling, тобто ім'я символу в object/shared library буде сумісне з C.

Це потрібно, коли C++ код викликає C-бібліотеку або C код має викликати функцію, написану на C++. Типовий header пишуть так: `#ifdef __cplusplus extern "C" { #endif` ... `#ifdef __cplusplus } #endif`, але сам код функції лишається C++ кодом, а ABI і назва символу стають C-сумісними.

## Detailed explanation

TODO

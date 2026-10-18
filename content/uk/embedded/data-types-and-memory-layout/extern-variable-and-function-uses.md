---
id: emb-cemb-0025
title: "Які варіанти використання `extern` знаєте?"
track: embedded
section: data-types-and-memory-layout
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
---

## Short answer

`extern` оголошує ім'я, яке визначене в іншому translation unit: у header пишуть `extern int counter;`, а в одному `.c` файлі має бути визначення `int counter;`. Це дозволяє розділяти declaration і definition без дублювання глобальної змінної.

Також `extern` застосовують для функцій, хоча для звичайних функцій external linkage є типовим. У C++ є окремий випадок `extern "C"` – він вимикає C++ name mangling, щоб C++ код міг лінкуватися з C API або динамічною бібліотекою.[^dou-embedded-interview]

## Detailed explanation

TODO

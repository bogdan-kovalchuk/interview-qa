---
id: emb-cemb-0001
title: "Опишіть використання модифікатора `static` в мовах C і C++."
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

**У C:**
- Локальна змінна: `static int cnt = 0;` – зберігає стан між викликами.
- Глобальна змінна/функція: `static void helper()` – видима лише в поточному `.c` файлі.[^dou-embedded-interview]

**Додатково у C++:**
- Статичний член класу: `static int count;` – один для всіх об'єктів, ініціалізується поза класом.
- Статичний метод: `static void reset();` – викликається як `MyClass::reset()`, не має доступу до `this`.

## Detailed explanation

TODO

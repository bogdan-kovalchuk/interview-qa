---
id: emb-cemb-0001
title: "Опишіть використання модифікатора `static` в мовах C і C++."
description: "`static` продовжує час життя локальної змінної, обмежує linkage глобальної змінної чи функції файлом і в C++ дає одну копію члена класу на всі об'єкти."
track: embedded
section: c-in-embedded
level: junior
type: concept
tags: []
status: published
updated: 2026-09-07
content_revision: 2
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження цього питання й відповіді; текст відповіді не перевірений незалежно від оригінальної Anki-колоди спільноти."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу c-in-embedded; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
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

## Sources

<!-- generated from frontmatter -->

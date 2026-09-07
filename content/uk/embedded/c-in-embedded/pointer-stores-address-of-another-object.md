---
id: emb-cemb-0014
title: "Що таке вказівник?"
description: "Вказівник – змінна, що зберігає адресу іншого об'єкта чи функції; & бере адресу, а *p розіменовує й дає доступ до значення."
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

**Вказівник** – змінна, яка зберігає адресу іншого об'єкта або функції в пам'яті.[^dou-embedded-interview] Наприклад: `int x = 10; int *p = &x;`. Оператор `&` бере адресу, а `*p` розіменовує вказівник і дає доступ до значення.

Вказівники потрібні для передачі об'єктів у функції без копіювання, роботи з масивами, динамічною пам'яттю, callback-ами, структурами даних і memory-mapped регістрами. Небезпеки: `NULL`, dangling pointer, вихід за межі масиву, неправильне приведення типів.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

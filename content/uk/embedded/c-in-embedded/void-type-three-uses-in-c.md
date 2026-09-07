---
id: emb-cemb-0002
title: "Як працювати з `void`?"
description: "`void` означає відсутність типу і використовується для функції без повернення, функції без параметрів і як узагальнений вказівник `void *`."
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

`void` означає «відсутність типу». Три використання:

1. **Функція без повернення**: `void init(void);`
2. **Функція без параметрів**: `int get(void);` – у C `int f()` і `int f(void)` різняться! 3; **Узагальнений вказівник**: `void *ptr` – вказівник на будь-який object type; його не можна напряму розіменувати або робити над ним стандартну pointer arithmetic;

У C `void *` неявно конвертується в object pointer, але перед доступом треба мати конкретний тип: `int *p = ptr;`; У C++ таке перетворення потребує явного cast.[^dou-embedded-interview]

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

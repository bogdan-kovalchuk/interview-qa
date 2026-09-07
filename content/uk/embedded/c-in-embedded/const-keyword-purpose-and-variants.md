---
id: emb-cemb-0012
title: "Яке призначення ключового слова const?"
description: "const забороняє змінювати значення через дане ім'я після ініціалізації; вказівник на const, const-вказівник і обидва разом читаються справа наліво."
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

Забороняє змінювати значення через це ім'я після ініціалізації.[^dou-embedded-interview] Компілятор видасть помилку при спробі запису.

Варіанти: `const int x = 5;` – константна змінна; `const int *p` – вказівник на константу (дані захищені); `int * const p` – константний вказівник (адреса захищена); `const int * const p` – обидва захищені.

В Embedded `const` не гарантує конкретне місце зберігання. У багатьох toolchain такі дані кладуть у `.rodata` у Flash, але це залежить від ABI, linker script і платформи; В C++ методи: `void get() const` – гарантує, що метод не змінює стан об'єкта.

## Detailed explanation

TODO

## Sources

<!-- generated from frontmatter -->

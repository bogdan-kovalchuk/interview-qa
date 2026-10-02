---
id: emb-dtypes-0079
title: "Що означає storage class `register` і чи має він значення сьогодні?"
description: "У C `register` не гарантує розміщення у CPU-регістрі й забороняє брати адресу оголошеного так об’єкта."
track: embedded
section: data-types-and-memory-layout
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
anki:
  export: true
sources:
  - source_id: embeddedinterviewlab
    title: "Embedded Interview Lab"
    url: https://embeddedinterviewlab.com/
    accessed: 2026-09-06
    kind: community
    version: null
    applicability: "Походження питання й первинної відповіді (власна колода). Коротку відповідь і пояснення звірено з технічними джерелами 2026-10-04; це джерело не є доказом тверджень."
  - source_id: iso-c-n1570
    title: "ISO/IEC 9899:201x Committee Draft N1570"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-09-06
    kind: spec
    version: "N1570"
    applicability: "Авторитетне джерело рівня секції для понять розділу data-types-and-memory-layout; деталі конкретних пристроїв і тулчейнів можуть відрізнятися."
  - source_id: cpp17-register-removal
    title: "C++17 draft: Removal of register storage-class specifier"
    url: https://eel.is/c%2B%2Bdraft/diff.cpp14.dcl.dcl
    accessed: 2026-10-04
    kind: spec
    version: "C++17"
    applicability: "Підтверджує вилучення специфікатора register у C++17; не описує правило C."
---

## Short answer

У C11 `register` є застарілим storage-class hint: він не гарантує розміщення об’єкта в CPU register, а реалізація може його не враховувати.[^iso-c-n1570] Для об’єкта, оголошеного з `register`, C забороняє застосовувати unary `&`.[^iso-c-n1570] У C++17 специфікатор `register` вилучено; це правило не слід змішувати з поведінкою C.[^cpp17-register-removal]

## Detailed explanation

У C `register` історично виражав побажання зберігати часто використовувану локальну змінну в регістрі процесора. Це не наказ компілятору і не гарантія швидшого коду: компілятор бачить типи, частоту використання, доступні регістри та весь контекст оптимізації. За стандартом C11 `register` є застарілим засобом, а реалізація може трактувати його як звичайне оголошення без вимоги розмістити об’єкт у регістрі.[^iso-c-n1570]

Специфікатор має помітний обмежувальний наслідок: до об’єкта, оголошеного з `register`, не можна застосувати оператор взяття адреси `&`. Тому не можна передати адресу такої змінної функції, яка очікує pointer, або отримати її для діагностики. Це обмеження стосується конкретної декларації, а не всіх змінних, які компілятор фактично тримає у регістрах.[^iso-c-n1570]

Не перенось це формулювання механічно на C++. У C++17 storage-class specifier `register` було вилучено; робочий проект стандарту документує зміну та пояснює, що в C++ він не мав ефекту як storage-class specifier.[^cpp17-register-removal] У старішому C++ коді ключове слово мало іншу історію сумісності, тож версію мови слід вказувати.

**Приклад:**

```c
register unsigned count = 0;
/* &count is a constraint violation in C */
```

Для звичайного коду оголошуй змінну без `register`, а продуктивність вимірюй на реальній цілі з потрібними compiler flags. Розподіл регістрів краще залишити оптимізатору: ручний hint може лише створити обмеження на адресу, не гарантуючи виграшу.

## Sources

<!-- generated from frontmatter -->

---
id: emb-structs-0023
title: "Чому не можна взяти адресу bit-field?"
description: "Bit-field не має адресованого byte object-а як звичайне поле."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Short answer

<span class="warn">До bit-field не можна застосувати оператор взяття адреси `&` у C.</span>

Bit-field може бути частиною addressable storage unit, але стандарт C прямо забороняє застосовувати до самого bit-field оператор `&`. Тому `&s.flag` є порушенням обмежень мови й потребує діагностики компілятора.[^iso-c-n1570]

Таке поле не можна передати у функцію як pointer на нього. Якщо API потребує адресу, скопіюй значення у звичайну змінну або передай структуру/маску іншим способом.[^iso-c-n1570]

## Detailed explanation

У C вираз `&object` утворює pointer на об’єкт. Для bit-field ця операція заборонена: стандарт прямо зазначає, що до bit-field не можна застосувати unary `&`, отже не існує pointer або array із елементів bit-field.[^iso-c-n1570]

Причина практична: поле може займати лише частину storage unit разом із сусідніми полями, а його фізичне розташування та порядок бітів залежать від реалізації. Звичайний pointer позначає адресу об’єкта, а не пару «адреса storage unit плюс маска біта». Компілятор може коректно прочитати або змінити поле, але C не надає стандартного pointer type, який посилався б саме на цей фрагмент бітів.[^iso-c-n1570]

Наприклад, `&s.flag` у `struct S { unsigned int flag : 1; };` не є дозволеним виразом C і має викликати діагностику. Не можна передати поле функції, що приймає `unsigned int *`, як `set_flag(&s.flag)`. Замість цього передай адресу всієї структури, звичайну змінну-копію або ціле значення; функція тоді зможе змінити bit-field через його контейнер.

**Типові помилки:**

- вважати, що кожне іменоване поле struct має власну адресу;
- намагатися передати bit-field через pointer-параметр;
- плутати адресу storage unit із адресою самого поля.

Пастка зазвичай проявляється як помилка компіляції на `&s.flag`. Щоб уникнути її, спроєктуй API навколо структури або значення, а якщо потрібна адреса окремого об’єкта – збережи прапорець у звичайній змінній відповідного типу.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

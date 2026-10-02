---
id: emb-dtypes-0003
title: "Чому `if(x < y)` повертає `false`, якщо `int x = -1` і `unsigned int y = 1`?"
description: "У змішаному виразі signed перетворюється на unsigned, тому -1 стає UINT_MAX."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 4
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
---

## Short answer

Це не integer promotion: для `int x = -1` і `unsigned int y = 1` usual arithmetic conversions приводять обидва операнди до `unsigned int`, бо ці типи мають однаковий ранг. Перетворення `-1` дає `UINT_MAX`, тому `x < y` хибне; числове значення `UINT_MAX` залежить від ширини `unsigned int`.[^iso-c-n1570]

## Detailed explanation

Спочатку integer promotions застосовуються до типів, ранг яких нижчий за `int`; для звичайних `int` та `unsigned int` вони нічого не змінюють. Далі для оператора порівняння діють usual arithmetic conversions: коли один операнд має signed-тип, а другий unsigned-тип того самого рангу, signed-операнд перетворюється до unsigned-типу.[^iso-c-n1570]

У прикладі `x` має значення −1, а після перетворення до `unsigned int` це значення за правилом стандарту стає максимальним значенням цього типу. `y` лишається рівним 1, тому порівняння фактично перевіряє, чи максимальне unsigned-значення менше за 1, і повертає false.[^iso-c-n1570]

Конкретне десяткове значення `UINT_MAX` не можна вивести лише з назви типу: воно визначається реалізацією. Результат порівняння в цьому прикладі від цього не змінюється. Попередження `-Wsign-compare` корисне для виявлення такого коду, але правильне виправлення залежить від задуму: перевірити знак до перетворення або привести значення до спільного типу, який коректно представляє потрібний діапазон.[^iso-c-n1570]

Ці правила не означають, що кожен signed-тип завжди перетворюється на unsigned. Для операндів різного рангу результат залежить від того, чи може signed-тип представити всі значення unsigned-типу; в одному випадку обидва стають signed-типом, в іншому signed-операнд переходить до відповідного unsigned-типу. Саме тому варто встановити точні типи виразу, а не застосовувати коротке гасло «signed стає unsigned».[^iso-c-n1570]

Для індексів контейнерів часто з'являється така проблема, коли signed-індекс порівнюють із беззнаковим результатом `sizeof` або `size_t`. Зміна лише одного боку на cast може приховати некоректний негативний індекс, тож спершу перевіряють, що signed-значення невід'ємне, і лише потім виконують беззнакове порівняння. Інший підхід – узгодити типи інтерфейсу та явно обробити межі на вході.

**Типова пастка:** негативне значення проходить перевірку межі після перетворення в unsigned. Наприклад, перевірка `x < y` може пропустити очікувану гілку; порівнюйте значення лише після явної перевірки допустимого діапазону.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

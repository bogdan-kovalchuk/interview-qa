---
id: emb-dtypes-0089
title: "Що таке type punning і коли це undefined behavior у C++?"
description: "У C type punning через union прийнятний, а у C++ безпечний лише через memcpy або std::bit_cast."
track: embedded
section: data-types-and-memory-layout
level: middle
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
---

## Short answer

**Type punning** – інтерпретація байтів об’єкта як іншого типу. У C читання іншого члена `union` має implementation-defined результат; доступ до того самого сховища через несумісний pointer може порушити правила effective type. У C++ читання неактивного члена `union` загалом не є дозволеним способом перетворення; для trivially copyable типів використовуйте `memcpy` або `std::bit_cast` з C++20 та перевірте, що цільовий тип має допустиме представлення.[^iso-c-n1570]

## Detailed explanation

Type punning – спосіб дослідити ті самі байти через інший тип, але адресація однакової пам’яті сама по собі не робить таке читання дозволеним. Мова задає правила доступу до об’єкта, його типу та часу життя. Компілятор може оптимізувати програму, спираючись на ці правила, тому результат, який випадково спостерігається при вимкнених оптимізаціях, не є гарантією.

У C читання нещодавно записаного іншого члена `union` має implementation-defined аспект: реалізація трактує байтове представлення нового члена як представлення прочитаного члена. Отримане значення залежить від представлення типів і може бути проблемним, якщо бітовий шаблон не є допустимим. У C++ діє модель active member: читати член, чий час життя не почався, загалом не можна; вузький виняток для common initial sequence структур не перетворює union на загальний механізм reinterpretation.[^iso-c-n1570]

Cast вказівника на `int` до `float*` і розіменування не перетворює `int` на `float`. Це доступ до об’єкта через несумісний glvalue, що порушує правила aliasing і може дати undefined behavior. Для копіювання представлення між trivially copyable типами використовуйте `memcpy`; у C++20 є `std::bit_cast`, якщо типи мають однаковий розмір і цільове представлення є допустимим. Жоден із цих засобів не гарантує однакових числових результатів на всіх архітектурах.

Приклад: щоб отримати бітове представлення `float` як `uint32_t`, збережіть байти через `memcpy` або `std::bit_cast<uint32_t>(value)`, а не розіменовуйте reinterpret-cast вказівник. Це копіює representation без порушення правил доступу.

**Типова помилка:** називати будь-який union punning undefined behavior у C, або вважати його універсально переносним у C++. Мова й версія стандарту мають значення; для переносимого коду обирайте засіб копіювання представлення та перевіряйте допустимість значення.[^iso-c-n1570]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->

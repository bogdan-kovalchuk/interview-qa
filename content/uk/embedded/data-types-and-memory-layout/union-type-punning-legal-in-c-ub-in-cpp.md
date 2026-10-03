---
id: emb-dtypes-0100
title: "Trap: легально у C чи C++? `union { float f; uint32_t u; } pun; pun.f = 1.0f; uint32_t r = pun.u;`"
description: "У C це поширений union type punning, а формально у C++ читання неактивного члена union - undefined behavior."
track: embedded
section: data-types-and-memory-layout
level: middle
type: pitfall
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
  - source_id: cpp-union
    title: 'C++ working draft: Unions'
    url: https://eel.is/c++draft/class.union.general
    accessed: 2026-10-04
    kind: spec
    version: current working draft
    applicability: 'Правила активного члена union у C++; спільна початкова послідовність має окремий виняток, але звичайне reinterpretation float як integer ним не охоплене.'
  - source_id: cpp-bit-cast
    title: 'C++ working draft: bit_cast'
    url: https://eel.is/c++draft/bit.cast
    accessed: 2026-10-04
    kind: spec
    version: current working draft
    applicability: 'Вимоги C++20 до std::bit_cast: однаковий розмір і trivially copyable типи; отримане представлення залежить від вихідних типів і реалізації.'
---

## Short answer

У **C** читання іншого члена union переінтерпретує відповідні байти; результат не є переносним числовим перетворенням, а trap representation не можна безпечно читати як значення.[^iso-c-n1570]

У **C++** читання неактивного члена `u` після запису в `f` має <span class="warn">undefined behavior</span> у наведеному випадку; виняток для спільної початкової послідовності тут не застосовується.[^cpp-union]

Для копіювання representation у C використовуй `memcpy`; у C++20 можна застосувати `std::bit_cast`, якщо типи однакового розміру й trivially copyable.[^cpp-bit-cast]

## Detailed explanation

Union type punning означає запис через один член `union` і читання тих самих байтів через інший. У C стандарт описує переінтерпретацію представлення; байти, що не відповідають записаному члену, можуть мати unspecified values, а trap representation робить читання значенням недопустимим.[^iso-c-n1570] У C++ активний член є членом, чий час життя розпочато; звичайне читання `u` після запису `f` не підпадає під виняток спільної початкової послідовності й не є переносним.[^cpp-union]

Важливо розділяти два питання: чи дозволяє мова виконати доступ і які біти має тип. Навіть коли реалізація підтримує union punning як розширення, результат залежить від розміру типів і представлення floating-point та integer. Endianness стає важливою, коли байти потім інтерпретують або передають; сам union не перетворює числове значення з одного формату на інший.

Для копіювання object representation у C можна застосувати `memcpy` у цілочисельний об’єкт за умови відповідного розміру; однак отримані байти можуть бути trap representation або не кодувати очікуване значення. У C++20 `std::bit_cast` копіює представлення, якщо типи trivially copyable і мають однаковий розмір, але також не створює універсального формату.[^cpp-bit-cast]

Якщо мета – серіалізувати число, кодуй його явно у визначений порядок байтів. Якщо мета – лише переглянути представлення під час діагностики на конкретній платформі, задокументуй це припущення й не видавай код за portable. Компіляторні extensions можуть мати чіткі гарантії, але тоді це контракт компілятора, а не стандартної C++ програми.[^cpp-union]

**Типова помилка:** переносити звичну практику C без змін у C++ або вважати, що compiler extension доводить відповідність стандарту. У C++ застосовуй `std::bit_cast` чи `memcpy` та окремо визначай інтерпретацію байтів.[^cpp-union] [^cpp-bit-cast]

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

---
id: emb-fnptr-0049
title: "Trap: чому не слід зберігати function pointer у `void *`?"
description: "ISO C гарантує conversion між void * та object pointers, але не задає такого самого правила для function pointers."
track: embedded
section: function-pointers-and-callbacks
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

<span class="warn">C не гарантує portable conversion між function pointer і object pointer `void *`.</span>

Представлення й розмір різних категорій вказівників залежать від реалізації; ISO C визначає conversion між `void *` та object pointers, але окремо такого правила для function pointers не задає. POSIX має окремі вимоги для `dlsym`, але це не загальне правило ISO C і не embedded-гарантія.[^iso-c-n1570]

Захист: зберігай function pointers у function pointer types, а data pointers у `void *`. Не клади callback адресу в generic data pointer field.[^iso-c-n1570]

## Detailed explanation

Function pointer і `void *` належать до різних категорій типів у C: перший вказує на функцію, другий є вказівником на об’єкт. Стандарт гарантує перетворення `void *` до та з вказівника на будь-який об’єктний тип із збереженням рівності після зворотного перетворення. Окреме правило для вказівника на функцію дозволяє перетворення між сумісними function pointer типами та назад, але не проголошує загальне перетворення між function pointer та object pointer.[^iso-c-n1570]

Отже, поле структури типу `void *context` підходить для передачі адреси об’єкта-контексту, але не є переносним універсальним контейнером для callback. На конкретному ABI може працювати явне перетворення, проте покладатися на нього можна лише за документованої гарантії платформи. Не робіть висновок про однаковий розмір або представлення вказівників з того, що на поширеній MCU вони мають однаковий розмір: цього не вимагає правило про `void *`.[^iso-c-n1570]

Типовий симптом – компілятор попереджає про перетворення між несумісними типами або код компілюється лише після cast, а потім працює не на іншому target. Cast прибирає частину діагностик, але не створює гарантій сумісності ABI. Для callback оголосіть поле точним function pointer типом або використайте `typedef`; для даних і контексту лишіть `void *`.[^iso-c-n1570]

Наприклад, структура може мати окремі поля `void (*callback)(void *)` і `void *context`. Перше зберігає адресу функції з визначеною сигнатурою, друге – адресу об’єкта контексту; функція отримує контекст під час виклику. Такий поділ зберігає типову інформацію й не потребує трактувати адресу коду як адресу даних.[^iso-c-n1570]

**Типові помилки:**

- Вважати `void *` універсальним вказівником на будь-яку адресу.
- Використовувати cast як доказ, що conversion переносне.
- Зберігати callback у полі даних, не документувавши залежність від конкретної платформи.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

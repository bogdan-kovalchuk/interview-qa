---
id: emb-volconst-0032
title: "Trap: чи безпечно прибрати `const` cast-ом?"
description: "Ні: якщо початковий об’єкт був оголошений const, спроба змінити його через non-const lvalue має undefined behavior."
track: embedded
section: volatile-and-const
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

## Question code

```c
const uint32_t cfg = 10;
uint32_t *p = (uint32_t *)&cfg;
*p = 20;
```

## Short answer

<span class="warn">Ні: якщо початковий об’єкт був оголошений `const`, спроба змінити його через non-const lvalue має undefined behavior.</span>

На MCU `cfg` може лежати у Flash/`.rodata`, і запис через `p` може спричинити BusFault/HardFault або просто не змінити дані. Навіть якщо адреса в RAM, оптимізатор може припускати, що `cfg` не змінюється.

Захист: не cast-away `const` для запису. Якщо дані мають змінюватися, вони не повинні бути `const`.[^iso-c-n1570]

## Detailed explanation

Cast-away `const` видаляє обмеження типу для конкретного доступу, але не змінює властивостей самого об’єкта. У прикладі `cfg` оголошено як `const uint32_t`, а `p` має тип вказівника на змінюваний `uint32_t`; присвоєння через `*p` намагається змінити початково незмінний об’єкт. За правилом C така спроба має undefined behavior, навіть якщо cast компілюється без діагностики.[^iso-c-n1570]

Наслідок на MCU залежить від реалізації: об’єкт може бути розміщений у Flash або read-only секції, і апаратний запис може завершитися fault чи не змінити значення. Навіть якщо він лежить у RAM, компілятор може використовувати припущення, що значення `const`-об’єкта не змінюється коректною програмою. Тому повторне читання може бути оптимізоване, а налагодження за фактичним вмістом пам’яті не перетворює програму на визначену.[^iso-c-n1570]

Це відрізняється від ситуації, коли початковий об’єкт змінюваний, але його адресу тимчасово передали через `const uint32_t *`. Зняття кваліфікатора й запис тоді можливі, якщо інші правила типів і доступу також дотримано. Проте cast приховує намір від API та читача, тож краще передати змінюваний вказівник або змінити контракт функції.[^iso-c-n1570]

Приклад:

```c
uint32_t value = 10;
const uint32_t *view = &value;
*(uint32_t *)view = 20; // об’єкт value не оголошений const
```

**Типова помилка:** плутати змінність вказівника з кваліфікатором об’єкта. Cast не «розконсервовує» сховище і не переносить `cfg` у RAM; він лише змінює тип виразу. Якщо конфігурацію потрібно змінювати під час роботи, оголосіть її змінюваною та застосуйте відповідне сховище й механізм оновлення.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

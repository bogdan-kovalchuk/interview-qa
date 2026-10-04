---
id: emb-align-0031
title: "Trap: чому `*(uint32_t*)&buf[1]` небезпечно?"
description: "Невирівняне перетворення pointer може мати undefined behaviour; реакція апаратури залежить від платформи."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: pitfall
tags: []
status: published
updated: 2026-10-04
content_revision: 2
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
    applicability: "Авторитетне джерело рівня секції для згаданих правил мови C; конкретні пристрої й тулчейни можуть відрізнятися."
---

## Question code

```c
uint8_t buf[8];
uint32_t v = *(uint32_t*)&buf[1];
```

## Short answer

<span class="warn">Зсунутий pointer може не мати alignment для `uint32_t`, тому перетворення або доступ через нього може мати undefined behaviour; наслідок на апаратурі залежить від архітектури й конфігурації.</span> Також читання байтів як `uint32_t` може порушити правила effective type.[^iso-c-n1570]

Перетворення `uint8_t*` -> `uint32_t*` не вирівнює адресу й не робить байтовий об’єкт об’єктом типу `uint32_t`.[^iso-c-n1570]

Захист від невирівняного typed load: `memcpy(&v, &buf[1], sizeof v);`, якщо джерело має щонайменше `sizeof v` байтів. Це не визначає byte order протоколу – за потреби декодуй байти явно.[^iso-c-n1570]

## Detailed explanation

`&buf[1]` вказує на другий байт масиву. Якщо його адреса не відповідає alignment для `uint32_t`, cast на `uint32_t*` не виправляє адресу. За правилами C перетворення pointer, результат якого не вирівняний належно для типу призначення, має undefined behaviour; подальше читання також мусить відповідати правилам доступу до об’єктів та effective type.[^iso-c-n1570]

На MCU можливі різні прояви: процесор може виконати unaligned access, розбити його на кілька операцій, сповільнити його або згенерувати fault. Це залежить від архітектури, інструкції та конфігурації, тому твердження «завжди HardFault» або «завжди лише штраф» некоректне без зазначення платформи.[^iso-c-n1570]

Щоб скопіювати байти у вирівняну локальну змінну, можна використати `memcpy(&v, &buf[1], sizeof v);`, якщо від offset 1 у джерелі є щонайменше `sizeof v` байтів. Це оминає typed load з невирівняного джерела, але числове значення залежатиме від native byte order MCU.[^iso-c-n1570]

Якщо байти надходять із протоколу, декодуй їх за явно заданим форматом: byte order, signedness і ширину поля визначає протокол, а не pointer cast. Для короткого поля можна зібрати число з окремих байтів або скористатися перевіреним decoder; `memcpy` не перетворює endianness.[^iso-c-n1570]

**Типові помилки:**
- Вважати cast еквівалентом копіювання або конвертації.
- Приписувати однакову реакцію всім Cortex-M моделям.
- Забути, що після `memcpy` може знадобитися декодувати byte order.

Для цього фрагмента спершу перевір межі буфера, скопіюй байти без pointer punning, а потім застосуй явно визначений порядок байтів повідомлення.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

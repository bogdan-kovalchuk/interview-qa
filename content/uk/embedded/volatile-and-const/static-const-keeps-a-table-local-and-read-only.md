---
id: emb-volconst-0056
title: "Що означає `static const` для таблиці всередині C-файлу?"
description: "static обмежує linkage цим translation unit, а const робить дані read-only через цей identifier."
track: embedded
section: volatile-and-const
level: junior
type: concept
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

**На рівні файлу `static` дає identifier internal linkage, а `const` забороняє зміну через цей identifier.**

Для embedded lookup table це поширена форма: інші translation units не бачать символ, а compiler може розмістити таблицю в read-only section. Розміщення у Flash залежить від linker script і платформи.

Правило: file-private immutable tables оголошуй як `static const`, якщо вони не мають бути частиною зовнішнього ABI.[^iso-c-n1570]

## Detailed explanation

`static const` для об’єкта на рівні файлу в C поєднує internal linkage зі змогою читати об’єкт, але не змінювати його через це ім’я. `static` тут стосується видимості імені між translation units, а `const` є кваліфікатором типу, а не гарантією фізичного захисту пам’яті.[^iso-c-n1570]

Internal linkage залишає таблицю приватною деталлю реалізації: інші `.c` файли не можуть звернутися до цього імені через звичайне зовнішнє оголошення. `const` забороняє зміну через const-qualified lvalue; спроба змінити об’єкт, визначений як const, через приведений неконстантний pointer має undefined behaviour.[^iso-c-n1570]

Куди потраплять байти, вирішують реалізація, linker script та архітектура. Compiler або linker часто кладуть таблицю в read-only section на кшталт `.rodata`, але стандарт C не гарантує ані назви секції, ані Flash. Для embedded-проєкту перевір linker map, якщо розміщення важливе.[^iso-c-n1570]

Приклад: `static const uint16_t gains[] = { 10, 20, 40 };` дає локальне для translation unit ім’я `gains`, а `gains[0] = 5` є недопустимим присвоєнням. Якщо таблиця потрібна іншим файлам, визнач її один раз без `static`, а в заголовку оголоси відповідний `extern` з узгодженим типом.[^iso-c-n1570]

**Типова помилка:** вважати, що ключове слово саме переносить дані у Flash. Воно задає правила мови для linkage і модифікації через тип; фізичний образ пам’яті визначає збірка прошивки. Перевір адресу й секцію в map-файлі.

## Sources

<!-- generated from frontmatter -->

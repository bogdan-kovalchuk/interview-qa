---
id: emb-structs-0008
title: "Що перевіряє цей код?"
description: "Під час компіляції перевіряє offset 0x14 для поля ODR у GPIO_TypeDef."
track: embedded
section: structs-unions-and-bitfields
level: junior
type: mechanism
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
_Static_assert(offsetof(GPIO_TypeDef, ODR) == 0x14,
               "bad GPIO layout");
```

## Short answer

Він перевіряє під час компіляції, що поле `ODR` у `GPIO_TypeDef` має offset `0x14`.

Для peripheral struct overlay це критично: якщо попередні поля або reserved gaps описані неправильно, `GPIOA->ODR` звертатиметься не до output data register, а до іншої адреси. На Cortex-M це може означати неправильну периферію, silent bug або fault.

Для такого твердження потрібні правильні визначення типу та `<stddef.h>` для `offsetof`; assertion перевіряє layout компіляції, але не підтверджує адресу бази периферії чи правильність самого hardware manual.[^iso-c-n1570]

## Detailed explanation

`_Static_assert` перевіряє константний вираз під час компіляції. Якщо `offsetof(GPIO_TypeDef, ODR)` не дорівнює `0x14`, компілятор видає діагностику з повідомленням `bad GPIO layout`, і збірка не проходить. У C11 макрос `offsetof` потрібно отримати з `<stddef.h>`; `GPIO_TypeDef` має бути визначеним типом структури з членом `ODR`.[^iso-c-n1570]

Це корисно для memory-mapped peripheral описів: поля структури представляють регістри, а зарезервовані проміжки задають їхні offsets. Помилка у типі попереднього поля, пропущений reserved gap або зміна packing може посунути `ODR`; звичайне звернення через `GPIOA->ODR` тоді потрапить за іншою адресою. Compile-time перевірка робить таку зміну видимою до запуску прошивки.[^iso-c-n1570]

Приклад трактує `0x14` як byte offset від початку `GPIO_TypeDef`. Це не абсолютна адреса периферії: базова адреса `GPIOA` і конкретний register map мають походити з документації саме цього MCU та його заголовків. Умова також перевіряє тільки одне поле, а не повноту всієї структури.

**Типова помилка:** сприймати успішний assertion як доказ, що регістр існує за правильною фізичною адресою. Перевіряйте джерело базової адреси окремо, додавайте assertions для важливих полів і звіряйте структуру з reference manual; `offsetof` лише порівнює layout, сформований компілятором, із заданим числом.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

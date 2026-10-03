---
id: emb-volconst-0033
title: "Коли cast-away `const` не є UB, а коли стає UB?"
description: "Cast-away const сам по собі не обов’язково UB; UB виникає при записі в об’єкт, який реально був оголошений const."
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

**Cast-away `const` сам по собі не обов’язково UB; UB виникає при записі в об’єкт, який реально був оголошений `const`.**

Якщо є mutable object `uint32_t x`, потім `const uint32_t *cp = &x`, то технічно можна повернути `uint32_t *p = (uint32_t *)cp` і змінити `x`. Але це поганий API-сигнал. Якщо object був `const uint32_t cfg`, запис через cast має undefined behavior.[^iso-c-n1570]

Правило: не використовуй cast для обходу type contract; виправляй сигнатуру або ownership моделі.[^iso-c-n1570]

## Detailed explanation

Сам cast-away `const` змінює кваліфікований тип виразу-вказівника, але не записує дані й сам по собі не створює undefined behavior. Важливо, яким є об’єкт за адресою: C визначає undefined behavior саме для спроби модифікувати об’єкт, оголошений із `const`-кваліфікованим типом, через lvalue без `const`.[^iso-c-n1570]

У першому прикладі `x` має звичайний змінюваний тип `uint32_t`. `cp` лише надає доступ для читання; після зняття кваліфікатора вказівник знову може надати змінюваний доступ до того самого об’єкта. Це не означає, що cast завжди безпечний: доступ має відповідати фактичному типу та правилам часу життя об’єкта, а інші обмеження aliasing і синхронізації залишаються чинними.[^iso-c-n1570]

У другому прикладі `cfg` від початку оголошений як `const uint32_t`. Спроба присвоєння через `p` не стає дозволеною від того, що `p` має тип `uint32_t *`; доступ через це lvalue порушує правило для const-об’єкта. Реалізація може розмістити такий об’єкт у read-only пам’яті, але апаратний fault – лише можливий прояв, а не визначення правила мови.[^iso-c-n1570]

Приклад:

```c
uint32_t x = 1;
const uint32_t *read_only_view = &x;
uint32_t *write_view = (uint32_t *)read_only_view;
*write_view = 2; // допустимо для самого об’єкта x
```

**Типова помилка:** казати, що «сам cast є UB» або, навпаки, що «після cast запис завжди безпечний». Критерій – чи дозволено змінювати об’єкт за цією адресою. У коді краще виправити сигнатуру функції, якщо вона без потреби приймає `const`, замість приховувати запис cast-ом.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

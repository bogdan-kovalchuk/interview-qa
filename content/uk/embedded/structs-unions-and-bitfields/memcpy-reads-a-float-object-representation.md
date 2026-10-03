---
id: emb-structs-0017
title: "Як безпечніше отримати біти `float` як `uint32_t` у C?"
description: "Через memcpy: uint32_t bits; memcpy(&bits, &f, sizeof bits); memcpy копіює object representation байт-в-байт і не порушує strict aliasing."
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

## Short answer

**Через `memcpy`**:

`uint32_t bits; memcpy(&bits, &f, sizeof bits);`

`memcpy` копіює object representation байт за байтом і не порушує правила доступу через несумісний тип. Значення отриманого `uint32_t` залежить від розміру та представлення обох типів і порядку байтів.[^iso-c-n1570]

Для копіювання представлення `memcpy` є переносним щодо правил aliasing; це не обіцяє переносного числового значення бітів на різних платформах.[^iso-c-n1570]

## Detailed explanation

`memcpy` копіює байти object representation між ділянками пам’яті, не звертаючись до об’єкта `float` через lvalue типу `uint32_t`. Тому цей спосіб уникає проблеми aliasing, яку створив би pointer cast на несумісний тип.[^iso-c-n1570]

Щоб копія була коректною, цільовий об’єкт має вмістити всі скопійовані байти. У прикладі `sizeof bits` визначає довжину копії; якщо розміри `float` і `uint32_t` різні, читати повне представлення як один `uint32_t` не можна. Перевіряйте припущення під час компіляції, наприклад `_Static_assert(sizeof(float) == sizeof(uint32_t), "size mismatch");`.[^iso-c-n1570]

**Приклад:**

```c
float f = 1.0f;
uint32_t bits;
memcpy(&bits, &f, sizeof bits);
```

Тут копіюються байти `f`, а не виконується арифметичне перетворення. Конкретне значення `bits` залежить від формату `float` і endian-порядку; стандарт C не вимагає, щоб `float` мав IEEE 754 binary32. Для обміну файлами чи мережевим протоколом краще визначити формат явно, а потім кодувати поля відповідно до нього.[^iso-c-n1570]

Компілятор часто може вбудувати малу копію, але це оптимізаційна можливість, а не семантична гарантія, тому на це не слід покладати коректність. У C++20 аналогічний інструмент для перетворення object representation у значення – `std::bit_cast`, який також має вимогу однакового розміру типів.[^iso-c-n1570]

**Типова помилка:** називати `memcpy` перетворенням `float` на ціле. Воно лише переносить байти; для числового результату використовуйте звичайне перетворення типу, а для бітового протоколу фіксуйте формат і порядок байтів.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

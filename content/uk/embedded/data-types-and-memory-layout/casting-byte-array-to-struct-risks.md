---
id: emb-dtypes-0107
title: "Які ризики виникають, якщо привести масив байтів до структури у C?"
description: "Пряме приведення uint8_t* до struct* ризикує порушити alignment, strict aliasing і очікуваний layout з padding. Також frame може мати інший endianness або packed формат. Безпечніше читати поля через memcpy у локальні типи."
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
  - source_id: dou-embedded-interview
    title: "DOU: Питання співбесід Embedded Engineer (Anki-колода спільноти)"
    url: https://dou.ua/lenta/articles/interview-embedded-engineer/
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

Пряме приведення `uint8_t*` до `struct*` ризикує порушити <span class="warn">alignment</span>, strict aliasing і очікуваний layout з padding. Також frame може мати інший endianness або packed формат, ніж ABI компілятора. Безпечніше читати поля через `memcpy` у локальні типи, перевіряти довжину й явно конвертувати byte order.[^iso-c-n1570]

## Detailed explanation

Пряме приведення адреси першого байта до `struct*` створює вказівник, ніби в буфері вже розміщений об’єкт цієї структури. Але мережевий чи файловий буфер зазвичай є послідовністю байтів, а не об’єктом із layout, який обрав компілятор. Для доступу через такий вказівник адреса також має задовольняти alignment структури; інакше поведінка не визначена стандартом C, навіть якщо конкретний процесор іноді виконує невирівняний доступ.[^iso-c-n1570]

Навіть правильне вирівнювання не розв’язує всі проблеми. Поля структури розміщуються за правилами ABI: між ними можуть бути padding bytes, а розміри й alignment типів залежать від реалізації. Порядок байтів multi-byte числа також може не збігатися з wire format. `packed` атрибут прибирає частину padding лише як розширення конкретного компілятора; він не конвертує endianness і може створити невирівняні поля.[^iso-c-n1570]

Є й питання типового доступу. У C правила effective type обмежують читання об’єкта через несумісний тип; доступ через character type має окремий виняток, але це не перетворює сирий пакет на коректно ініціалізовану структуру. У C++ діють правила lifetime та object model, тож ті самі припущення не можна механічно переносити між мовами.[^iso-c-n1570]

Надійний декодер спершу перевіряє, що буфер містить повне поле, копіює байти до локального об’єкта через `memcpy` або збирає число з байтів, а тоді явно перетворює byte order. Для signed та floating-point значень окремо враховують представлення, яке визначає протокол.

Приклад: для двох байтів little-endian спочатку перевірити `length >= 2`, потім обчислити значення з молодшого та старшого байтів. Це усуває залежність від alignment структури й порядку байтів хоста.

**Типові помилки:**
- Вважати, що cast виконує копіювання або byte-order conversion.
- Покладатися на `sizeof(struct)` як на розмір wire frame.
- Вважати, що `packed` робить доступ переносимим на всіх процесорах і компіляторах.[^iso-c-n1570]

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

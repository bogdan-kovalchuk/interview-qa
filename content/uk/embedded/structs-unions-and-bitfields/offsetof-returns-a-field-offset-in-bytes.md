---
id: emb-structs-0007
title: "Що таке `offsetof` і навіщо він потрібен?"
description: "offsetof(T, field) повертає offset поля всередині структури в байтах."
track: embedded
section: structs-unions-and-bitfields
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

**`offsetof(T, field)`** повертає offset поля всередині структури в байтах.

Це стандартний макрос із `<stddef.h>` для перевірки layout без ручного підрахунку. У embedded його використовують у static assertions для register maps, protocol headers, Flash records і DMA descriptors.

Якщо hardware manual задає `STATUS` на offset `0x10`, це можна перевірити через `_Static_assert(offsetof(Type, STATUS) == 0x10, "...")`. `offsetof` не застосовують до bit-field членів.[^iso-c-n1570]

## Detailed explanation

`offsetof(T, field)` дає зсув у байтах від початку об’єкта типу `T` до вказаного поля. Макрос оголошено в `<stddef.h>`; результат має тип `size_t` і під час компіляції може бути цілим константним виразом. Він враховує padding перед полем, тому корисний для перевірки фактичного layout структури.[^iso-c-n1570]

У звичайній структурі перше поле починається з offset 0, але наступні поля можуть мати проміжки через вимоги alignment. Наприклад, компілятор може розмістити `uint32_t` за offset 4 після однобайтового поля. `offsetof` повідомить саме зсув поля в обраному ABI, а не позицію, обчислену з суми попередніх розмірів.[^iso-c-n1570]

Це зручно для перевірки периферійних описів та структур, що мають узгоджений двійковий layout. Якщо документація задає `STATUS` на offset `0x10`, compile-time assertion може зупинити збірку, коли зміна типу, порядок полів або опція компілятора порушить це очікування. Така перевірка підтверджує лише layout цієї збірки; вона не доводить, що адреса бази периферії правильна або що опис відповідає документації.[^iso-c-n1570]

Приклад перевірки для C11:

```c
_Static_assert(offsetof(struct Device, STATUS) == 0x10,
               "STATUS offset mismatch");
```

**Типова помилка:** трактувати `offsetof` як абсолютну адресу поля. Це відносне зміщення від початку структури. Макрос також не можна застосовувати до bit-field, оскільки такий член не має адреси, яку можна виразити у байтах.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

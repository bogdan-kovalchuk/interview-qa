---
id: emb-macros-0033
title: "Як зробити compile-time перевірку без `static_assert` (старий C)?"
description: "Коли константна умова хибна, межа масиву стає -1 і порушує обмеження мови, тому компілятор видає діагностику під час трансляції."
track: embedded
section: inline-and-macros
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
  - source_id: iso-c-array-static-assert
    title: "ISO/IEC 9899:201x Committee Draft N1570, array declarators and static assertions"
    url: https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf
    accessed: 2026-10-04
    kind: spec
    version: N1570
    applicability: "C array bounds, integer constant expressions, constraint diagnostics, and _Static_assert in C11; it does not prescribe that every compiler abort after a diagnostic."
---

## Question code

```c
#define STATIC_ASSERT(c, name) \
  typedef char name[(c) ? 1 : -1]
```

## Short answer

**Трюк із від’ємним розміром масиву**: якщо константна умова хибна, межа стає `-1` і порушує обмеження мови, тож компілятор має видати діагностику, але може продовжити роботу.[^iso-c-array-static-assert]

Це старий спосіб перевірити властивість типу під час компіляції, наприклад розмір структури, якщо перевірка є константною: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)`.[^iso-c-array-static-assert]

У C11 і C++11 є відповідно `_Static_assert` і `static_assert` із діагностичним повідомленням.[^iso-c-array-static-assert]

## Detailed explanation

Макрос може перетворити умову на розмір масиву: за істини межа дорівнює `1`, а за хиби – `-1`. Від’ємна межа порушує обмеження мови й вимагає діагностики під час трансляції, але стандарт не зобов’язує компілятор негайно зупинитися після неї. Звичний toolchain зазвичай не створить об’єктний файл після такої діагностики.[^iso-c-array-static-assert]

У макросі `c` має бути цілочисловим константним виразом. `sizeof(Frame)` підходить для повного типу `Frame`, а значення, відоме лише під час виконання, – ні. Ім’я typedef також має бути унікальним у своїй області видимості, щоб успішна перевірка не спричинила конфлікт.[^iso-c-array-static-assert]

Це був поширений прийом до стандартних static assertion. Починаючи з C11 можна використати `_Static_assert`, який чітко висловлює задум і дозволяє вказати повідомлення; у C++11 є `static_assert`. Переносний код має обрати конструкцію за мовою та версією стандарту, а не припускати, що будь-який старий embedded-компілятор підтримує новіший синтаксис.[^iso-c-array-static-assert]

Приклад: `STATIC_ASSERT(sizeof(Frame) == 8, frame_size)` приймає структуру рівно восьми байтів і викликає діагностику, якщо умова хибна. Це не перевірка під час запуску і не спосіб виправити невідповідний layout: якщо потрібний розмір не виконується на цільовій ABI, треба розібратися з типами, вирівнюванням та padding.

**Типова помилка:** передати змінну часу виконання й очікувати оцінки під час компіляції. Використовуй константні умови, унікальне ім’я typedef, а за підтримки стандарту – `_Static_assert` або `static_assert`.

## Sources

<!-- generated from frontmatter -->

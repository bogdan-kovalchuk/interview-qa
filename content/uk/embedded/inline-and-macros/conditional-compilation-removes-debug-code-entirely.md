---
id: emb-macros-0017
title: "Як зробити debug-only код, який повністю зникає у release-збірці?"
description: "Conditional compilation: при DEBUG макрос розгортається у printf, інакше – у порожнечу, і код повністю прибирається ще до компіляції (нуль flash/RAM)."
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
  - source_id: gcc-cpp-overview
    title: "GCC CPP: Overview"
    url: https://gcc.gnu.org/onlinedocs/cpp/Overview.html
    accessed: 2026-10-04
    kind: official
    version: "current"
    applicability: "Пояснює препроцесинг як етап до компіляції; не гарантує конкретний розмір бінарного файла для будь-якого toolchain."
---

## Question code

```c
#ifdef DEBUG
  #define DBG(fmt, ...) printf(fmt, ##__VA_ARGS__)
#else
  #define DBG(fmt, ...)
#endif
```

## Short answer

**Conditional compilation**: коли визначено `DEBUG`, макрос розгортається у `printf`; інакше виклик стає порожнім і не потрапляє до компілятора як C-код.

Це відрізняється від `if (debug)`: препроцесор вилучає текст до компіляції, але фактичний розмір прошивки залежить і від інших посилань та налаштувань збірки.

Визначай `DEBUG` через build-флаг (`-DDEBUG`) та перевіряй конфігурацію release окремо.[^gcc-cpp-overview]

## Detailed explanation

Conditional compilation дає змогу включати або пропускати частини translation unit за умовою, відомою препроцесору. Для debug-макросу `#ifdef DEBUG` перевіряє саме факт визначення імені: значення `DEBUG=0` також вважається визначеним, тому release-конфігурація має або не визначати його, або використовувати умову на значенні, наприклад `#if DEBUG`.[^iso-c-n1570]

У прикладі гілки `#ifdef` і `#else` обираються до компіляції. Якщо `DEBUG` не визначено, тіло `DBG(...)` порожнє; аргументи виклику, включно з обчисленнями, також зникають з C-програми. Це корисно для дорогих діагностичних викликів, але може приховати побічний ефект, якщо програміст передасть у макрос вираз, що змінює стан. З цієї причини debug-інструментування не повинно бути єдиним місцем виконання потрібної логіки.

Твердження про «нуль flash/RAM» надто абсолютне: вилучення саме цього виклику прибирає його внесок, однак функція `printf` може використовуватися іншим кодом, а linker та налаштування оптимізації визначають підсумковий образ. Так само звичайний `if` із compile-time умовою іноді буде оптимізований, але це інше джерело гарантії; `#ifdef` взагалі не передає невибрану гілку компілятору.[^gcc-cpp-overview]

Приклад конфігурації: у debug target build-система передає `-DDEBUG`; у release target цей прапорець відсутній. Перевірка препроцесованого файлу для обох конфігурацій допомагає переконатися, що діагностичні виклики видалені саме там, де потрібно. Не додавайте `#define DEBUG` у загальний заголовок: тоді прапорець збірки вже не зможе керувати режимом надійно.

**Типові помилки:**

- Вважати `#ifdef DEBUG` хибним, коли `DEBUG` визначено як `0`.
- Передавати в debug-макрос вираз із потрібним побічним ефектом.
- Обіцяти нульовий розмір усієї діагностичної інфраструктури, не перевіривши linker map.

## Sources

<!-- generated from frontmatter -->

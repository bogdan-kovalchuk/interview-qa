---
id: emb-structs-0031
title: "Trap: чому positional initializer крихкий?"
description: "Значення прив’язані до порядку полів, а не до імен."
track: embedded
section: structs-unions-and-bitfields
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
struct Cfg { uint32_t baud; uint8_t parity; uint8_t stop; };
struct Cfg c = { 115200, 0, 1 };
```

## Short answer

<span class="warn">Значення прив’язані до порядку полів, а не до імен.</span>

Якщо хтось вставить нове поле між `baud` і `parity`, initializer може залишитися синтаксично валідним, але значення поїдуть у неправильні поля. У driver configs це створює тихі runtime bugs.

Захист: для non-trivial structs використовуй designated initializers: `{ .baud = 115200, .parity = 0, .stop = 1 }`.[^iso-c-n1570]

## Detailed explanation

Позиційний aggregate initializer зіставляє перше значення з першим полем структури, друге – з другим і так далі. Тому його зміст залежить від порядку членів у декларації, а не від їхніх назв.[^iso-c-n1570]

Пастка проявляється після зміни структури. Якщо між `baud` і `parity` вставити нове поле, старий список `{ 115200, 0, 1 }` може залишитися синтаксично допустимим, але `0` тепер ініціалізує нове поле, а решта значень зсуваються. Компілятор часто не може визначити, що автор мав на увазі інше призначення; помилка може проявитися лише під час роботи пристрою.

Для короткої локальної структури з очевидними типами позиційна форма іноді читається нормально. Для довгої конфігурації драйвера значення на кшталт `{ 115200, 0, 1 }` не пояснюють, яке поле отримує кожне число. Designated initializer прив’язує значення до назви: `{ .baud = 115200, .parity = 0, .stop = 1 }`. За такого стилю перестановка полів не перенаправить ці значення на інші члени.[^iso-c-n1570]

Приклад: якщо додається `uint8_t mode` перед `parity`, старий initializer тепер призначає `0` полю `mode`, а `1` – `parity`; `stop` лишається неявно нульовим. Саме така тиха зміна конфігурації є типовим симптомом проблеми. У C++ aggregate initialization також має позиційний порядок, однак наведені правила designated initializers у цьому матеріалі стосуються синтаксису C.[^iso-c-n1570]

**Типова помилка:** перевірити лише, що код компілюється. Після зміни полів треба звірити семантику всіх initializer-ів; для конфігурацій використовувати назви полів і тестувати значення, які передаються драйверу.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

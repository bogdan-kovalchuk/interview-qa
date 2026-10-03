---
id: emb-structs-0030
title: "Що буде з незаданими полями?"
description: "parity і stop_bits будуть zero-initialized."
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
struct Cfg {
    uint32_t baud;
    uint8_t parity;
    uint8_t stop_bits;
};

struct Cfg c = { .baud = 115200 };
```

## Short answer

**`parity` і `stop_bits` будуть zero-initialized.**

Aggregate initialization у C занулює поля, які не були явно ініціалізовані. Це зручно для config structs, де `0` є valid default.

Правило: designated initializers зменшують ризик переплутати positional fields, але default zero має бути семантично коректним. Якщо `0` небезпечний, потрібен factory/default function.[^iso-c-n1570]

## Detailed explanation

Для aggregate initializer у C поля структури, яких немає у списку ініціалізації, отримують значення так, ніби їх ініціалізували константою `0`. Для арифметичних типів це числовий нуль, для вказівників – null pointer, а для вкладених агрегатів правило застосовується рекурсивно до їхніх членів.[^iso-c-n1570]

У прикладі явно задано лише `.baud`, тому `parity` і `stop_bits` мають нульові значення. Це не особливість designated initializer: такий самий ефект має пропуск членів в aggregate initializer з позиційними значеннями. Назви полів роблять запис читабельним, а правило нульового заповнення стосується самого агрегатного ініціалізатора.[^iso-c-n1570]

Нульове значення не означає автоматично «вимкнено», «за замовчуванням» або «безпечний режим». У конкретному драйвері нуль може означати parity none, але в іншому API може бути зарезервованим кодом або невірною кількістю stop bits. Перевірте визначення кожного поля та вимоги до периферії, перш ніж покладатися на неявне заповнення.

Приклад: якщо нульовий `parity` позначає відсутність перевірки парності, `{ .baud = 115200 }` може бути валідним. Якщо ж нульовий `mode` заборонений протоколом, структуру варто ініціалізувати явними значеннями або підготувати через функцію, яка встановлює валідну конфігурацію.[^iso-c-n1570]

**Типова помилка:** трактувати нульове заповнення як логіку прикладного рівня. Компілятор застосовує правило ініціалізації C; він не знає, яке значення є безпечним для UART чи іншого пристрою.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

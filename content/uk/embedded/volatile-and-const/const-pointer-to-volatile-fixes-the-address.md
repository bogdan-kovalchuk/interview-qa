---
id: emb-volconst-0012
title: "Що означає `volatile uint32_t * const reg`?"
description: "reg є const pointer to volatile uint32_t."
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

**`reg` є const pointer to volatile `uint32_t`**.

Адресу вказівника змінити не можна: `reg = other` порушує обмеження мови й вимагає діагностики. Дані за адресою мають тип `volatile uint32_t`, тож доступ до них є volatile-доступом за правилами конкретної реалізації. Це типовий тип для фіксованої адреси writable hardware register.[^iso-c-n1570]

Embedded-use case: адреса GPIO output register стала, а вміст регістра може змінюватися апаратурою або записами firmware.[^embeddedinterviewlab]

## Detailed explanation

У декларації `volatile uint32_t * const reg` є два незалежні кваліфікатори. `const` стоїть після `*`, тому стосується самого вказівника: після ініціалізації його адресу не можна перепризначити. `volatile` стоїть у типі `uint32_t` ліворуч від `*`, тому стосується об’єкта, на який указує `reg`. Такі декларації зручніше читати від імені `reg` назовні: це const pointer до volatile `uint32_t`.[^iso-c-n1570]

Для регістра периферії базова адреса задається схемою пам’яті пристрою й не має змінюватися під час роботи цієї змінної. Натомість значення регістра може змінюватися через запис програми або через периферію. Поєднання кваліфікаторів виражає саме ці різні властивості: `const` забороняє змінювати адресу через `reg`, а `volatile` повідомляє реалізації, що об’єкт за адресою має volatile-кваліфікований тип. Стандарт вимагає обчислювати вирази з такими об’єктами за правилами абстрактної машини, але конкретне визначення доступу до volatile є implementation-defined.[^iso-c-n1570]

Це не робить тип універсально правильним для кожного регістра. Розмір доступу, вирівнювання, адреса, read/write властивості й побічні ефекти визначаються документацією MCU та ABI компілятора. Наприклад, деякий регістр може вимагати 16-бітних операцій або мати біти, які очищуються читанням; одного `volatile uint32_t` недостатньо, щоб описати такі апаратні правила. Так само `volatile` сам по собі не забезпечує атомарності чи бар’єрів пам’яті.[^iso-c-n1570]

Приклад декларації з адресою, визначеною платформою:

```c
volatile uint32_t * const gpio_output = (volatile uint32_t *)GPIO_OUTPUT_ADDRESS;
```

Після створення вказівника код не може присвоїти йому іншу адресу, однак доступ через `*gpio_output` зберігає volatile-кваліфікатор даних. Якщо адреса повинна бути змінною, прибери `const` із самого вказівника; якщо регістр за специфікацією read-only, додай `const` до типу даних. Вибір кваліфікаторів має відображати окремо сталість адреси та допустимість доступу до даних.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

---
id: emb-structs-0009
title: "Trap: що не так із таким register map?"
description: "Можуть бракувати reserved gaps між регістрами."
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
typedef struct {
    volatile uint32_t CR;
    volatile uint32_t SR;
    volatile uint32_t DR;
} UART_TypeDef;
```

## Short answer

<span class="warn">Можуть бракувати reserved gaps між регістрами.</span>

Hardware register map часто має пропуски адрес. Якщо manual каже, що `DR` на offset `0x10`, а структура ставить його на offset `0x08`, усі доступи після gap будуть неправильними. `volatile` не рятує неправильний layout.

Захист: додавай reserved поля потрібного розміру, наприклад `uint32_t RESERVED0[2]`, і перевіряй `offsetof`.[^iso-c-n1570]

## Detailed explanation

Register map у C-структурі має відтворювати адреси периферійних регістрів, визначені reference manual мікроконтролера. Компілятор розміщує поля за правилами ABI та вирівнювання, а не за знанням про апаратну периферію, тому послідовні поля самі собою не означають, що адреси регістрів збігаються з апаратними адресами.[^iso-c-n1570]

У наведеному прикладі `CR`, `SR` і `DR` ідуть без проміжних полів. Якщо кожен регістр має ширину 32 біти, offsets перших двох дорівнюють `0x00` і `0x04`; третій буде на `0x08`. Але якщо документація задає `DR` на `0x10`, у структурі бракує восьми байтів між `SR` та `DR`. Цей проміжок описують reserved полем відповідного типу й розміру, а адресу базового об’єкта задають окремо згідно з картою пам’яті пристрою.

Помилка часто проявляється не під час компіляції, а як керування не тим регістром: запис у `DR` може потрапити в інше місце, а читання status register – повернути неочікуване значення. `volatile` вимагає виконувати відповідні доступи через volatile lvalue, але не змінює розташування полів і не виправляє неправильний offset.[^iso-c-n1570]

**Приклад перевірки:**

Для заданого target перевіряйте `offsetof(UART_TypeDef, DR)` та `sizeof` полів assertions-ами збірки, зіставляючи числа з таблицею регістрів у manual. Для offset `0x10` і чотирибайтових слів потрібні два 32-бітні reserved slots після `SR`, якщо саме така карта пам’яті задана виробником. Не копіюйте кількість slots з іншої моделі MCU: схожі периферійні блоки можуть мати різні карти адрес.[^iso-c-n1570]

**Типові помилки:**

- Вважати, що compiler padding автоматично створить саме апаратні reserved gaps.
- Перевірити лише загальний `sizeof`, не перевіривши offset кожного важливого поля.
- Приписувати `volatile` властивість керувати layout структури.

Для регістрів також враховуйте правила доступу з документації: ширину читання/запису, read-to-clear поведінку та заборонені reserved addresses. Структура є зручним способом опису карти, але сама по собі не перевіряє її відповідність конкретному MCU.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

---
id: emb-structs-0025
title: "Як безпечніше встановити поле register без bit-field?"
description: "Типовий патерн: mask + shift."
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
  - source_id: stm32-w1c-manual
    title: "SR5E1x 32-bit Arm Cortex-M7 architecture microcontroller reference manual"
    url: https://www.st.com/resource/en/reference_manual/rm0483-sr5e1x-32bit-arm-cortexm7-architecture-microcontroller-for-electrical-vehicle-applications-stmicroelectronics.pdf
    accessed: 2026-10-04
    kind: official
    version: "RM0483 Rev 6"
    applicability: "Приклад визначення W1C у документації виробника; фактичну семантику треба перевіряти в manual конкретного пристрою."
---

## Question code

```c
#define CTRL_MODE_Pos  4u
#define CTRL_MODE_Msk  (7u << CTRL_MODE_Pos)
```

## Short answer

Типовий патерн: mask + shift.

`reg = (reg & ~CTRL_MODE_Msk) | ((mode << CTRL_MODE_Pos) & CTRL_MODE_Msk);`

Це явно показує, які біти змінюються, не залежить від bit-field layout і збігається з форматом datasheet. Але все ще є read-modify-write, тому для W1C або concurrent hardware bits треба дивитися register semantics.

Правило: masks/shifts більш portable для register definitions, ніж C bit-fields.[^iso-c-n1570]

## Detailed explanation

Mask-and-shift змінює вибраний діапазон бітів у значенні integer register: спочатку очищає цей діапазон, а потім вставляє туди нове закодоване значення.

У прикладі `CTRL_MODE_Pos` задає позицію молодшого біта, а `CTRL_MODE_Msk` позначає три біти поля `MODE`. Вираз спершу очищає лише ці біти інвертованою маскою. Потім він зсуває `mode` на потрібну позицію та застосовує маску, щоб сторонні біти не потрапили в результат. Інші біти початкового `reg` зберігаються. Таке явне відображення відповідає позиціям у документації пристрою й не залежить від implementation-defined розкладки C bit-fields.[^iso-c-n1570]

Наприклад, якщо поле починається з біта 4 і має ширину три, його значення займає біти 4–6. Маска відріже значення, яке виходить за межі поля, але таке мовчазне обрізання може приховати помилку виклику. Перевіряй значення, якщо можливі недопустимі режими. Також переконайся, що тип integer достатньо широкий для зсуву, а позиція менша за його ширину: зсув на ширину типу або більше не є коректним у C.[^iso-c-n1570]

Якщо `reg` є volatile hardware register, цей вираз виконує read-modify-write: читає register, поєднує значення та записує результат. Він підходить лише тоді, коли документована семантика register дозволяє таку послідовність. Для деяких W1C, read-to-clear або паралельно оновлюваних регістрів вона небезпечна; manual периферії може вимагати окремий SET/CLEAR register або прямий запис.[^stm32-w1c-manual]

**Типові помилки:**

- Застосувати OR без попереднього очищення старого поля.
- Не обмежити зсунутий `mode` маскою.
- Вважати mask-and-shift атомарним лише через те, що поле описане явно.

Перед використанням порівняй маску й позицію з таблицею регістрів, а потім перевір інструкції компілятора та правила доступу конкретного пристрою.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

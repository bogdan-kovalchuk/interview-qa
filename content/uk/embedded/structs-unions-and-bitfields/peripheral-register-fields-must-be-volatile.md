---
id: emb-structs-0010
title: "Чому поля peripheral register struct мають бути `volatile`?"
description: "Бо кожне поле представляє hardware register, значення якого може змінитися поза C-кодом або мати side effects при читанні/записі."
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

**Бо кожне поле представляє hardware register, значення якого може змінитися поза C-кодом або мати side effects при читанні/записі.**

Без `volatile` компілятор може кешувати status bit, прибрати читання read-to-clear register або об’єднати записи. Для Cortex-M це типова причина багів, які видно лише в release build.

Правило: register overlay має мати volatile-qualified fields або доступ через pointer to volatile register type.[^iso-c-n1570]

## Detailed explanation

`volatile` потрібен для доступу до memory-mapped register, коли кожне читання або запис має бути видимим для реалізації C, а значення може змінюватися поза потоком виконання програми. Наприклад, peripheral може змінити status bit після завершення передачі, а читання певного register може очистити прапорець. Компілятор не знає апаратного контракту, якщо доступ не описаний відповідним типом і способом.[^iso-c-n1570]

Без volatile-кваліфікації оптимізатор може використати раніше прочитане значення замість нового читання, прибрати читання, результат якого не використано, або оптимізувати послідовність записів як звичайну пам’ять. Для hardware register така зміна може пропустити новий стан пристрою або необхідний side effect. Кваліфікувати можна кожне поле структури або сам тип/вказівник, через який відбувається доступ; важливо, щоб вираз доступу фактично мав volatile-qualified тип.[^iso-c-n1570]

**Приклад:**

Якщо `STATUS` відображає стан апаратного блоку, повторне читання має бути окремим volatile access, а не кешованим значенням із попередньої ітерації. Для read-to-clear register навіть «зайве» читання може мати наслідки, тож кількість і порядок доступів беруть із документації MCU.

**Типові помилки:**

- Вважати, що volatile робить операцію атомарною або синхронізує кілька потоків чи ISR.
- Вважати, що volatile забезпечує правильний порядок між звичайною RAM і периферійними операціями або замінює memory barrier.
- Додавати volatile до всіх змінних «про всяк випадок», хоча це не виправляє гонки чи неправильну карту адрес.

У стандарті C точний ефект volatile access залежить від реалізації, тож для embedded-системи перевіряйте ABI та compiler documentation разом із reference manual. `volatile` керує тим, як компілятор обробляє доступи до об’єкта; він не надає апаратному регістру магічних властивостей і не замінює специфічних операцій set/clear, якщо вони потрібні для безпечного оновлення бітів.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

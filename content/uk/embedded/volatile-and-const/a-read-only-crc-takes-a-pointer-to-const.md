---
id: emb-volconst-0051
title: "Яке оголошення краще для функції CRC, яка лише читає дані?"
description: "Краще оголосити CRC як uint32_t crc32(const uint8_t *data, size_t len), бо функція лише читає дані."
track: embedded
section: volatile-and-const
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
uint32_t crc32(? data, size_t len);
```

## Short answer

Краще: `uint32_t crc32(const uint8_t *data, size_t len);`[^iso-c-n1570]

CRC не змінює buffer, тому pointer має бути to const data. Це дозволяє рахувати CRC для RAM buffer, Flash table, firmware image slice або string literal без втрати type safety.

Embedded-правило: `const` забороняє цій функції змінювати елементи через цей pointer, але не гарантує, що дані фізично розташовані у Flash або що інші alias не змінюють їх.[^iso-c-n1570]

## Detailed explanation

У параметрі `const uint8_t *data` слово `const` кваліфікує об’єкт, на який указує `data`: тіло CRC-функції може читати байти, але не може присвоїти нове значення через цей вираз. Сам pointer є локальним параметром, тому функція може пересунути його, наприклад перейти до наступного байта. Це відрізняється від `uint8_t * const data`, де незмінним був би сам pointer, а запис через нього залишався б дозволеним.[^iso-c-n1570]

Сигнатура також пояснює вимоги до caller-а. Звичайний mutable buffer можна передати у функцію, що приймає pointer-to-const, а рядковий літерал у C не треба приводити до змінного pointer. `const` є обмеженням доступу через конкретний тип pointer-а, а не обіцянкою глобальної незмінності об’єкта. Якщо обчислення потребує лише читання, такий інтерфейс документує це обмеження і дозволяє компілятору відхилити випадкове присвоєння у функції.[^iso-c-n1570]

Уявімо реалізацію, яка проходить `len` байтів і додає кожен до CRC-стану. Вона читає `data[i]`, але не має причини записувати `data[i]`; тому параметр має тип `const uint8_t *`. Якщо алгоритм справді має змінити буфер, наприклад обробити його на місці, `const` буде неправильним контрактом і його слід прибрати. Так само `const` не робить доступ до memory-mapped register безпечним: для такого доступу потрібні окремі платформні правила, зокрема відповідний `volatile`-кваліфікований тип.[^iso-c-n1570]

**Типова помилка:** написати `const uint8_t data` замість `const uint8_t *data`. У першому варіанті `data` – один байт за значенням, а не адреса буфера; параметр довжини тоді не має сенсу для обходу масиву. Зірочка є частиною типу pointer-а і не може бути пропущена.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

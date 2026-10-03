---
id: emb-volconst-0018
title: "Що означає `const uint8_t * const buf`?"
description: "buf є const pointer to const uint8_t."
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

**`buf` є const pointer to const `uint8_t`**.

Не можна змінити ані адресу pointer, ані дані через pointer. Це корисно для локального alias на read-only table, calibration data або read-only memory region.

Правило: перший `const` біля base type захищає дані; `const` після `*` захищає сам pointer.[^iso-c-n1570]

## Detailed explanation

`const uint8_t * const buf` оголошує const pointer на `const uint8_t`: не можна перепризначити сам pointer і не можна записувати в об’єкт через нього. Два кваліфікатори стосуються різних рівнів декларації: `const` біля базового типу обмежує доступ до цільового байта, а `const` після `*` обмежує значення pointer. Таке читання узгоджується з правилами кваліфікованих типів у C.[^iso-c-n1570]

Такий тип корисний для локального alias на таблицю констант, калібрувальні параметри чи інший буфер, який цей фрагмент коду лише читає і не має перенаправляти. Але `const` не обов’язково означає, що фізична пам’ять незмінна: якщо об’єкт не був оголошений const, інший некваліфікований pointer може його змінити, і тоді читання через `buf` побачить нове значення. Кваліфікатор обмежує операції, дозволені через цей вираз, а не створює копію чи блокування пам’яті.[^iso-c-n1570]

У параметрі функції верхньорівневий `const` на самому pointer впливає лише на локальний параметр-копію, тоді як `const` на елементі залишається суттєвим для типу даних, доступних через pointer. Якщо потрібен лише read-only доступ до даних, у публічному інтерфейсі часто достатньо `const uint8_t *buf`; додатковий `const` після зірочки має сенс переважно в реалізації, щоб захистити локальне ім’я від випадкового перепризначення. Це також не робить читання атомарним і не гарантує, що інший контекст не змінює буфер.[^iso-c-n1570]

**Приклад:** після `const uint8_t * const p = table;` обидва присвоєння `p = other` і `p[0] = 7` є недопустимими. Водночас початкове присвоєння при ініціалізації дозволене, а копіювання значень з `p` для обчислення контрольної суми не порушує обмежень.

**Типові помилки:**
- сприймати два `const` як надлишкове повторення одного правила;
- вважати, що вказана пам’ять глобально незмінна;
- додавати top-level `const` у параметр і очікувати, що це обмежить викликач.

## Sources

<!-- generated from frontmatter -->

---
id: emb-volconst-0017
title: "Що означає `uint8_t * const buf` у параметрі або локальній змінній?"
description: "buf є const pointer to mutable uint8_t."
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

**`buf` є const pointer to mutable `uint8_t`**.

Не можна присвоїти `buf = other`, але можна змінювати `buf[0]`. У параметрі функції top-level `const` на самому pointer рідко є частиною API, бо параметр і так копія pointer value.

Embedded-use case: локальний alias на фіксовану адресу або register pointer, який не має бути випадково переназначений.[^iso-c-n1570]

## Detailed explanation

`uint8_t * const buf` оголошує `buf` як const pointer на змінний `uint8_t`: після ініціалізації саме значення pointer не можна перепризначити, але через нього можна змінювати об’єкт, якщо той самий об’єкт не оголошено `const`. У декларації `const` стоїть після `*`, тож кваліфікує pointer, а не цільовий тип. Це відрізняється від `const uint8_t *buf`, де змінним може бути сам pointer, але запис через нього заборонено.[^iso-c-n1570]

Для локальної змінної цей запис доречний, коли адреса вже обрана і алгоритму потрібно змінювати дані за нею, не перенаправляючи alias. Наприклад, функція може отримати звичайний `uint8_t *`, скопіювати його в локальний `uint8_t * const current`, а потім використовувати `current` для оновлення байтів. Кваліфікатор не впливає на адресну арифметику чи права доступу до регіону: він лише забороняє присвоєння новому значенню самому `current`.[^iso-c-n1570]

У параметрі функції верхньорівневий `const` pointer не є частиною типу функції після коригування параметра; він обмежує лише локальну копію аргументу всередині визначення. Тому `void f(uint8_t * const p)` не обіцяє викликачеві, що передана адреса не зміниться деінде. Для memory-mapped register сама декларація pointer зазвичай потребує також `volatile` на цільовому типі, якщо апаратне забезпечення може змінювати значення або читання й записи мають спостережувані побічні ефекти; `const` цього не замінює.[^iso-c-n1570]

**Приклад:** у `uint8_t * const p = buffer;` вираз `p = other` не компілюється, а `p[0] = 7` дозволений, якщо `buffer` посилається на змінний об’єкт. Окремо перевіряйте, що початковий pointer коректний і що індекс лежить у межах буфера.

**Типові помилки:**
- плутати const pointer із pointer на const;
- робити висновок, що `const` на pointer захищає самі дані;
- вважати цей кваліфікатор достатнім для опису MMIO-доступу.

## Sources

<!-- generated from frontmatter -->

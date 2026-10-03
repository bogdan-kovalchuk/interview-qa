---
id: emb-volconst-0023
title: "Що скомпілюється, а що ні: `const int * const p`?"
description: "Не скомпілюються обидва записи: p = 3 і p = &y."
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
int x = 1, y = 2;
const int * const p = &x;
*p = 3;
p = &y;
```

## Short answer

**Не скомпілюються обидва записи: `*p = 3` і `p = &y`.**

`const int * const p` означає const pointer to const int. Через цей pointer не можна змінити ні pointed-to value, ні сам pointer value.

Embedded-приклад: fixed pointer на read-only lookup table або на read-only register, якщо додати ще `volatile` для hardware.[^iso-c-n1570]

## Detailed explanation

`const int * const p` є незмінним вказівником на `int`, доступний для читання через `p`, але не для запису через нього. Перше `const` кваліфікує тип об’єкта, на який вказує `p`, а друге – сам об’єкт-вказівник. Ініціалізація адресою `x` дозволена, бо після створення `p` адреса встановлюється один раз.[^iso-c-n1570]

Вираз `*p` має кваліфікований тип `const int`, отже він не є змінюваним lvalue для цілі присвоєння. Тому `*p = 3` заборонено. Сам `p` також є const-об’єктом; оператор `p = &y` намагався б змінити його значення після ініціалізації, тож це теж порушення обмежень.[^iso-c-n1570]

Читати значення можна: наприклад, `int copy = *p;` копіює число в окремий змінюваний об’єкт. Водночас оголошення не обов’язково робить `x` глобально незмінним: якщо `x` є звичайним `int`, код може змінити його через інше ім’я. Кваліфікатор обмежує доступ через цей вказівник; фактичний запис в об’єкт, початково оголошений `const`, має окремі правила і не стає дозволеним через приведення типу.[^iso-c-n1570]

Приклад застосування – незмінне посилання на таблицю параметрів, яку функція має лише читати. Якщо це апаратний регістр, `const` може передавати заборону запису на рівні типу, а `volatile` окремо описує спостережувані зовнішні зміни; потрібні кваліфікатори залежать від конкретного регістра. Типова помилка – вважати два `const` зайвими: вони захищають різні речі, сам вказівник і дані за адресою.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

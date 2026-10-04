---
id: emb-align-0039
title: "Що таке type punning через union і чим воно ризиковане?"
description: "Перегляд тих самих байтів як інший тип."
track: embedded
section: memory-alignment-and-endianness
level: junior
type: concept
tags: []
status: published
updated: 2026-10-04
content_revision: 2
reconciled_with:
  en: 4
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
  - source_id: cpp-draft-class-union
    title: "C++ Working Draft: Unions"
    url: https://eel.is/c%2B%2Bdraft/class.union
    accessed: 2026-10-04
    kind: spec
    version: null
    applicability: "Описує активний член union у C++; не слід переносити це правило на C."
---

## Question code

```c
union { float f; uint32_t u; } x;
x.f = 1.5f;
// читаємо x.u - бітовий патерн float
```

## Short answer

**Перегляд тих самих байтів як інший тип**. У C читання іншого члена union інтерпретує збережене представлення через його тип, але результат може бути залежним від реалізації; у C++ таке читання для цих типів зазвичай має undefined behavior, тож краще `memcpy` або `std::bit_cast`.

Результат залежить від endianness і представлення (наприклад IEEE 754), тож для локального inspection це може бути корисно, але не для portable serialization.

Правило: для дроту не використовуй union layout; серіалізуй явно з відомим byte order.[^iso-c-n1570]

## Detailed explanation

Type punning через union означає запис одного члена, а потім читання іншого, який займає ту саму пам’ять. Це не числове перетворення: програма не перераховує значення `float` у ціле, а просить інтерпретувати його об’єктне представлення як інший тип. У C стандарт допускає таке читання через union, але результат може залежати від реалізації; типи можуть мати різні розміри чи представлення, а окремі бітові шаблони можуть не бути допустимими значеннями цільового типу.[^iso-c-n1570]

У C++ діє модель активного члена union. Після запису `x.f = 1.5f` активним є `f`; читання `x.u` для цієї пари типів не є переносимим способом перегляду бітів і має undefined behavior. Для перетворення представлення між однаковорозмірними типами використовуй `memcpy`, або `std::bit_cast` починаючи з C++20, із перевіркою вимог до розміру та допустимого представлення.[^cpp-draft-class-union]

Навіть коли така операція підтримана конкретним компілятором, результат не задає portable wire format. Число, прочитане з байтів, залежить від розміру типів, floating-point representation та byte order. Наприклад, для передачі числа протоколом краще записати його байти за чітко визначеним порядком, а на іншому кінці зібрати значення за тією самою домовленістю; не покладатися на те, що інша система має ідентичний `union` layout.[^iso-c-n1570]

**Типова помилка:** називати це cast або вважати, що однакова адреса гарантує однакову семантику. Спільне сховище пояснює, чому байти перекриваються, але не скасовує правил мови щодо активного члена чи представлення типу.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

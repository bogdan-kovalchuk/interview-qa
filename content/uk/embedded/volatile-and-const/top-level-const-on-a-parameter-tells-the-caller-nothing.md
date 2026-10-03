---
id: emb-volconst-0041
title: "Чому `void f(uint8_t * const p)` не дуже корисне як API-контракт?"
description: "Бо const тут top-level і стосується лише локальної копії pointer parameter всередині функції."
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

**Бо `const` тут top-level і стосується лише локальної копії pointer parameter усередині функції.**[^iso-c-n1570]

Caller не бачить різниці: pointer value і так передається by value. Функція не може змінити pointer у caller-а незалежно від `const`. Але вона все ще може змінювати `p[0]`, бо pointed-to data не const.

Правило: якщо хочеш пообіцяти, що buffer не буде змінено через цей pointer, пиши `void f(const uint8_t *p)`, а не `uint8_t * const p`.[^iso-c-n1570]

## Detailed explanation

`const` у `void f(uint8_t * const p)` кваліфікує сам pointer `p`, який є локальним параметром функції. У C параметри передаються за значенням: під час виклику функція отримує власну копію pointer value, тому caller не може спостерігати, чи переприсвоює функція цю копію, і top-level `const` не змінює контракт виклику.[^iso-c-n1570]

Важливо розрізняти два місця для `const`. У `uint8_t * const p` незмінним є pointer: його не можна перенаправити на іншу адресу в тілі функції. Дані за адресою залишаються змінними, тому присвоєння на кшталт `p[0] = 1` дозволене, якщо сам об’єкт доступний для запису. Натомість у `const uint8_t *p` pointer можна переприсвоювати, але записувати через нього в елемент буфера не можна. Це обмеження доступу через конкретний вираз; саме по собі воно не доводить, що об’єкт ніде не змінюється.[^iso-c-n1570]

**Приклад:**

```c
void inspect(uint8_t * const p) {
    p[0] = 1;       // дозволено: pointed-to byte не const
    /* p = other; */ // помилка: сам pointer const
}

void read_only(const uint8_t *p) {
    /* p[0] = 1; */ // помилка: запис через const-qualified lvalue
    p = 0;          // дозволено: pointer не const
}
```

Типова помилка – сприймати `uint8_t * const` як обіцянку «функція не змінить буфер». Щоб виразити таку обіцянку на рівні інтерфейсу, став `const` перед типом елемента, як у `const uint8_t *p`. Якщо функція має змінювати дані, залишай `uint8_t *p`; локальний top-level `const` можна використовувати для внутрішньої дисципліни реалізації, але не як властивість API, видиму caller-у.[^iso-c-n1570]

## Sources

<!-- generated from frontmatter -->

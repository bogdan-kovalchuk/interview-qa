---
id: emb-macros-0044
title: "Trap: що не так із `#define BIT(n) (1 << (n))` при `BIT(31)`?"
description: "На платформі з 32-бітним int вираз 1 << 31 не має визначеного результату; unsigned-зсув також вимагає індексу в межах ширини типу."
track: embedded
section: inline-and-macros
level: junior
type: pitfall
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
---

## Short answer

На платформі з 32-бітним `int` літерал `1` має тип `int`, а `1 << 31` дає undefined behaviour: степінь двійки не представний у signed result type.[^iso-c-n1570]

На багатьох MCU «спрацює» як `0x80000000`, але стандарт цього не гарантує, і compiler може оптимізувати непередбачувано.

Для unsigned-зсуву результат обчислюється за модулем, але `n` однаково має бути меншим за ширину promoted left operand. Для фіксованої 32-бітної маски використовуйте `UINT32_C(1)` і перевіряйте `n < 32`.[^iso-c-n1570]

## Detailed explanation

Проблема `#define BIT(n) (1 << (n))` полягає не в самому факті встановлення старшого біта, а в типі лівого операнда та правилах зсуву. Десятковий integer constant `1` має тип `int`, якщо значення в ньому представне; на звичній платформі з 32-бітним `int` вираз `1 << 31` намагається отримати значення, яке не представне в signed result type, тому поведінка не визначена стандартом C.[^iso-c-n1570]

На системі з іншою шириною `int` число 31 може означати інше: сам приклад припускає 32-бітний `int`. Не можна переносити спостереження з одного MCU на інший або покладатися на те, що конкретний компілятор збереже бітовий шаблон. Після undefined behaviour компілятор не зобов’язаний відтворювати очікуваний результат.

Додавання суфікса `u` змінює тип константи на unsigned, але не робить будь-який зсув допустимим. За стандартом C від’ємний shift count або count не менший за ширину promoted left operand сам по собі спричиняє undefined behaviour; валідний unsigned left shift, навпаки, обчислюється модульно.[^iso-c-n1570] Для 32-бітної маски `UINT32_C(1)` задає відповідний unsigned тип із `<stdint.h>`, а індекс треба обмежити діапазоном 0–31.

**Типові помилки:**

- Вважати, що `1u` завжди має щонайменше 32 біти. Ширина `unsigned int` залежить від реалізації.
- Перевіряти лише знак операнда й забувати перевірку `n < width`.
- Називати проблему переповненням signed integer: тут діють конкретні правила shift operator, тож корисно перевірити тип після integer promotions і допустимість count.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->

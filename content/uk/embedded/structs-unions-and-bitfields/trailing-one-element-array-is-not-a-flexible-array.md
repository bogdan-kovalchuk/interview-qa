---
id: emb-structs-0034
title: "Trap: що не так із старим патерном `uint8_t data[1]` в кінці структури?"
description: "Це не flexible array member, а реальний масив з 1 байта."
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

## Short answer

<span class="warn">Це не flexible array member, а реальний масив з 1 байта.</span>

`sizeof(struct)` включає цей байт і padding після нього. Код, який виділяє `sizeof(struct) + len`, може отримати off-by-one layout або залежати від нестандартного extension. Сучасний C має стандартний синтаксис `data[]`.

Захист: у C99+ використовуйте flexible array member `uint8_t data[];` і перевіряйте allocation size на переповнення.[^iso-c-n1570]

## Detailed explanation

Масив `data[1]` є звичайним членом структури з одним елементом, а не flexible array member. У C стандартний гнучкий масив записують як `data[]` без розміру; він може бути лише останнім членом структури, яка має й інші іменовані члени.[^iso-c-n1570]

Різниця важлива під час обчислення обсягу пам’яті. `sizeof(struct Packet)` враховує повний розмір оголошеного об’єкта, включно з єдиним елементом `data[1]` та кінцевим padding, який може додати реалізація. Для структури з flexible array member цей розмір не враховує елементи гнучкого масиву. Пам’ять після нього виділяє програма, а не сам член автоматично розширює об’єкт.[^iso-c-n1570]

Приклад розрахунку: якщо `len` – кількість байтів корисних даних, то для гнучкого масиву базовий запит має враховувати зміщення члена `data` та `len`; на практиці часто використовують `sizeof(struct Packet) + len`, коли структура містить лише потрібний заголовок перед масивом. Треба також перевірити переповнення перед додаванням і врахувати, чи саме `sizeof` або `offsetof` відповідає обраному layout.[^iso-c-n1570]

Типова помилка – замінити `[1]` на `[]`, але залишити стару формулу `sizeof(struct Packet) + len - 1`; тепер вона може виділити замало пам’яті. Інший ризик – покладатися на компіляторне розширення для масиву нульового розміру: це не стандартний синтаксис flexible array member у C99. Для переносимого C99+ використовуйте `[]` і документовану формулу розміру.[^iso-c-n1570]

**Типова помилка:** вважати, що одиничний елемент у декларації є лише місцем-заповнювачем. Він має реальний розмір і впливає на layout та `sizeof`; перевіряйте allocation formula разом із фактичним оголошенням.[^iso-c-n1570]

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Sources

<!-- generated from frontmatter -->
